from ..basic_game import BasicGame


class PalworldGame(BasicGame):
    Name = "Palworld Support Plugin"
    Author = "Kaedras"
    Version = "1.0.0"

    GameName = "Palworld"
    GameShortName = "palworld"

    GameDocumentsDirectory = "%USERPROFILE%/AppData/Local/Pal"
    GameBinary = "Palworld.exe"
    GameDataPath = "Pal/Content/Paks/~mods"

    GameSteamId = 1623730
