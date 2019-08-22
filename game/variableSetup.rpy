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
    call locationSetup
    return

label locationSetup:
    python:
        locations = ["Biorobotics Lab"]
    return
