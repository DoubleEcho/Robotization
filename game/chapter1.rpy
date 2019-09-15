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

    show background echo at top
    with fade

    cri "Audio/Visual systems connected."
    cri "An administrator has been notified of a successful startup."

    "You see someone moving through the lab."

    $ renpy.music.play(darkGroove,fadein=1,loop=True)

    show echo neutral at right
    with easeinright

    echo "Good morning, Servitor [name]."
    echo "How are you feeling?"
    echo "Much better, I'd guess."
    echo "Why don't you take a look at your system status now?"

    $ butThouMustCounter = 0

label lookAtStatusPlease:
menu:
    "{i}System.Act.GetStatusLog{/i}":
        call systemState from _call_systemState_1
        jump lookedAtStatus

    "... no, I won't.":
        call butThouMust from _call_butThouMust
        jump lookAtStatusPlease

label lookedAtStatus:
    
    echo "Now {i}that's{/i} a good looking status report."
    echo "I think it's safe to pull you off life support now."
    hide echo
    with easeoutleft
    $renpy.pause(3)
    $renpy.sound.stop(fadeout=1)
    show echo neutral at right
    with easeinleft
    echo "Your sync with the neural interface is a bit low, but that's not surprising."
    echo "Typically, the neural interface is built off of..."
    $ renpy.pause(1.5)
    echo "Well, I don't want to bore you with the details, [name]."
    menu:
        "I'm interested to hear.":
            jump explainInterface
        "I don't think I'd understand, anyway.":
            jump noExplainInterface
        "{i}Say nothing.{/i}":
            jump prologueExplain

label explainInterface:
    $ characters["echo"]["relationship"] += 1
    echo "Oh, you are?"
    echo "I'm not used to folks caring about the nitty-gritty of how their bodies work."
    echo "Most of the time, people don't care about things that don't affect their day to day."
    echo "But, I think it's worth trying to understand the \"why\" of our lives, not just the \"what.\""
    echo "... if that makes any sense."
    $ renpy.pause(2)
    echo "Sorry, I got a little off track."
    echo "You wanted to know about the neural interface, right?"
    echo "Usually, when I'm making a cyborg, I start with a scan of someone's neural activity."
    echo "From there, you can make a biomechanical duplicate of it."
    echo "Since you have an accurate representation of their neural traffic, it's easy to make a basic neural interface to sync the brain to its new body."
    echo "In your case, it wasn't so simple."
    echo "You see, when I..."
    $ renpy.pause(1)
    echo "... got hold of you, your body was in exceptionally bad condition."
    echo "For the purposes of making a cyborg, the state of the original body doesn't {i}typically{/i} matter, since it's all going to get replaced by a new one anyway."
    echo "However, the brain needs to be intact to take an initial scan and make a duplicate."
    echo "And yours {i}really{/i} wasn't."
    echo "In order for you to survive- that is, the cyborg \"you\"- I had to simulate neural traffic to \"fill out\" what was missing."
    echo "That's what your CRI is."
    echo "It fulfills the function of being a neural interface between your brain and your body, but it also fills in the gaps where there wasn't any neural traffic to copy."
    echo "Essentially, it generates thoughts for you when the rest of your brain doesn't have the capacity to do so."
    echo "Which sounds... kind of terrifying when I phrase it like that, to be honest."
    echo "However, your sync with the CRI should build up over time. Once it's fully in sync with you, it'll be an inseperable part of your mind, and you'll just kind of... subsume it."
    echo "Until then, you might experience some oddities."
    echo "Nothing major, hopefully."
    echo "I hope that makes sense."
    $prologueQuestions = [True, True, True, True]

label prologueAnyQuestions:  
    menu:
        "I feel like I understand most of what's going on.":
            $ characters["echo"]["relationship"] += 1
            echo "Good to hear."
            echo "I know that's a lot to take in, but I hope it helps you get some understanding of the situation you're in."
            jump prologueExplain
        "What do you mean you \"got hold of me?\"" if prologueQuestions[0]:
            $ renpy.pause(2)
            echo "I'd rather not talk about that right now."
            echo "The events that lead up to it were simultaneously extraordinarily stressful for me and decidedly not the high point of my career."
            echo "If it's all the same to you, I need some time to think about it myself."
            echo "I've been buried in my work trying to get you up and running, so I haven't had a lot of time to process it."
            echo "If it's any consolation, I had nothing to do with the events that left you injured."
            echo "So, lets leave it at that."
            menu:
                "Alright.":
                    echo "Any other questions?"
                    $ prologueQuestions[0] = False
                    jump prologueAnyQuestions
                "I want you to tell me what happened.":
                    $ characters["echo"]["relationship"] = -10
                    echo "Well, we're at at an impasse, then."
                    $ renpy.pause(1)
                    echo "I don't think I want to talk about this anymore."
                    echo "Let's move on."
                    jump prologueExplain
        "What happened to me that left me injured?" if prologueQuestions[1]:
            echo "Unfortunately, I don't know."
            echo "I only got to see the aftermath."
            echo "Is there anything else you wanted to know?"
            $ prologueQuestions[1] = False
            jump prologueAnyQuestions
        "Should I be worried about those \"oddities\"?" if prologueQuestions[2]:
            echo "Not really."
            echo "I mean, they're not totally innocuous, but they shouldn't be harmful, either."
            echo "You might see things that aren't really there or have odd \"dreams\" while you're in standby."
            echo "It's just a symptom of the bad sync."
            echo "There's nothing I can really do to help you, so you'll just need to soldier on."
            echo "It should stop eventually."
            echo "I'm sorry I can't do any more for you."
            $ prologueQuestions[2] = False
            jump prologueAnyQuestions
        "I don't like the CRI very much." if prologueQuestions[3]:
            $ characters["echo"]["relationship"] -= 1
            echo "What, like... its personality?"
            echo "Sorry, can't help you there. It's based on {i}your{/i} neural traffic."
            echo "Or do you mean its functionality?"
            echo "I don't really know how to respond to that."
            $ prologueQuestions[3] = False
            jump prologueAnyQuestions


