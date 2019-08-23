init python:
    config.screen_width = 1024
    config.screen_height = 600

label gameSetup:
    python:
        sync = 80
        armsHealth = 0
        legsHealth = 0
        headHealth = 72
        bodyHealth = 11
        gender = "None"
        name = "No data found."
        unitId = "BIO-33cf94-735b28"
        licenseOwner = "Echo"
        location="Biorobotics Lab"

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
    call locationSetup from _call_locationSetup
    return

label locationSetup:
    python:
        locations = {
            "biolab":{"name":"Biorobotics Lab", "x":0, "y":0, "known":True, "bg":"background echo"},
            "trash":{"name":"Inside of Trash Can", "x":4, "y":3, "known":True, "bg":"background trash"}
        }
    return

label characterSetup:
    python:
        characters = [
            {"name":"Echo", "location":"Biorobotics Lab", "storyState":0, "charid":"echo"}
        ]
