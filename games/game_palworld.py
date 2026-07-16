import mobase

from ..basic_features import BasicModDataChecker, GlobPatterns
from ..basic_game import BasicGame


class PalworldGame(BasicGame):
    Name = "Palworld Support Plugin"
    Author = "Kaedras"
    Version = "1.0.0"

    GameName = "Palworld"
    GameShortName = "palworld"
    GameBinary = "Palworld.exe"
    GameDataPath = "Pal/Content/Paks/~mods"
    GameDocumentsDirectory = "%USERPROFILE%/AppData/Local/Pal"
    GameSavesExtension = "sav"
    GameSteamId = 1623730

    def init(self, organizer: mobase.IOrganizer) -> bool:
        super().init(organizer)
        self._register_feature(
            BasicModDataChecker(GlobPatterns(valid=["*.pak"], ignore=["*.txt"]))
        )
        return True
