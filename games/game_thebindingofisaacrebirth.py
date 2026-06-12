from ..basic_game import BasicGame


class TheBindingOfIsaacRebirthGame(BasicGame):
    Name = "The Binding of Isaac: Rebirth - Support Plugin"
    Author = "Luca/EzioTheDeadPoet"
    Version = "0.1.0"

    GameName = "The Binding of Isaac: Rebirth"
    GameShortName = "thebindingofisaacrebirth"
    GameNexusName = "thebindingofisaacrebirth"
    GameNexusId = 1293
    GameSteamId = 250900
    GameBinary = "isaac-ng.exe"
    GameBinaryLinux = "run-x64.sh"
    GameDocumentsDirectory = "%DOCUMENTS%/My Games/Binding of Isaac Afterbirth+"
    GameDocumentsDirectoryLinux = "%GENERIC_DATA_LOCATION%/binding of isaac afterbirth+"
    GameDataPath = "%DOCUMENTS%/My Games/Binding of Isaac Afterbirth+ Mods"
    GameDataPathLinux = "%GENERIC_DATA_LOCATION%/binding of isaac afterbirth+ mods"
    GameSupportURL = (
        r"https://github.com/ModOrganizer2/modorganizer-basic_games/wiki/"
        "Game:-The-Binding-of-Isaac:-Rebirth"
    )

    def iniFiles(self):
        return ["options.ini"]
