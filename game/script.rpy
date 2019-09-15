# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define crinvl = Character("CRI", color="#33FF66", what_color="#33FF66", kind=nvl)
define echo = Character("Echo", color="22b4dd")
define system = Character("???", color="#33FF66", what_color="#33FF66")
define cri = Character("CRI", color="#33FF66", what_color="#33FF66")
define you = Character("[name]")
image echo neutral= "echo/Echoclothed.png"
image background echoinit = "background/EchoLabBackgroundClear.png"
image background echo = "background/EchoLabBackground.png"
image background trash = "background/trash.jpg"
define darkGroove = "sound/music/Dark Groove.mp3"

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

    show background echoinit at top
    with dissolve

    $ renpy.sound.set_volume(0.1)
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

    cri "An administrator has been notified of a successful startup."

    "Well, well. Look who finally woke up."

    show background echo at top
    with dissolve

    $ renpy.music.set_volume(0.5)
    $ renpy.music.play(darkGroove,fadein=1,loop=True)

    show echo neutral at right
    with easeinright
    
    echo "How are you feeling? A little sore, I'd expect."
    "You attempt to reply, but you find that you're unable."
    "Other attempts to move your body prove equally futile."
    cri "Warning: The administrator has initiated a lockout of all motor functions until further notice."
    cri "Reason: Severe system damage."
    cri "Please refer to system information for further details."
    echo "I'll pull up your logs for you."
    echo "It'll shed a little light on your situation."

    call systemState from _call_systemState

    echo "\"Zero percent integrity\" means that part is entirely missing, by the way. I know you can't move your head to check for yourself."
    echo "You were in quite the state when I got to you. Still alive, but only barely."
    echo "Not enough to survive the night, unfortunately."
    echo "I was able to rebuild something from what was left, though. Sentient AIs, especially cyborgs like you, are always in demand."

    $ renpy.pause(1.5)

    echo "That sounded {i}much{/i} worse than I imagined it would."
    echo "I didn't rebuild you up to sell you off."
    echo "What you do going forward is, to some extent, up to you."
    echo "However, there's a bit of a limitation."
    echo "We're on a resort planet called Xeania."
    echo "The only reason you're still with us is because the company that owns the planet gave me the resources to save you."
    echo "That means that you're indebted to them, though."
    echo "Same as me."

    #echo smile
    echo "I'm Echo, by the way. Primary biorobotics technician for Xeania Resorts Inc."
    echo "I put myself in your memory so you'd be able to recognize me when you woke up."

    #echoStandard
    echo "Speaking of which, I woke you up because I'd like your input."
    echo "As you saw from the log, I have a lot of your body to put back together. I could just put you back the way you were before but..."
    echo "Honestly, the way you were before probably isn't much of a representation of your mental state now."
    echo "You've got the chance to be somebody else..."

    #echosmile
    echo "...and I love to help people change."

    #echoStandard
    echo "So, that being said, lets start from the basics."
    echo "Are you going to be a boy-bot or a girl-bot?"
    $selectFlag = True

label genderTryAgain:
menu:
    "Male.":
        $ gender = "Male"
        jump initGender
    "Female.":
        $ gender = "Female"
        jump initGender
    "Something else?" if selectFlag:
        #echosmile
        echo "You're a bot after my own heart, I see."
        echo "Those are premium products you're asking for, though. Can't give 'em away for free."
        echo "You'll have to come back with a few credits."

        #echoStandard
        echo "Better stick with the basics for now."
        $ selectFlag = false
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
    
    $renpy.music.stop(fadeout=1)
    hide echo
    hide background
    with fade

    cri "Powering down..."
    $renpy.sound.stop(fadeout=1)
    "Everything fades to black."

    $ renpy.pause(3)

    jump chapter1

label endgame:
    return
