import math
from pathlib import Path
from typing import Iterable, List

import mobase

from ..basic_features import BasicModDataChecker, GlobPatterns
from ..basic_game import BasicGame


class PalworldGame(BasicGame):
    Name = "Palworld Support Plugin"
    Author = "Kaedras"
    Version = "1.0.0"

    GameName = "Palworld"
    GameShortName = "palworld"
    GameSteamId = 1623730

    GameDocumentsDirectory = "%USERPROFILE%/AppData/Local/Pal"
    GameBinary = "Palworld.exe"
    # _ROOT is a placeholder value.
    # In order to properly apply load order to mods, custom mapping is used below.
    GameDataPath = "_ROOT"

    def init(self, organizer: mobase.IOrganizer) -> bool:
        super().init(organizer)
        self._register_feature(
            BasicModDataChecker(
                GlobPatterns(
                    valid=["*.pak"],
                    ignore=[
                        "*.mohidden",
                    ],
                )
            )
        )
        return True

    def _get_mods_path(self):
        """The directory path of where .pak files from mods should go"""
        return (
            Path(self.gameDirectory().absolutePath())
            / "Pal"
            / "Content"
            / "Paks"
            / "~mods"
        )

    def _active_mod_paths(self) -> Iterable[Path]:
        mods_parent_path = Path(self._organizer.modsPath())
        modlist = self._organizer.modList().allModsByProfilePriority()
        for mod in modlist:
            if self._organizer.modList().state(mod) & mobase.ModState.ACTIVE:
                yield mods_parent_path / mod

    def _active_mod_mappings(self, mod_paths: List[Path]) -> Iterable[mobase.Mapping]:
        if not mod_paths:
            return
        pak_priority_digits = math.floor(math.log10(len(mod_paths))) + 1

        for priority, mod_path in enumerate(mod_paths):
            pak_prefix = str(priority).zfill(pak_priority_digits) + "_"
            for child in mod_path.iterdir():
                dest_path = (
                    self._get_mods_path()
                    / child.with_stem(pak_prefix + child.stem).name
                )
                if child.is_dir() or child.suffix.lower() == ".pak":
                    yield mobase.Mapping(
                        str(child),
                        str(dest_path),
                        child.is_dir(),
                    )

    def mappings(self) -> List[mobase.Mapping]:
        return [
            # Not applying load order modifications to overwrites is OK
            # since the UX is better this way and it will generally work out anyways
            mobase.Mapping(
                self._organizer.overwritePath(),
                str(self._get_mods_path()),
                True,
                True,
            )
        ] + list(self._active_mod_mappings(list(self._active_mod_paths())))
