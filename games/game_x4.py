from ..basic_game import BasicGame


class X4FoundationsGame(BasicGame):
    Name = "X4 Foundations Support Plugin"
    Author = "Twinki,BrandonM4"
    Version = "0.1.0"

    GameName = "X4: Foundations"
    GameShortName = "x4foundations"

    GameDocumentsDirectory = "%DOCUMENTS%/Egosoft/X4"
    GameDocumentsDirectoryLinux = "%USERPROFILE%/.config/EgoSoft/X4"
    GameBinary = "x4.exe"
    GameBinaryLinux = "testandlaunch"
    GameDataPath = "extensions"

    GameNexusId = 2659
    GameSteamId = 392160
