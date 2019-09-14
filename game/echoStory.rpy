label storyecho0:
    echo "How's that new body treating you?"
menu:
    "I like it!":
        echo "That's good to hear!"
        echo "Most newly-cyborgified people struggle with their new bodies."
        echo "You seem to be taking it exceptionally well."
        echo "That being said, it's probably worth doing a checkup on your body after you've spent some time in it."
        jump storyecho0_2

    "It has some problems...":
        echo "That's not surprising."
        echo "Most newly-cyborgified people struggle with their new bodies."
        echo "If you give it a chance, it should start to feel more natural."
        echo "That being said, biorobotic bodies suffer wear and tear a bit differently from natural bodies."
        echo "It's probably worth doing a checkup on your body after you've spent some time in it."
        jump storyecho0_2

label storyecho0_2:
    echo "Go out there and get some more use out of it, then come back and talk to me in a week."
    echo "If things are still looking good then, I'll let you completely loose."
    echo "As an added bonus, I'll even clear you for modification."
    echo "Sound good?"
    $ characters["echo"]["storyState"] = 1
    jump freeRoam

label storyecho1:
    echo "Hey, welcome back."
    echo "I'd like to do a checkup after you've gotten a {i}little{/i} bit more use out of your body."
    echo "So, just take some time to got out and use it some more, okay?"
    jump freeRoam