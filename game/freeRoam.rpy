label freeRoam:
    $ _skipping = True
    $ isRoaming = True
    while isRoaming:
        call screen actionsSelection()
    return

label endGame:
    return

label moveTo(locationtoGo): 
    if location != locationtoGo:  
        if locations[location]["region"] != locations[locationtoGo]["region"]:
            call doCrossRegionTravel(locationtoGo=locationtoGo) from _call_doCrossRegionTravel
            $ fadeDelay = 2
        else:
            $ fadeDelay = 0
        $location = locationtoGo
        call findCharactersAtCurrentLocation from _call_findCharactersAtCurrentLocation           
        call displayCurrentLocation(pauseAfterFade=fadeDelay) from _call_displayCurrentLocation
        $ cri("Travel to location \"" + locations[location]["name"] + "\" complete.")
        if len(charactersAtCurrentLocation) == 0:
            "It seems like no one is here."
    else:
        cri "System indicates current location matches chosen destination."
        cri "Navigation attempt aborted."
    return

label doCrossRegionTravel(locationtoGo):
    call setTravelTimeTo(regionId=locations[locationtoGo]["region"], currentRegionId=locations[location]["region"]) from _call_setTravelTimeTo
    $cri("Location \""+ locations[locationtoGo]["name"] + "\" is in a different region from current location.")
    cri "Estimated travel time is [distance] day(s). Proceed anyway?"
    menu:
        "Yes.":
            cri "Confirmation accepted."                    
            call adjustDate(daysToAdvance=distance) from _call_adjustDate
            $cri("Expected arrival: " + daysOfWeek[weekDay] + ", " + str(daysSinceActivation) + " days after unit activation.")
            return
        "No.":
            cri "Navigation aborted."
            jump freeRoam

label setTravelTimeTo(regionId, currentRegionId):
    python:
        distance = int(math.floor(math.sqrt((regions[currentRegionId]["x"]-regions[regionId]["x"])**2+(regions[currentRegionId]["y"]-regions[regionId]["y"])**2)))
    return

label findCharactersAtCurrentLocation:
    python:        
        charactersAtCurrentLocation = []
        for char in characters:
            if characters[char]["location"] == location:
                charactersAtCurrentLocation.append(char)

    return

label hideAllCharacters:
    python:
        for charId in characters:
            renpy.hide(characters[charId]["gameid"])

    return

label displayCurrentLocation(pauseAfterFade=0):
    call hideAllCharacters from _call_hideAllCharacters
    hide background 
    with fade
    python:
        renpy.music.stop(fadeout=1)
        renpy.sound.stop(fadeout=1)
        renpy.pause(pauseAfterFade)
        renpy.show(locations[location]["bg"], at_list=[top])
        renpy.with_statement(fade)
        i = 0
        for charId in charactersAtCurrentLocation:
            if i == 0:
                renpy.show(characters[charId]["gameid"] + " neutral", at_list=[right])
                renpy.with_statement(easeinright)
            elif i == 1:
                renpy.show(characters[charId]["gameid"] + " neutral", at_list=[left])
                renpy.with_statement(easeinleft)
            elif i == 2:
                renpy.show(characters[charId]["gameid"] + " neutral", at_list=[center])
                renpy.with_statement(fade)
            else:
                renpy.say("Error!", "Too many characters at this location! Clean it up!")
            i = i + 1
        if i != 0 and locations[location]["music"] != "":
            renpy.music.play(locations[location]["music"],fadein=1,loop=True)
    return

label advanceDay:
    cri "Begin end of day recharge cycle?"
    menu:
        "Yes.":
            jump endOfDay

        "No.":
            return
    return

label endOfDay:
    $renpy.music.stop(fadeout=1)
    call hideAllCharacters from _call_hideAllCharacters_1
    hide background
    with fade
    call adjustDate from _call_adjustDate_1
    cri "Entering standby."
    $renpy.sound.stop(fadeout=1)
    "Everything fades to black." 
    $ renpy.pause(1.5) 
    cri "Exiting standby."
    call setupCharacterLocations from _call_setupCharacterLocations
    call findCharactersAtCurrentLocation from _call_findCharactersAtCurrentLocation_1
    call displayCurrentLocation from _call_displayCurrentLocation_1
    $ cri("It is now " + daysOfWeek[weekDay] + ". Please perform tasks as appropriate.")
    cri "Bioenergy reserves returned to maximum!"
    return

label adjustDate(daysToAdvance=1):
    python:
        weekDay = (weekDay + daysToAdvance) % 7
        daysSinceActivation += daysToAdvance 
    return

label setupCharacterLocations:
    python:
        for char in characters:
            characters[char]["location"] = characterLocations[char][weekDay]
    return

label systemState:
    cri "{i}System Status{/i}\nSystem Identification: [unitId]\nNeural Interface Sync: [sync]\%"
    cri "{i}System Integrity{/i}\nArm Subsystem Integrity: [armsHealth]\%\nLeg Subsystem Integrity: [legsHealth]\%\nMain Body Integrity: [bodyHealth]\%\nMain Processing Integrity: [headHealth]\%"
    cri "{i}Public Identification Status{/i}\nPublic Identification (Name): [name]\nSystem Gender Identification: [gender]\nSystem Owner: [licenseOwner]"

    return

label talkTo(charId):
    $ renpy.jump("story"+charId+str(characters[charId]["storyState"]))
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
                    label "System.Act.Navigate"
                    null height 10
                    for i in locations:
                        if locations[i]["known"]:
                            textbutton regions[locations[i]["region"]]["name"]+": "+locations[i]["name"] action [Hide("navigationSelection"), Call("moveTo",locationtoGo=i)]

                    null height 5
                    textbutton "Change Action" action [Hide("navigationSelection"), Show("actionsSelection")]

            null

screen conversationSelection():
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
                    label "System.Act.Converse"
                    null height 10
                    for char in charactersAtCurrentLocation:
                        textbutton characters[char]["name"] action [Hide("conversationSelection"), Call("talkTo",charId=char)]

                    null height 5
                    textbutton "Change Action" action [Hide("conversationSelection"), Show("actionsSelection")]

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
                    label "System.Act"
                    null height 10
                    textbutton "Act.GetStatusLog" action [Hide("actionsSelection"), Call("systemState")]                    
                    textbutton "Act.Navigate" action [Show("navigationSelection"), Hide("actionsSelection")]
                    if len(charactersAtCurrentLocation) != 0:
                        textbutton "Act.Converse" action [Show("conversationSelection"), Hide("actionsSelection")]
                    null height 10
                    textbutton "Act.EnterStandby" action [Hide("actionsSelection"), Call("advanceDay")]
                    textbutton "Debug - End Game" action [Jump("endGame")]
            null
