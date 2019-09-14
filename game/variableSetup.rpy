init python:
    config.screen_width = 1024
    config.screen_height = 600

label gameSetup:
    python:
        day = 0
        sync = 80
        armsHealth = 0
        legsHealth = 0
        headHealth = 72
        bodyHealth = 11
        gender = "None"
        name = "No data found."
        unitId = "BIO-33cf94-735b28"
        licenseOwner = "Echo"

    return


label chapterOneSetup:
    python:
        armsHealth = 100
        legsHealth = 100
        headHealth = 100
        bodyHealth = 100
        licenseOwner = "Xeania Resorts Incorporated"
    return

label setupAllRoamData:
    $ namekey = "name"
    $ daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    $ location = "biolab"
    call locationSetup from _call_locationSetup
    call characterSetup
    call findCharactersAtCurrentLocation
    return

label locationSetup:
    python:
        locations = {
            "biolab":{"name":"Biorobotics Lab", "x":0, "y":0, "known":True, "bg":"background echo", "music":"sound/music/Dark Groove.mp3"},
            "trash":{"name":"Inside of Trash Can", "x":4, "y":3, "known":True, "bg":"background trash", "music":""}
        }
    return

label characterSetup:
    python:
        characters = {
            "echo" : {"name":"Echo", "location":"biolab", "storyState":0, "gameid":"echo"}
        }
        

        characterLocations = {
            "echo": ["biolab", "biolab", "biolab", "biolab", "trash", "trash", "trash"]
        }

    return
