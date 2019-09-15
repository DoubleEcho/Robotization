init python:
    config.screen_width = 1024
    config.screen_height = 600
    import math

label gameSetup:
    python:
        weekDay = 0
        daysSinceActivation = 0
        sync = 40
        armsHealth = 0
        legsHealth = 0
        headHealth = 72
        bodyHealth = 11
        gender = "None"
        name = "No data found."
        unitId = "BIO-33cf94-735b28"
        licenseOwner = "Echo"

    call setupAllRoamData from _call_setupAllRoamData

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
    call characterSetup from _call_characterSetup
    call findCharactersAtCurrentLocation from _call_findCharactersAtCurrentLocation_2
    return

label locationSetup:
    python:
        locations = {
            "biolab":{"name":"Biorobotics Lab", "region":"central", "known":True, "bg":"background echo", "music":darkGroove},
            "trash":{"name":"Inside of Trash Can", "region":"central", "known":True, "bg":"background trash", "music":""},
            "crossRegionTest":{"name":"Test Location", "region":"testRegion", "known":True, "bg":"background trash", "music":""}

        }

        regions = {
            "central":{"name":"Central Administration", "x":0, "y":0},
            "testRegion":{"name": "testRegion", "x":0,"y":1}
        }
    return

label characterSetup:
    python:
        characters = {
            "echo" : {"name":"Echo", "location":"biolab", "storyState":0, "relationship":0, "gameid":"echo"}
        }
        

        characterLocations = {
            "echo": ["biolab", "biolab", "biolab", "biolab", "trash", "trash", "trash"]
        }

    return
