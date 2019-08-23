label freeRoam:
    $ isRoaming = True
    while isRoaming:
        call screen actionsSelection()
    return

label endGame:
    return

label moveTo(locationtoGo): 
    if location != locationtoGo:
        $ renpy.show(locations[locationtoGo]["bg"])
        $ location = locationtoGo
        "Character location is now [location]."
    else:
        "Character location is already [location]."
    return

label systemState:
    cri "{i}System Status{/i}\nSystem Identification: [unitId]\nNeural Interface Sync: [sync]\%"
    cri "{i}System Integrity{/i}\nArm Subsystem Integrity: [armsHealth]\%\nLeg Subsystem Integrity: [legsHealth]\%\nMain Body Integrity: [bodyHealth]\%\nMain Processing Integrity: [headHealth]\%"
    cri "{i}Public Identification Status{/i}\nPublic Identification (Name): [name]\nSystem Gender Identification: [gender]\nSystem Owner: [licenseOwner]"
    nvl clear

    return

label talkToPresent:
    "This ain't do shit yet."
    return

screen navigationSelection():
    # This vbox organizes everything.
    vbox:

        ypos 0.33
        spacing 5
        grid 3 1:

            spacing 5
            xfill True

            null

            frame:
                xpadding 5
                ypadding 5
                xfill True

                vbox:
                    label "Act.Navigate"
                    null height 10
                    for i in locations:
                        if locations[i]["known"]:
                            textbutton locations[i]["name"] action [Hide("navigationSelection"), Call("moveTo",locationtoGo=i)]

                    null height 5
                    textbutton "Change Action" action [Hide("navigationSelection"), Show("actionsSelection")]

            null

screen actionsSelection():
    vbox:

        ypos 0.33
        spacing 5
        grid 3 1:

            spacing 5
            xfill True

            null

            frame:
                xfill True
                xpadding 5
                ypadding 5

                vbox:
                    label "System.Action"
                    null height 10
                    textbutton "Action.GetStatusLog" action [Hide("actionsSelection"), Call("systemState")]                    
                    textbutton "Action.Navigate" action [Show("navigationSelection"), Hide("actionsSelection")]
                    textbutton "Action.InitiateConversation" action [Hide("actionsSelection"), Call("talkToPresent")] 
                    textbutton "Debug - End Game" action [Jump("endGame")]
            null
