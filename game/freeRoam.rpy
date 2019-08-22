label freeRoam:
    $ isRoaming = True
    while isRoaming:
        call screen actionsSelection()
    return

label endGame:
    return

label test:
    echo "This is how we move it."
    return

label systemState:
    crinvl "System Status\nSystem Identification: [unitId]\nNeural Interface Sync: [sync]\%"
    crinvl "System Integrity\nArm Subsystem Integrity: [armsHealth]\%\nLeg Subsystem Integrity: [legsHealth]\%\nMain Body Integrity: [bodyHealth]\%\nMain Processing Integrity: [headHealth]\%"
    crinvl "Public Identification Status\nPublic Identification (Name): [name]\nSystem Gender Identification: [gender]\nSystem Owner: [licenseOwner]"
    nvl clear

    return

screen navigationSelection():
    # This vbox organizes everything.
    vbox:

        ypos 20
        spacing 5
        grid 3 1:

            spacing 5
            xfill True

            null

            frame:
                xfill True

                vbox:
                    label "Act.Navigate"
                    null height 10
                    for i in locations:
                        textbutton i action Call("test")
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

                vbox:
                    label "System.Action"
                    null height 10
                    textbutton "Action.GetStatusLog" action Call("systemState")                    
                    textbutton "Action.Navigate" action [Show("navigationSelection"), Hide("actionsSelection")]
                    textbutton "Debug End Roam" action [Jump("endGame")]
            null
