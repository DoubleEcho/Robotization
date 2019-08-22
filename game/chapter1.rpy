label chapter1:

    call chapterOneSetup from _call_chapterOneSetup

    cri "Booting..."
    cri "Interface version 1.0.0."
    cri "It has been 23 days since last succesful boot."
    cri "Neural connection established."
    cri "System state... good."
    cri "Unit [unitId] boot success."
    cri "Boot message: {i}Hello World, [name]!{/i}"

    $ renpy.sound.play("sound/ventilator.wav",fadein=2,loop=True)

    show echobg at top
    with fade

    cri "Audio/Visual systems connected."
    cri "An administrator has been notified of a successful startup."

    "You see someone moving through the lab."

    $ renpy.music.play("sound/music/Dark Groove.mp3",fadein=1,loop=True)

    show echoNeutral at right
    with easeinright

    echo "Good morning, Servitor [name]."
    echo "How are you feeling?"
    echo "Much better, I'd guess."
    echo "Why don't you take a look at your system status now?"

    $ butThouMustCounter = 0

label lookAtStatusPlease:
menu:
    "Act.GetStatusLog":
        call systemState from _call_systemState_1
        jump lookedAtStatus

    "... no, I won't.":
        call butThouMust from _call_butThouMust
        jump lookAtStatusPlease

label lookedAtStatus:
    
    echo "Better, isn't it?"


    call setupAllRoamData

    jump freeRoam

label butThouMust:
    if butThouMustCounter < 3:
        echo "I mean, it could be interesting."
        echo "Why don't you take a look, for me?"
        $ butThouMustCounter += 1
        return
    else:
        echo "But thou must!"
        return