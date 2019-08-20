# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define echo = Character("Echo", color="22b4dd")
define system = Character("???", color="#33FF66", what_color="#33FF66")
define cri = Character("CRI", color="#33FF66", what_color="#33FF66")
define you = Character("[name]")
image echoNeutral = "echo/Echoclothed.png"
image echobginit = "EchoLabBackgroundClear.png"
image echobg = "EchoLabBackground.png"



# The game starts here.

label start:

    call gameSetup from _call_gameSetup

    system "Booting..."

    system "Interface version 0.2.1."

    system "Neural connection established."

    system "Neural matrix integrity is only 34\%."

    system "System flag \"reconstruct-missing\" is set to \"simulate\"."

    system "Creating new neural traffic..."

    $ renpy.pause(1.6)

    system "Done in 1601 ms."

    system "Neural matrix integrity is 96\%."

    system "Rebuild successful. Audio/Visual systems connecting."

    system "Boot message: {i}Welcome back.{/i}"

    show echobginit at top
    with dissolve

    $ renpy.sound.set_volume(0.3)
    $ renpy.sound.play("sound/ventilator.wav",fadein=2,loop=True)

    "You suddenly find that you can see and hear."


    system "Beginning organic/digital interface confirmation."

    cri "I am CRI, your Cognition Replacement Interface."

    cri "If you can perceive these messages, you can communicate with me through thought."

    cri "If you can hear me, please think the word \"Yes.\""

menu:
    "... yes?":
        jump understood

    "... no.":
        jump notunderstood

label notunderstood:
    cri "Your negative response indicates that communication has been established."

    cri "Noted: Organic system may be hostile."

label understood:

    cri "Thank you. Our administrator has been notified of a successful startup."

    "Well, well. Look who finally decided to wake up."

    show echobg at top
    with dissolve
    hide echobginit

    show echoNeutral at right
    with easeinright
    
    echo "How are you feeling? A little sore, I'd expect."
    "You attempt to reply, but you find that you're unable."
    "Any attempts to move your body at all prove equally futile."
    cri "Warning: The administrator has initiated a lockout of all motor functions until further notice."
    cri "Reason: Severe system damage."
    cri "Please refer to system information for further details."
    echo "You might want to do that."
    echo "It could shed a little light on your situation."

    call systemState from _call_systemState

    echo "\"Zero Percent Integrity\" means entirely missing, by the way. I know you can't move your head to look."
    echo "You were in quite the state when I found you. Still alive, but only barely."
    echo "Not enough to survive the night, unfortunately."
    echo "I was able to rebuild something from what was left, though. Sentient AIs are always in demand."

    $ renpy.pause(1.5)

    echo "... I'm not planning on just selling you off, if that's what it seems like."
    echo "What you do going forward is, to some extent, up to you."
    echo "However, I can make you an offer."
    echo "We're on a resort planet called /FIXME/. They're always looking for... service bots."

    #echo smile
    echo "Take that as you will."

    #echoStandard
    echo "I woke you up because I'd like your input."
    echo "As you saw, I have a lot of your body to put back together. I could just put you back the way you were before but..."
    echo "Honestly, the way you were before probably isn't much of a representation of your mental state now."
    echo "You've got the chance to be somebody else..."

    #echosmile
    echo "...and I love to help people change."

    #echoStandard
    echo "So, that being said, lets start from the basics."
    echo "Are you going to be a boy-bot or a girl-bot?"
label genderTryAgain:
menu:
    "Male.":
        $ gender = "Male"
        jump initGender
    "Female.":
        $ gender = "Female"
        jump initGender
    "Something else?":
        #echosmile
        echo "A bot after my own heart, I see."
        echo "Those are premium products you're asking for, though. Can't give 'em away for free."
        echo "You'll have to come back with a few credits."

        #echoStandard
        echo "Better stick with the basics for now."
        jump genderTryAgain
label initGender:
    cri "Registered Unit as [gender]."
    #echosmile
    echo "Not what I would have guessed, but I'm sure it'll work."
    #echoStandard
    echo "Only one major thing left: a name."
    echo "Unless you're planning on being a barcode."

    python:
        name = renpy.input("What is your name going to be?")
        name = name.strip()

    if not name:
        echo "If you're not going to suggest anything, I'll pick."
        $ name = "Naukar"

    cri "Registered Public Identification: [name]"

    #echosmile
    echo "That's everything."
    echo "So for now, I need some private time to get you fixed up."
    echo "See you on the other side."

    $renpy.sound.stop()
    hide echoNeutral
    hide echobg
    with fade

    cri "Entering standby."

    "Everything fades to black."


label endgame:
    return