label noExplainInterface:
    $ characters["echo"]["relationship"] -= 1
    echo "Ah, of course."
    echo "Sorry, I sometimes get..."
    $ renpy.pause(1)
    echo "... lost in the little details, I guess."
    $ renpy.pause(1)
    echo "Either way."
    jump prologueExplain

label prologueExplain:
    echo "I wouldn't feel right just letting you wander around the planet completely freely at this point."
    echo "I want to make sure that you've got a decent grip on your systems, and have an idea of what Xeania wants from you."
    echo "At least two of your action systems are working: your status log and your speech system."
    echo "You've exclusively been responding to me since your boot, so you haven't had to intentionally launch the latter."
    echo "Just keep in mind that you'll have to manually do so to initiate a conversation with someone."
    echo "It's not as complicated as it sounds. You'll see when you try."
    echo "There're a few other main systems."
    echo "You've got a built in navigation system that can help you find your way to any location on the planet."
    echo "As an added bonus, if the trip is particularly long, you can put yourself into standby during the trip and let your body take you there automatically."
    echo "Due to company policy, it can only navigate you to places you've already been or have been explicitly told about."
    echo "That's mainly to keep cyborgs and other bots from navigating to people's private hideaways."
    echo "Just something to keep in mind."
    echo "In addition, you'll have access to an \"interfacing\" system that will let you interact with the automation network as well as physical data ports, among other things."
    echo "One of the biggest benefits of this system is that you get access to all the data and tools that the fully robotic parts of staff do."
    echo "Basically, you get the benefit of being half human, half AI."
    echo "It's very versatile."
    echo "As with the navigation system, there are a bunch of limits due to company policy, so you'll just have to try things to see what happens."
    echo "The CRI should be able to help you detect things you can interface with, and it'll give you the option to do so when you can."
    echo "Finally, you have a very robust standby system."
    echo "Rather than having to sleep, you'll need to recharge each night."
    echo "It takes a lot of power to keep you running."
    echo "Activate the standby system and the CRI will take over."
    echo "It'll take you to the nearest recharging station to fill up your batteries overnight, then return you to where you were when you started the standby process."
    echo "That should all happen while you're in standby, too, so you won't even notice it."
    if characters["echo"]["relationship"] >= 2:
        echo "I think that's pretty cool, don't you?"
        echo "Actually, now that I think about it..."
        echo "I don't offer this to most new cyborgs, but you've been interested in the inner workings of your new body."
        echo "If you ever wake up and you're not in the same spot as where you entered standby, it means that someone or something prevented the CRI from returning you to where you were."
        echo "If you come back to me after that happens, I can try to figure out what caused it."
        echo "It's very hard to do and often doesn't work, since your neural interface doesn't record much of anything while you're in standby, so no promises."
        echo "I'll give it my best shot, though."
        $ echoBadStandbyHelp = True
    else:
        $ echoBadStandbyHelp = False
    echo "That's the gist of your main system functions."
    echo "As for the company..."
    echo "Xeania doesn't give anything away for free."
    echo "It is a huge company, after all. It wouldn't make sense to do anything else."
    echo "I convinced them to let me rebuild you on the condition that you would work for them."
    echo "Luckily, the job isn't very complex."
    echo "Since you bridge the gap between the various technological systems at the resort and the people who pay to vacation here..."
    echo "... you'll make a {i}great{/i} service attendant."
    echo "Essentially, you'll get paid for acting as a general purpose worker bot, as well as for helping individual customers with their specific needs."
    echo "For the first, there are datapoints you can interface with that'll install any subroutines you need to complete a specific task, then you can have CRI autopilot you through the work."
    echo "If you want to get some extra credits or build a relationship with the customers, you can talk to various patrons of the resort."
    echo "You might make some friends. Maybe some very good friends."
    echo "They might even buy you off of Xeania if they can afford it."
    echo "Either way, Xeania is going to take a cut out of your pay each week. Make sure that you can afford it."
    echo "Xeania's going to find their own way to get their value out of you if you don't."
    echo "I'm speaking from experience when I say that you don't want that."
    echo "I think that about sums it all up."
    echo "It's about time you got out of the lab, anyway."
    if characters["echo"]["relationship"] >= 1:
        echo "Feel free to come back any time if you need repairs or if you just want to chat."
    else:
        echo "If you need repairs, this is the place to come."
    echo "You should be able to pull a list of availible actions in your mind, once we're done here."
    $ echo("We're in the Central Administration region of the Xeania, and I've limited your access to the other " + str(len(regions) - 1) + " regions of the planet for now.")
    echo "Apart from that, you've got free reign. Get some use out of your body to get a feel for it, then come back later so I can run a checkup."
    echo "If everything checks out then, I'll give you full access to the navigation terminal here in the lab, which will give you navigation information for the other regions."
    echo "I've got a few other things to work on today, but I'm usually here in the lab on weekdays, if you need me."
    echo "I'm going to head out, and I'd recommend that you do too."
    if characters["echo"]["relationship"] >= 0:
        echo "Good luck with all this, [name]."
        echo "I know it's a lot of information."
    else:
        echo "I wish you success in your new life, Servitor."
    echo "I'll talk with you soon."
    $ echoStory1Day = 7
    $ characters["echo"]["location"] = ""
    $renpy.music.stop(fadeout=2)
    hide echo
    with easeoutright
    call findCharactersAtCurrentLocation from _call_findCharactersAtCurrentLocation_3


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