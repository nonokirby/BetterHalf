define quickerd = Dissolve(0.2)

transform lefty:
    xanchor 0.5
    xpos 0.3
    yalign 1.1

transform left_center:
    xanchor 0.5
    xpos 0.35
    yalign 1.1

transform righty:
    xanchor 0.5
    xpos 0.65
    yalign 1.1

transform faceright:
    xzoom -1

transform faceleft:
    xzoom +1

define narrator = Character (None, what_color="#e8e8e7")
define t = Character("Thiu", what_color="#2ecbba", who_color="#f3f0e9")
define h = Character("Thiu", what_color="#5bd896", who_color="#f3f0e9")
define s = Character("Thiu", what_color="#71a8d2", who_color="#f3f0e9")
define j = Character("The Jerkface", what_color="#c2a2e2", who_color="#f3f0e9")
define l = Character("Lua", what_color="#c2a2e2", who_color="#f3f0e9")
define a = Character("Tal", what_color="#f39af9", who_color="#f3f0e9")
define ls = Character("Lil Sis", what_color="#f39af9", who_color="#f3f0e9")
define m = Character("Ms. Mage", what_color="#8a8aec", who_color="#f3f0e9")
define v = Character("Vivian", what_color="#8a8aec", who_color="#f3f0e9")
define w = Character("Woman", what_color="#f5e59d", who_color="#f3f0e9")


label start:

    $ narcissus = 0

    $ together = False

    $ healthy = False

    $ reishi = False

    play music "audio/01_rideout.mp3" fadein 2.0

    scene shop with fade

    "One awfully awful evening..."
    "A sad young man sits his sorry ass down in a mysterious shop."
    "He is our hero, Thiu."
    "And out of Thiu's mouth comes this asinine plea:"

    show w awkward_smile at righty with dissolve
    t "Can you take my pain away, Ms. Mage?"
    show v down at lefty, faceright with dissolve
    m "What do you mean?"
    show w sad
    t "I'm just so tired..."
    show v ohyeah
    m "Try sleeping."
    show w annoyed
    t "No, not like that..!"
    show w doubt
    t "I really am at the end of my wits here..."
    show w explain
    t "My happiest thought this month was \n \"Thank god everyone dies eventually\"!"
    show v heh
    m "Nice! That's my happiest thought too!"
    show w confused
    t "...Huh?"
    show v smirk
    m "Anyway, the only magic potion you need is tequila!"
    show w doubt
    t "W-what?"
    show v smile
    m "Sorrows begone! Guaranteed!"
    show w annoyed
    t "Please Ms. Mage!!"
    show w explain_angry
    t "I don't want to be an alcoholic! I just want to be me again."
    show w sad
    t "Or the me I was before I became this miserable shell of a man..."
    show v sigh
    m "Sorry friend. I can't help you."
    show v down
    m "Mind spells are prohibited."
    show v ohyeah
    m "But I know a therapist who--"
    show w explain
    t "Ahh, forget it."
    show w lookaway
    t "Wasn't there another mage around here?"
    show w surprise
    show v ukidding
    play sound "audio/echo.mp3"
    m "No, wait!!" with hpunch
    show w defa
    show v impatient
    m "You don't want to get involved with him!"
    show v think
    m "That guy has no morals or care for anyone's well-being!"
    show w nervous
    t "Oh??"
    show v pissed
    m "Trust me! He is called The Jerkface!"
    show v unsure
    m "..By me."
    show v ohyeah
    m "And it's never ended well for anyone who asked for his help."
    show v impatient
    m "...Besides he still owes me like a hundred bucks."
    show w doubt
    t "........."
    show v unimpressed
    m "Anyway, he'll just screw you over."
    show v heh
    m "But try the pharmacist though. \n She sells coke under the table."
    show w awkward_smile
    t "O-... kaaay. Thank you."
    show w lookaway
    t "I should get going..."
    show v ukidding
    m "Seriously! Don't involve yourself with that douchebag."
    show w awkward_laugh
    t "Okay, thank you! Goodbye!!"
    play sound "audio/enter_shop.mp3"
    show w at faceright
    hide w with moveoutright

    scene city_late with fade

    "Daft as he is, Thiu figures drugs won't make his depression any better."
    "Except serotonin, which he takes everyday along with some quetiapine..."
    "But I digress. The point is that Thiu is looking for an instant and permanent cure."

    show w defa at lefty, faceright with dissolve
    t "(Where is this \"Jerkface\"?)"
    show w doubt
    t "(I heard he doesn't have a shop, he just makes spells at home...)"
    hide w with dissolve

    menu:

        "Try downtown.":

            "So Thiu wanders downtown."
            "He has no idea what exactly he is supposed to be looking for."
            "A big neon sign that reads \"ILLEGAL SPELLS HERE!!\" would be nice."
            "But alas, no such luck."
            show w annoyed at lefty, faceright with dissolve
            t "(What did I think was going to happen?)"
            show w miffed
            t "(I'll never find the guy like this.)"
            show w doubt
            t "(Screw this. I'm such a moron.)"
            show w sad
            t "(I'm just gonna buy myself some soda and go home...)"
            hide w with dissolve
            "Thiu would stuff quarters into the vending machine, but a sticker is blocking the coin slot."
            show w explain_angry at lefty, faceright with dissolve
            t "(Argh! Can't I even have this!?)"
            hide w with dissolve
            "The sticker reads: \"MY AWESOME SPELLS. YOUR SORRY LIFE. {b}JUST ASK.{/b}\""
            "It also has an address written on it with such tiny, tiny letters."
            show w confused at lefty, faceright with dissolve
            t "..........."
            show w sad
            t "(Whatever... I'll check it out...)"
            show w explain
            t "(If I get mugged or killed then that's what the universe wants.)"
            show w annoyed
            t "(Who cares. I'm worthless anyway.)"
            hide w with dissolve

        "Ask around.":

            show w awkward_smile at lefty, faceright with dissolve
            t "(Maybe I could ask around...)"
            show w defa
            t "(I'm sure someone knows where he lives.)"
            t "......"
            play sound "audio/_nervousbubbles.mp3"
            show w awkward_laugh
            t "(Hahahah, yeah right!)" with hpunch
            show w explain_angry
            t "(As if I'd have the guts to ask help from a stranger!)"
            show w miffed
            t "(I battled with myself for weeks before I gathered up the guts to visit Ms. Mage!)"
            show w nervous
            t "(I planned all the things I would say in advance and everything.)"
            show w annoyed
            t "(And even then I managed to make a complete ass out of myself.)"
            show w doubt
            t "(And I bet she's sitting there in her little shop right now thinking about what a loser I am.)"
            show w awkward_laugh
            t "(I can never go back again.)"
            show w sad
            t ".....{i}Sigh.{/i}"
            show w miffed
            t "(I'm just gonna wander around aimlessly.)"
            show w explain
            t "(I'll find the guy's place if it's meant to be.)"
            show w lookaway
            t "(And if not then my dumbass can crawl back home and cry myself to sleep like the useless worm that I am.)"
            hide w with dissolve

    stop music fadeout 2.0
    play music "audio/04_cantelope.mp3" fadein 2.0

    scene kitchen_late with fade
    "While Thiu is busy berating himself, another man is drinking coffee at home."
    "Or he would be drinking it, if it didn't taste like death."
    show l ugh at lefty, faceright with dissolve
    j "Ugh!! Where'd you get \n these coffee grounds from?"
    show a laugh at righty with dissolve
    ls "Our bio waste!"
    show l angry_explain
    j "{i}What!?{/i} Then what happened \n to the money I gave you?"
    show a playing
    ls "Dude. Check this out!"

    hide a
    hide l
    with dissolve

    "The little lady pulls a bouncy ball out of her pocket."

    show a grin_bouncy at righty
    show l oh at lefty, faceright
    with dissolve
    play sound "audio/boing.mp3"
    ls "Isn't this the coolest thing ever!?"
    j "..............................."
    play sound "audio/ding.mp3"
    show l happy at faceleft
    j "Oh. A guest?"
    show l bouncy
    show a rage
    play sound "audio/_impact.mp3"
    ls "{b}Look at it!!{/b}"

    scene city_late with fade
    play sound "audio/opendoor.mp3"

    show w defa at lefty, faceright
    show l smilesmile at righty
    with dissolve
    j "Well helloooo hello."
    show l smile
    j "How can I help you?"
    show a smile_bounce at right with moveinright
    ls "Who is it?"
    show l ugh at faceright
    show w confused
    j "Piss off Tal."
    show a angry_bounce
    a "Fine, I don't care anyway!"
    show a bored_bounce
    a "I was asking just to be nice..."
    show w lookaway
    show l angry_explain
    play sound "audio/_metal.mp3"
    j "I told you to get lost!" with hpunch
    show a angry_bounce at faceright
    hide a with moveoutright
    a "Screw you!"
    show l think_pleased at faceleft
    j "A-hem."
    show l sheepish
    j "Let's try this again."
    show w awkward_laugh
    t "...Aha...ha........."
    show l smile
    j "How can I help you my friend?"
    show w awkward_smile
    t "H-hi! Uhhh...."
    show w defa
    t "M-my name is Thiu..."
    show l miffed
    j "Dumbest name I've ever heard..."
    show w sad
    t "...Are you perhaps The Jerkface?"
    show l think_pleased
    j "............A certain someone calls me that, yes."
    show l oh
    l "But you should call me Lua."
    show w defa
    show l happy
    stop music fadeout 2.0
    l "Come on in, you're just in time for some coffee!"

    play music "audio/02_outof.mp3" fadein 2.0
    scene kitchen_late with fade
    show l smilesmile at righty with dissolve
    l "Here, have some."
    show w awkward_laugh at lefty, faceright with dissolve
    t "Oh! Thank you..!"
    hide w
    hide l
    with dissolve
    "He says, while in reality the last thing he wants is coffee."
    "It's already past nine, and Thiu has a hard enough time getting to sleep as it is."
    "But social awkwardness dictates he accept it anyway, or risk offending the man who called his name dumb."
    "Yeah, we can't have that."
    show w defa at lefty, faceright
    show l chuckle at righty
    with dissolve
    l "And what brings you here Thiu?"
    show l playful
    l "Surely you know I'm a big bad miracle maker who ruins people's lives for a living?"
    show l sheepish
    l "Or so I've heard myself described."
    show l fake_laugh
    l "Jealousy is such an ugly thing, isn't it?"
    show l chuckle
    l "I'm really a {i}really{/i} nice man y'know? Really."
    show w awkward_laugh at lefty, faceright
    t "Um... well..."
    show w sad
    t "I was hoping you'd have a spell for me."
    hide w
    hide l
    with dissolve
    "Thiu feels like his request is dumb and embarrassing. Which it is."
    "So he figures this is a great moment to sip down the whole coffee in one gulp to postpone speaking."
    play sound "audio/isbad.mp3"
    show w urb at lefty, faceright with vpunch
    "Big mistake."
    "The foulest coffee Thiu has ever tasted washes over his taste buds."
    show l lol at righty with dissolve
    l "Ehee, you like it??"
    t "(Don't spit, don't spit, that's rude, don't spit, don't-...)"
    show l smilesmile
    l "It's my sister's special blend!"
    hide w
    hide l
    with dissolve
    "Thiu uses sheer willpower to swallow the damn thing down."
    "There is no way in hell Lua didn't notice how much he hated every drop."
    show w awkward_laugh at lefty, faceright
    show l smilesmile at righty
    with dissolve
    t "I-it's got character......."
    show l chuckle
    l "Aww, glad you like it."
    show l happy
    l "Here, want another cup?"
    show w awkward_smile
    t "(Absolutely not!! Tell him nicely!! Say something like... like-...)"

    menu:

        "No thank you.":

            show w doubt
            show l smilesmile
            t "(...But that sounds so harsh. Is it too harsh??)"
            show w lookaway
            t "(I bet it's too harsh.)"
            show w confused
            t "(Ahh, I'm taking too long!! Say something now!!!)"
            show w awkward_laugh
            play sound "audio/_nervousbubbles.mp3"
            t "Y-yes, please! Another cup would be nice." with vpunch

        "I'm good, thanks.":

            show w defa
            show l smilesmile
            t "(No wait. That almost sounds like yes.)"
            show w doubt
            t "(What if he misunderstands it as a yes??)"
            show w lookaway
            t "(Maybe if I switch it to \"No thanks, I'm good\"?)"
            show l smile
            l "Well?"
            show w awkward_smile
            t "Huh? What??"
            show w awkward_laugh
            t "O-oh, right! I'd love another cup!"

    show l lol
    l "Why, I'm so glad to hear it! Hahahah!!"
    show w doubt
    t "(God, why am I like this??)"
    hide w
    hide l
    with dissolve
    "Thiu can do nothing but curse his life, as Lua refills his cup."
    "Coming here was a bad idea..."
    show w defa at lefty, faceright
    show l smile at righty
    with dissolve
    l "So what kind of spell were you looking for?"
    show w sad
    t "Well umm..."
    show w lookaway
    t "I'm about thiiiiiis close to killing myself..."
    show l think_pleased
    l "Hmm, I see! So you need some help with that?"
    show l lol
    l "I suggest a rope. It's a classic!"
    show w confused
    play sound "audio/echodull.mp3"
    t "N-no!" with hpunch
    show l smug
    l "No? Well if you wanna get fancy we can--"
    show w explain_angry
    play sound "audio/echolong.mp3"
    t "{b}NO!{/b} I want to get rid of those feelings, not myself!" with vpunch
    show w annoyed
    t "The hopelessness and such..."
    show l bored
    l "Ugh. Boring."
    show l oh
    l "But sure. I might have something."
    hide w
    hide l
    with dissolve

    "The really nice man excuses himself to go looking for a book."
    "Thiu takes this chance to pour his coffee into the nearest potted plant."
    "Lua returns flipping through a big, weathered down book."
    "...It's got coffee stains all over it."

    show w defa at lefty, faceright
    show l playful at righty
    with dissolve
    l "Now before we proceed, there's the issue of your payment..."
    show w awkward_laugh
    t "It's not my soul or something right? Hahha...."
    show l complain
    l "The hell would I do with that?"
    show l miffed
    l "It's cash or credit."
    show w nervous
    t "Oh... How much?"
    show l smilesmile
    l "Ah! Here's something!"
    hide w
    hide l
    with dissolve

    "Lua slams the tome onto the table."
    play sound "audio/book.wav"
    show book:
        xalign 0.5 yalign 0.2,
    with dissolve
    l "A splitting spell!"
    l "It divides your existence in two."
    l "You could put all the negatives in one half, and keep the good stuff."
    hide book
    show w defa at lefty, faceright
    show l smilesmile at righty
    with dissolve
    t "Oh?"
    show l mock
    l "It does come with the {i}minor inconvenience{/i} of cutting your life force in half too."
    show l smug
    l "But hey! Weren't you gonna kick the bucket anyway?"
    show w sad
    t "........."
    show l smilesmile
    l "Well? Sound good?"

    "Thiu recalls the words of Ms. Mage."
    hide w
    hide l
    show v fady at lefty, faceright
    with dissolve
    m "\"It's never ended well for anyone who asked for his help.\""
    hide v
    show w doubt at lefty, faceright
    show l smilesmile at righty
    with dissolve
    t "........................."
    show w explain
    t "....Fuck it. Why not."
    show l smile
    l "Wonderful!"
    show l lol
    stop music fadeout 2.0
    l "By the way your soul's mine now."
    show w confused
    play sound "audio/surprise.wav"
    t "H-HUH!?" with vpunch
    play music "audio/commercialbliss.ogg" fadein 2.0
    hide w
    hide l
    with dissolve

    "And just like that, a spell wraps around Thiu's body, lifting him up in the air!"
    "He struggles to get loose, but only manages to turn himself upside down."
    "So now not only is he floating in mid-air, but blood begins rushing to his head."
    "Great."
    t "Wait wait wait wait!!" with hpunch
    l "What?"
    t "I-I thought it's cash or credit?"
    l "I don't know. I changed my mind."
    l "Plus you look kinda poor so I figured you'd be thankful."
    t "No, wait! I can take a quick loan or something-!!"
    l "Shut up and let's get this over with."

    "And with that, Lua yanks the floating loser by the hair."
    "And pulls him in for a kiss!"
    "It'd be {i}sooo romantic{/i} if it weren't for the fact that it wasn't romantic at all."
    "Thiu's soul gets pulled out of his body via his mouth like a long chewy marshmallow."
    "And just as he figures he's going to choke on it, he passes out."
    "But he didn't pass out from lack of oxygen, it's just that his soul had left his body."
    "And with no brain for it to think with, it simply stopped doing that."
    "Lua chops the soul in half, and out pours all kinds of crap."
    "And by crap I mean Thiu's feelings and thoughts materialized as weird magical stuff."
    "Luckily Lua is an expert in weird magical stuff, and he shoves the happy things in one half."
    "And all the gross, sad things into the other."
    "Then he sews both halves shut, creating two smaller marshmallowy souls!"
    "The larger one quickly turns dark and murky and moldy."
    "While the tiny one looks like it might actually be tasty."
    "Lua shoves both souls right back into Thiu's mouth."
    "And that's when the pain starts."
    "Ohhh boy, does the pain start."
    "With two emerging consciousness arguing over who gets to inhibit this lousy excuse of a body..."
    "....Thiu feels torn in half."
    "Did I say feels? I mean he was actually, physically being torn in half."
    "All the while his organs attempt to grow larger to accommodate two souls."
    "Extra fingers start pushing out of his hand while a brand new skull emerges out of Thiu's left eye."
    "While all this is happening, a little lady walks into the kitchen."

    show a listening at righty with moveinright
    a "What's all this noise?"
    show l sheepish at lefty, faceright with dissolve
    l "Oh, hey Tal. I'm splitting this guy in two."
    show l smile
    l "Wanna watch?"
    show a ohshit
    a "It... doesn't look right. Have you done this before?"
    show l playful
    l "Nope. First time."
    show a think
    a "Oh my god..."
    show a miffed
    a "Who's gonna clean this up?"
    show l oh
    l "I believe it's your turn."
    hide a
    hide l
    with dissolve
    play sound "audio/split.mp3"
    "Before they can start arguing over it, a sickening noise fills the room."

    "And Thiu successfully splits himself in two."
    "Both existences hit the floor unconscious."

    show a ohshit at righty
    show l happy at lefty
    with dissolve
    play sound "audio/special.wav"
    l "Aha!! It's done!" with vpunch
    show l playful
    l "I'm such a genius!"
    show l think_pleased at faceright
    l "Tal, go buy some premium coffee."
    show l smile
    l "I want to celebrate!"
    show a angry
    a "Why do I always have to!? There's barely any stores even open at this hour!"
    show l angry_explain
    l "Listen, you little princess! You can either go buy me coffee or clean up my spell!"
    show a think
    a "Ughhh, {i}fine.{/i}"
    hide a
    hide l
    with dissolve
    stop music fadeout 2.0
    "Lua hands Tal some money, and she proceeds to go buy another bouncy ball."
    play music "audio/05_iwill.mp3" fadein 2.0
    scene black with fade

    "The next time Thiu opens his eyes, he feels like he's been hit with a truck."
    scene kitchen_day with fade
    "The sun is already high up in the sky. So it must be mid-day."
    "Not that he cares. He has never felt this awful in his entire life."
    show s hurt at lefty, faceright with dissolve
    s "Ughh... Where am I?"
    show a laugh_bounce at righty with dissolve
    a "Heeeey!! You're awake!"
    show s surprise
    play sound "audio/echo.mp3"
    s "AH!! Who're you!?" with vpunch
    show a smug
    a "You slept around the clock, haha!"
    show s bitetongue
    s "....That's... not what I asked."
    show s ohwell
    show a playing at faceright
    a "Hey Lua!! He woke up!!"
    hide a with moveoutright
    show s yeahright
    s "(Ugh. That's right. I bought a spell from The Jerkface...)"
    show l smilesmile at righty with moveinright
    l "Well hello there!"
    show s listen
    s "(Yeah, that Jerkface right there...)"
    show s scold
    s "(I can't believe he just left me on the floor!!)"
    show s sad
    s "(How long was I out?? The girl said round the clock so, uhh..?)"
    show l chuckle
    l "How are you feeling?"
    show s fuckyou
    play sound "audio/echowhip.wav"
    s "Like shit!" with vpunch
    show s thefuck
    s "I feel worse than ever!"
    show s explain
    s "Your spell didn't do crap!!"
    show s scold
    show l fake_laugh
    l "Wrong."
    show l think_pleased
    l "My spell was perfect!"
    show l mock
    l "It's just that you're the miserable half."
    show s confused
    s "Wh--... huh??"
    show l smug
    l "I told you, didn't I?"
    show l playful
    l "I split your existence. And dumped all the negativity in one half."
    show l mock
    play sound "audio/special.wav"
    l "{b}CONGRATULATIONS!!{/b} You're that half." with vpunch
    show s nervous_smile
    s ".....................You're kidding, right?"

    "But Lua was not kidding."

    show l smilesmile
    l "Come! Let's go meet the lucky one!"
    show l chuckle
    l "He's an early bird, unlike you."

    scene black with fade

    "Thiu follows Lua to another room, miserable and terrified."
    "He's not so sure he wants to meet the other half."
    "He considers walking out and pretending none of this ever happened."
    "But then..."
    play sound "audio/Special (8).wav"
    h "Hahahahah!!"
    "A warm laughter echoes from the other room."
    "Thiu peeks to see who it is."

    scene entry
    show h laugh at righty
    show a approve at lefty, faceright
    with fade
    h "Why is your drawing so much better than mine, hahha!"
    show a playing
    a "Because I CHEATED!! My eyes weren't actually closed!"
    show a smug
    play sound "audio/_laugh.mp3"
    a "HAHAHAHAHAH!!" with hpunch
    show h lol
    play sound "audio/_nervousbubbles.mp3"
    h "Gasp! Such nerve! HAHAH!!" with vpunch
    hide a
    hide h
    with moveoutright
    show s down at center, faceright
    show l pleased at left, faceright
    with moveinleft
    s "................................."
    show l lol
    l "Aww. Look how happy you are!"
    show l mock
    l "Worth it, wasn't it?"
    show s surprise
    show l pleased
    show h smile at right with moveinright
    h "Ah! It's me!"
    show s docile
    show h lol
    h "Wow! That's super weird!"
    show h laugh
    h "It's like a 3D mirror!"
    show h shruglaugh
    h "No. What am saying? Hahah!"
    show h kindasmile
    h "Aren't mirrors 3D too?"
    show h confused
    h "No wait... I mean they {i}are{/i} flat surfaces... So, uhh..?"
    show s sad
    s "I want this spell undone."
    show h surprised
    h "...Huh?"
    show l fake_laugh
    l "Now now. You agreed to this."
    show h nervous
    h "Y-yeah yeah!"
    show h smile
    show l think_pleased
    l "Besides, I haven't decided what to do with you yet."
    show l playful
    l "Since I own your life...s."
    show s scold at faceleft
    s "Lives? I thought it was my soul."
    show l smilesmile
    l "It's lives now."
    show s whatever
    s "The details of our deal just keep on changing, huh?"
    show l mock
    l "Indeed! Oh, if only you had it in writing, my friend!"
    show l lol
    l "You're learning so much today, hahaha!!"
    show l bored
    l "Tal, stop drawing on the walls and come help me with lunch."
    show a listening at right with moveinright
    a "'kaaaaay."
    show l at faceleft
    hide l
    hide a
    with moveoutleft
    show s think at lefty, faceright
    show h at righty
    with moveinright
    s "{i}Sighh...{/i}"
    show h smilecalm
    h "........"
    show s down
    s "........."
    show h explain
    h "So about--"
    show s sad
    s "About--"
    show h laugh
    h "Hahah! Jinx!"
    show s ticked
    s "(Oh my god. He's annoying.)"
    show s embarrassed
    s "(God. I hate myself. No wonder I have no friends. Look at this moron.)"
    show h smilegentle
    h "What were you saying? You go first."
    show h kindasmile
    h "Actually, no. Let me guess!"
    show h smug
    h "You wanted to ask about the deal I made!"
    show s sorry
    s "Yeah."
    show h laugh
    h "Hehe, I knew it. Of course I'd know."
    show h smile
    h "I was going to ask you the same."
    show h confused
    h "But I bet you--... No. I bet {i}I{/i} knew that already?"
    show h lol
    h "Haha!! Isn't that a bizarre sentence?"

    menu:

        "Tell yourself to shut up.":

            show s ticked
            s "...Shut the fuck up."
            show h explain
            h "Wow, excuse me."
            show h kindasmile
            h "And by me I mean you."
            show h lol
            play sound "audio/_laugh.mp3"
            h "HAHAHAHAHAH!!!" with hpunch
            show s explain
            s "Christ... It's been less than five minutes and I've already had it with you!"
            show h shruglaugh
            h "Well I've had had it with myself years ago so tell me something I don't know."
            show s think
            s "Ugh..."
            show s sorry
            s "Just..."

        "Agree with yourself.":

            $ narcissus += 1

            show s nervous_smile
            s "Yeah... It's, uhhh.... Yeah."
            show h smile
            h "...Yeah."
            show h smileguilty
            h "Anyway, I can't decide how to relate to you."
            show h confused
            h "As in should I keep calling you me. Or you."
            show s shrug
            s "You seem to be using \"you\", so I guess that's that."
            show h laugh
            h "You're using \"you\" too."
            show s ohwell
            s "Yup..."
            show h smile
            h "Yuuuup yup...."
            show h smileaway
            h "......"
            show s down
            s "....................."
            show h nervous
            h ".........................................."
            show s bitetongue
            s "(Great. I'm so socially awkward I can't even keep up a conversation with myself!!)"
            show h shruglaugh
            h "Hahah, looks like I didn't gain any social skills despite losing the anxiety!"
            show s confused
            s "Oh..."
            show s nervous_smile
            s "So then.. uh...."

    show s sad
    s "How is it? ...Being happy."
    show h explain
    h "It's pretty great!"
    show h smilecalm
    h "I still remember all the bad things, but they feel so long ago."
    show h laugh
    h "I had forgotten that breathing could be so easy!"
    show h smileaway
    h "I don't know how else to describe it. I just feel... hmm... well, happy."
    show h smilegentle
    show s disapprove
    s "...Yeah? Well I feel like my chest is a black hole."
    show s sorry
    s "And the only thing keeping me from collapsing into myself..."
    show s hurt
    s "Is the barbed wire tearing me apart."
    h "................."
    show h nah
    h "(Jeeeesuuuus. Could I be more melodramatic?)"
    show h smileguilty
    h "Um, so hey..."
    show h shruglaugh
    h "Maybe we shouldn't talk?"
    show h nervous
    h "You're kinda bumming me out."
    show s confused
    play sound "audio/surprise.wav"
    s "HUH!?" with hpunch
    show s thefuck
    s "What the hell!?"
    play sound "audio/_hiss2.ogg"
    s "You're blowing me off!?" with vpunch
    show s fuckyou
    s "Aren't you the one person supposed to care for me!?"
    show h kindasmile
    h "Well I mean you {i}say{/i} that..."
    show h mock
    h "But when did I ever care for myself?"
    show s listen
    s ".....(Okay he got me there.)"
    show h laugh
    h "But hey! Look at the bright side!"
    show h shruglaugh
    h "I can finally reach to suck myself!"
    show s thefuck
    s ".....................!?"
    show h smilegentle
    h "Hm? Not interested? Or maybe later?"
    show s angry at faceleft
    s "I'm out of here!"
    show h smile
    h "But we didn't pay yet?"
    show s explain at faceright
    s "You take care of that!"
    show s at faceleft
    hide s with moveoutleft
    stop music fadeout 2.0
    s "Since you're the only beneficiary here!!"

    play music "audio/04_cantelope.mp3" fadein 2.0
    scene city_day with fade

    play sound "audio/_impact.mp3"
    show s thefuck at center with hpunch
    s "(This is some bullshit!!)"
    show s scold
    s "(Why did I have to get the negative stuff!?)"
    show s thefuck
    s "(And I'm supposed to pay for this!?)"
    show s think
    s "(This is so---)"
    hide s with dissolve
    "While digging though his pockets, a terrifying realization hits Thiu."
    show s surprise at center with dissolve
    s "(W-where are my keys!?)"
    show s confused
    s "(And my phone?)"
    show s thefuck
    play sound "audio/_metal.mp3"
    s "(AND MY WALLET!?)" with vpunch
    show s shrug
    s "(.....Come to think of it... What on earth am I wearing?)"
    show s think
    s "(Looks like something Jerkface would wear...)"
    show s whatever
    s "(Great. How do I get home now?)"
    show s ticked
    s "(Because I'm NOT going back to the other me.)"
    show s down
    s ".....{i}Sigh.{/i}"
    show s worry
    s "(I don't have any friends that I could go to...)"
    s "(Nor do I have any relatives around here.)"
    show s yeahok
    s "(Not that I would go for them either...)"
    show s yeahright
    s "(They're just a bunch of strangers with the same last name.)"
    show s scold
    s "(Arrrghh... I can't just stand here for god knows how long!)"
    show s sad
    s "(People are staring....)"
    show s surprise
    play sound "audio/_increase.mp3"
    s "(Oh god, {i}PEOPLE ARE STARING!{/i})" with hpunch
    show s hurt
    s "(I look stupid!!)"
    show s desperate
    play sound "audio/_nervousbubbles.mp3"
    s "(I bet everyone in the world is going to take notice of me standing here and think I'm stupid!!)" with hpunch
    show s docile at faceright
    s "(Aaaah, I need to go somewhere!!)"
    show s confused at faceleft
    s "(But I don't have any money so I can't even go to a store.)"
    show s whatever
    s "(Because god forbid I exit one without buying anything!)"
    show s think
    s "(Well... I guess I left Ms. Mage's shop without buying anything...)"
    stop music fadeout 2.0
    show s hurt
    s ".............."

    play music "audio/12_looking.mp3" fadein 2.0
    scene shop with fade

    play sound "audio/enter_shop.mp3"
    show v smile at lefty, faceright  with dissolve
    m "Welco-... Oh!"
    show s down at righty with moveinright
    show v down
    m "It's you again..."
    show s nervous_smile
    s "H-hi..!"
    show v ohyeah
    m "What brings you here this time?"
    show s ashamed
    s "Well... um...."
    hide s
    hide v
    with dissolve

    "Thiu explains what happened."

    show v ukidding at lefty, faceright  with dissolve
    m "...........................So."
    show v unimpressed
    m "You did exactly what I told you not to do."
    show v impatient
    m "And it went exactly like I said it would."
    show s down at righty with dissolve
    s "Mm-hmm..."
    show s ashamed
    s "Look, I just wanna call my landlord so she'll let me in my apartment."
    show s embarrassed
    s "And after the call I'm probably gonna have a panic attack, so I'm sorry in advance."
    show v think
    m "Help yourself I guess."
    hide s
    hide v
    with dissolve
    "Ms. Mage points Thiu to the phone."
    "It's a rotary dial one."
    show s embarrassed at righty
    show v smile at lefty, faceright
    with dissolve
    s ".........(Is she messing with me??)"
    show v smile_closed
    m "Go ahead."
    show s sad
    s "Umm...."
    show s shrug
    s ".......Isn't this a movie prop?"
    show v down
    m "Huh???"
    show s think
    s "How do you use this?"
    show v unimpressed
    m "{i}Sigh...{/i} I'll do it. What's the number?"
    show s docile
    s "I don't know. It's on my phone."
    show v ukidding
    m "......................................"
    show s ashamed
    s "............."

    hide s
    hide v
    with dissolve
    "At that point Ms. Mage is done helping Thiu, and goes back to stocking the shelves."
    "Good luck charms and dream catchers are both 10\% off."

    show v sigh at lefty, faceright  with dissolve
    m "Looks like you'll just have to wait."
    show v gentle
    m "I'm sure your other self goes home eventually."
    show s sad at righty with dissolve
    s "Well... Since I'm here..."
    show s makenice
    s "Can you help me undo this spell?"
    show s nervous_smile_away
    s "I'll pay you once I get my wallet back."
    show v unsure
    m "Sorry. I don't know anything about banned magic."
    show v worry
    m "You need to ask The Jerkface."
    show s sad
    s "He already said no."
    show s tocry
    s "I don't know what else to do..."
    show v ohyeah
    m "U-huh. Tough."
    show s disapprove
    s "A little compassion please? My life just turned upside down!"
    show v ukidding
    m "I'm working. Who are you anyway?"
    show s nervous_smile
    s "Oh! ...Haha... er...."

    hide s
    hide v
    with dissolve

    "\"I'm so sorry for bothering you. Thank you for your time and goodbye.\""
    "That's what Thiu wanted to say, but was too thrown off to form the sentence."

    show s ashamed at righty with dissolve
    s "I-... I'm-... M-my name is Thiu..."

    "Nailed it. Had a nice voice crack and everything."

    show v gentle at lefty, faceright  with dissolve
    v "Alright, Thiu. My name is Vivian."
    show v ohyeah
    v "And here's what I think..."
    show v impatient
    v "As far as Lua goes, you got off easy."
    show v unimpressed
    v "I'd count my blessings and attempt to make the best of what you have left."
    show s docile
    s ".............B-but..."
    show s hurt
    s "But it's not-!! It's--!! It's unfair! I just--!"
    show s bigsad
    play sound "audio/_impact.mp3"
    s "Sniff! {i}WHY!?{/i}" with hpunch
    show s desperate
    s "I just wanted to be happy!"

    hide s
    hide v
    with dissolve
    "Thiu continues embarrassing himself by starting to cry in public."
    "Vivian pours him some tea."
    "She seems awfully used to this kind of thing."
    "Perhaps her shop attracts mostly broken people?"
    "You'd have to be pretty desperate to rely on a mage after all."
    show v gentle at lefty, faceright with dissolve
    v "Here, have a drink."
    show s stopcrying at righty with dissolve
    s "Sniff. Thanks..."
    show v smile_closed
    v "Feel free to come talk to me whenever."
    show s confused
    s "...Really? But why?"
    show v unsure
    v "Well, you don't have to... It's just-..."
    show s docile
    s "(Wait, could this mean...??)"
    show s makenice
    s "(After all this time, have I made a friend..?)"
    show v smirk
    v "It's just that I've never seen this spell in person!"
    show s confused
    s ".............Huh?"
    show v heh
    v "It's so fascinating!! I'd love to hear all about it!"
    show s down
    s "Oh..... Yeah... Sure."
    show s yeahok
    stop music fadeout 2.0
    s "(Never mind...)"

    play music "audio/09_doit.mp3" fadein 2.0
    scene kitchen_day with fade

    "Meanwhile, the other Thiu is still loitering around at Lua's place."
    show l pleased at lefty, faceright with dissolve
    l "Care to join us for lunch?"
    show h laugh at righty with dissolve
    h "Really? Can I?"
    show l smilesmile
    l "Yes. Free of charge!"
    show l down
    l "Huh... There's just one of you? Where's the other one?"
    show h mock
    h "Speeeeeeaking of payments, how can I repay you?"
    show l sheepish
    l "....Like I said, I'm undecided."
    hide h
    hide l
    with dissolve
    "In front of Thiu is a bowl of soup."
    "And in the soup floats mysterious bits and pieces."
    "He recognizes the carrots and potatoes. Everything else is a mystery..."
    show h confused at righty
    show l pleased at lefty, faceright
    with dissolve
    h "(What on earth am I eating?)"
    show l happy
    l "Let's just say I'll let you know when I need a favor."
    show l down
    l "But that aside, where's the other Thiu?"
    show h nah
    h "I'd like to get this payment stuff settled now though..."
    show l ugh
    l "And {b}I'd{/b} like to know where the other you went."
    show h shruglaugh
    h "Oh!! Oh, sorry! The other me--"
    hide h
    hide l
    with dissolve
    "Thiu's eyes catch a curious sight."
    "On top of the spice shelf, sits a human skull."
    show h confused at righty with dissolve
    h "Wait... Is that real?"
    "He would not put it past Lua at this point..."
    show l miffed at lefty, faceright with dissolve
    l "I don't know Thiu. Is anything real?"
    show l complain
    l "Can we please keep on the subject?"
    show l ugh
    l "Where the hell did you put the other you?"
    show h smile
    h "Huh? Nowhere?? He went home already."
    show l angry_explain
    l "You just let him walk off?"
    show h surprised
    h "I-... was I not supposed to?"
    show l oh
    l "God. I must've given all your intelligence to the sad one..."
    show h angry
    play sound "audio/_hiss1.ogg"
    h "Hey!!" with vpunch
    show l whatever
    l "As I recall, you wanted to get rid of your negative feelings."
    show l down
    l "Not let them run around town by themselves."
    show l playful
    l "That is to say, the job is still half done."
    show h unsure
    h "Oh......."
    show l chuckle
    l "Bring him back here and I'll help you dispose of the body. With no extra cost!"
    show h nervous
    h "I don't... think that's necessary."
    show l down
    l "Are you sure?"
    show l oh
    l "I've split it, but you still have the same soul."
    show l whatever
    l "There's no guarantee he won't pull you back under with him."
    show h unsure
    h "...I--"
    hide h
    hide l
    with dissolve

    "Something hits the back of Thiu's head." with hpunch
    "And then it continues bouncing off the table and walls, as if it's mission is to wreck as much havoc as possible."
    "It takes a moment for Thiu to understand it's a bouncy ball."

    show a laugh_bounce at righty with dissolve
    a "HAHA!! Sorry!"
    show a playing
    a "That's my bouncy ball! Like it?"
    show l angry_explain at lefty, faceright with dissolve
    l "Goddamit Tal! I thought I threw that thing in the trash already!"
    show a grin_bouncy
    a "Hehee!! It's a new one!"
    hide l
    hide a
    with dissolve
    h "I should get going..."

    scene entry with fade

    show h nah at lefty with dissolve
    h "Hmmm..."
    show l pleased at righty with moveinright
    l "Something a miss?"
    show h laugh at faceright
    h "Looks like other me took our shoes."
    show l smile
    l "You can borrow mine."
    hide h
    hide l
    with dissolve
    "Lua opens a closet. It is full of mismatched shoes."
    show h smilelow at lefty, faceright
    show l smile at righty
    with dissolve
    h "......."
    show l oh
    l "....What?"
    show h laugh
    h "Do you have a single matching pair?"
    show l miffed
    l "Ah. That."
    show l mock
    l "A certain someone cursed me to lose my other shoe until I pay her 100 bucks."
    show l fake_laugh
    l "Cute, right?"
    show h whatever
    h "Oh yeah... Gradual foot damage is the epitome of cuteness..."
    show h shruglaugh
    h "Anyway, I'll drop by again!"
    show l chuckle
    l "I'm sure you will."
    show l smilesmile
    l "...And do think about what I said."
    show l smile
    l "The body disposal offer is part of our deal."
    show h unsure at faceleft
    stop music fadeout 2.0
    h ".........O-okay bye."
    hide h with moveoutleft

    play music "audio/13_where.mp3" fadein 2.0
    scene city_day with fade

    "Thiu walks home barefoot."
    "Small rocks keep stabbing the bottom of his feet."
    "His socks wear down quickly, and the ground is muddy and nasty."
    "Any other day this would've dampened his mood to the point of considering suicide."
    "But not today! Today is a mighty fine day and he just can't be bothered with the little things!"
    "Like shards of glass. Who cares!"
    "Damn, that deal with the devil was a great one!"

    "Once he reaches his apartment, a huge piece of trash is blocking the door."
    show h kindasmile at lefty, faceright with dissolve
    h "Oh-ho! What do we have here?"
    "It's the other Thiu."
    show s disapprove at righty with dissolve
    s "You have the keys."
    show h lol
    h "Oh, right! You've been locked out this whole time, hahahah!!"
    show s bitetongue
    s "I don't know what's so funny about that..."
    show h sorry
    h "Awww, I'm sorry. You left so suddenly I didn't even think to give you the keys."
    show h mock
    h "I mean since they're my keys. Obviously it makes sense I'd hold onto them, y'know?"
    show s sad
    s "Whatever. Just open the door..."

    scene home_dirty with fade

    play sound "audio/opendoor.mp3"
    "Happier Thiu unlocks the door."
    show h surprised at lefty, faceright with dissolve
    play sound "audio/_impact.mp3"
    h "WHOAHH!" with hpunch
    show h smug
    h "Man. I forgot what a garbage dump this place was!!"
    show h unamused
    h "That's it! We're cleaning this place up!"
    show h smile
    h "You take care of the dishes and I'll--"
    "Sadder Thiu goes straight to bed."
    show h smilelow
    h "Ah."
    show h laugh
    h "C'mon. There's two of us, it'll be a breeze!"
    s "No."
    show h shruglaugh
    h "C'mooooon. A neat house will improve your mood."
    s "Fuck off."
    show h smilelow
    stop music fadeout 2.0
    h "........."

    scene black with fade
    play music "audio/11_bitch.mp3" fadein 2.0
    "Thiu resolves to doing the dishes himself."

    scene home_dirty with fade
    show h unhappy at lefty with dissolve
    h "(Man... What's my problem?)"
    show h bleh
    h "(At least pretend to help...)"
    hide h with dissolve
    "He pours some dish soap and pulls up his sleeves."
    play sound "audio/book.wav"
    show cuts:
        xalign 0.5 yalign 0.3
    with dissolve
    h "......................."
    h "(Right... I do crap like this.)"
    hide cuts with dissolve
    "The words of a certain jerk resurface in Thiu's mind..."
    show l fady at righty with dissolve
    l "\"There's no guarantee he won't pull you back under with him.\""
    l "\"As I recall, you wanted to get rid of your negative feelings.\""
    hide l
    show h unsure at lefty
    with dissolve
    h "(Yeah, that was the whole point, wasn't it?)"
    hide h with dissolve
    "Thiu washes a knife."
    "It has gone unwashed for months..."
    "The dirt and the blade have formed an unholy union. Never to be separated again!"
    show h unamused at lefty with dissolve
    h "(God. Look at that useless hunk of shit moping around in bed.)"
    show h miffed at faceright
    h "(You're gonna lay there for days eating nothing but pizza and watching cartoons, aren't you?)"
    hide h with dissolve
    "Indeed, that was Thiu's plan, much to Thiu's dismay."
    "Thiu walks over to Thiu, and though Thiu hears Thiu coming, Thiu won't move."
    "This is getting confusing, isn't it??"
    "Well anyway, one Thiu stands next to the bed, while the other pretends to sleep."
    show h unsure at lefty, faceright with dissolve
    h "Hey, me?"
    s "............"
    show h bleh
    h "I was thinking that if you're not going to help me clean, you could at least kill yourself."
    show s thefuck at righty
    play sound "audio/_hiss2.ogg"
    s "Come again!?" with hpunch
    show h nah
    h "Well I mean, that was the plan, right?"
    show h unamused
    h "Getting rid of my negativity."
    show h bleh
    h "And if you're not even going to suck my dick, why should I keep you around?"
    show s scold
    s "Oh my god!"
    s "Are you threatening me right now!?"
    show h kindasmile
    h "I'm just saying we're kinda half-assing the deal."
    show s sad
    s "Just-.... I-?? What can I even say to that..?"
    show h sorry
    h "There was some reason why we're not pushing up daisies yet, right?"
    show s think
    s "Yeah, mom's gonna be sad."
    show s yeahright
    s "...Even though she only calls once a year...."
    show s ticked
    s "But still."
    show h smilecalm
    h "Yeah, but it's okay now."
    show h kindasmile
    h "Because even if you give up the ghost, I'm still here."
    show h shruglaugh
    h "She won't even notice you're gone!"
    show h smilegentle
    h "So how about it? Time to rest in peace?"
    show s confused
    s "Wh--- No??"
    show h unhappy
    h "No? What do you mean?"
    show s explain
    s "No! As in no way that's happening!"
    show h argue
    h "Argh. Now you're just contradicting yourself!"
    show h angry
    h "You want this!!"
    show s bitetongue
    s "No, I don't!! I want to {i}NOT{/i} want it!"
    show h argue
    h "So you {i}do{/i} want it!"
    show s scold
    play sound "audio/echodull.mp3"
    s "AAAARG!! {b}No!!{/b} And you know how it is!!" with vpunch
    show h fuckyou
    h "Don't raise your voice at me! The neighbors are gonna think I'm screaming here alone."
    show s doubleflip_angry
    play sound "audio/echowhip.wav"
    s "I {i}AM{/i} SCREAMING HERE ALONE!!" with hpunch
    show h angry
    stop music fadeout 2.0
    h "Oh, I'll fucking make you scream alright!"
    play music "audio/commercialbliss.ogg" fadein 2.0
    hide s
    hide h
    with dissolve
    "Thiu grabs that nasty, unwashable knife."
    "And attempts to ram it into the other Thiu."
    "This doesn't go quite as smoothly as he had hoped."
    play sound "audio/isbad.mp3"
    s "STOP!! STOP, GET OFF ME!!" with hpunch
    "Kicking and screaming ensues."
    stop music fadeout 2.0
    play sound "audio/knockfast.mp3"
    "The Thius are having a battle to the death, until someone knocks on the door."
    show h surprised at lefty
    show s embarrassed at righty
    with dissolve
    h ".............."
    s ".............."
    show h unhappy at faceright
    play music "audio/03_partisan.mp3" fadein 2.0
    h "...Go get it."
    show s confused
    s "Me!?"
    show h whatever
    h "Yeah, you, I'm bleeding!"
    show s whatever
    s "That's entirely your own fault, but okay..."
    show h unamused
    h "It's probably the lady from upstairs again..."
    hide s
    hide h
    with dissolve
    play sound "audio/opendoor.mp3"
    "The less wounded Thiu opens the door, and is greeted with the utmost wrath of the neighbor woman."
    show s nervous_smile at lefty, faceright with dissolve
    s "Uhhh.... Y-yeah?"
    w "Do you have any idea how loud you're being?"
    show s sad
    s "Sorry I was just-..."
    "Just getting killed, sorry about that ma'am."
    show s sorry
    s "Just... I mean I'll keep it down."
    w "Could you be any less considerate!?"
    w "I work night swifts, y'know?"
    w "How would you feel if I started making a ruckus in the middle of the night!?"
    show s yeahok
    s "I mean... The guy downstairs argues with his wife every night, so..."
    play sound "audio/split.mp3"
    w "What do I care!? Stop making so much noise or I'm going to file a noise complaint!" with hpunch
    show s bitetongue
    s "......Okay, sorry."
    w "I can't believe this even needs to be said!!"
    w "I'm a nurse! What will you do if I'm sleep deprived tonight and someone dies because of that??"
    w "How will you live with yourself then?"
    show s think
    s "(How to live with myself indeed...)"
    w "Do you have any idea how hard my job is?? The last thing I need is--"
    hide s with dissolve
    play sound "audio/doorclose.mp3"
    "While the sadder half is attempting to come up with something diplomatic to say, other half closes the door."
    show h miffed at righty
    show s surprise at lefty, faceright
    with dissolve
    s "......"
    h ".........."
    hide s
    hide h
    with dissolve
    "The silence that follows is so thick, that it could be cut with the dirty knife Thiu was trying to stab the other with."
    "Half of Thiu expects the woman to come kicking through the door."
    "Other half expects her to leave to get that sleep, she so desperately claims to need."
    play sound "audio/knock_angry.mp3"
    "Instead, the lady starts banging the door so furiously you'd think there is a prize for it."
    play sound "audio/knock_angry2.mp3"
    "Neither Thiu opens the door, and eventually she gives up."
    play sound "audio/_metal.mp3"
    w "This better not happen again!!" with hpunch
    "The woman feels satisfied thinking she had the final say, and leaves."
    show h miffed at righty
    show s confused at lefty, faceright
    with dissolve
    s "........................"
    show h whatever
    h "Well... There she goes."
    show s angry
    s "..........Just how the hell is her job my problem?"
    show h mock
    h "Exactly! Can't she invest in some earplugs or something?"
    show s disapprove
    s "Right! Why's she tearing into me and not the others??"
    show h nah
    h "Like that guy playing the guitar right now? Go yell at him!"
    show s explain
    s "I don't know, maybe the guitar guy yells back or something."
    show h smug
    h "I'll yell back too next time."
    show s thefuck
    s "Tell her if she rings my doorbell one more time I'll rip the damn thing off and shove it up her ass!"
    show h lol
    play sound "audio/_laugh.mp3"
    h "HaHHAha!!" with vpunch
    show h laugh
    h "Nooo, I can't say that. She'll just get angrier."
    show h kindasmile
    h "Let's just not open the door anymore."
    show s yeahright
    s "Yeah, to anybody."
    show h smug
    h "But the mailman."
    show s sorry
    s "Yeah."
    show h smile
    h "Yeah."
    show s docile
    s "......."
    show h smileaway
    h "............"
    show h awkward
    h "So..... Wanna order pizza?"
    show s ohwell
    s "...I don't know. Are we going to open the door for the delivery guy?"
    show h laugh
    h "Hehee, yes. Him and the mailman."
    show s sad
    s "............Are you going to slice me with the pizza cutter?"
    show h smilegentle
    h "Hmm... Now that is the question."
    show s bitetongue
    s "......................"
    show h smilelow
    h "No. I won't."
    show h smug
    h "Ah, unless you want me to?"
    show s fuckyou
    play sound "audio/_hiss2.ogg"
    s "{b}No!{/b} Isn't that obvious by now??" with vpunch
    show h lol
    stop music fadeout 2.0
    play sound "audio/_laugh.mp3"
    h "Hahahahha!!" with hpunch

    play music "audio/02_outof.mp3" fadein 2.0
    scene black with fade

    "Unbeknownst to Thiu, another door is being abused by an unwanted visitor."

    scene shop with fade

    play sound "audio/enter_shop.mp3"
    show v gentle at lefty, faceright with dissolve
    v "Welcome! What can I--"
    show a smug at righty with moveinright
    a "Hellooo Vivian!"
    show v impatient
    v "........I take it back. You're unwelcome, please leave."
    show a grin_bouncy
    a "Your business looks as slow as ever."
    show v down
    v "What do you want?"
    hide v
    hide a
    with dissolve
    "Tal browses around casually as if Vivian wasn't giving her the death glare."
    show v pissed at lefty, faceright
    show a laugh_bounce at righty
    with dissolve
    a "Nice glass charms."
    show a smug
    a "By the way, have you seen my new bouncy ball?"
    show a grin_bouncy
    a "Watch this--"
    show v heh
    v "You're paying for anything you break."
    show a ohshit
    a "....."
    "Tal puts the bouncy ball back into her pocket."
    show a laugh
    a "So, uhh... Hey, what's up?"
    show a approve
    a "Nice weather we're having lately and all that."
    show v smile_closed
    v "The door is right behind you."
    show a angry
    a "Such cold reception!"
    show a miffed
    a "Can't I just come and have a chat with an old friend?"
    show v ukidding
    v "But that's not what you're here for, is it?"
    show a rage
    play sound "audio/echolong.mp3"
    a "Well not anymore! After receiving this kind of treatment!!" with hpunch
    show v impatient
    v "The door, Tal. Use it."
    show a angry
    a "I was just trying to be nice!"
    show v pissed
    v "It'd be nice if you got out of my shop right now."
    show v ukidding
    v "And tell Lua that if he wants to keep tabs on me, he can come do it himself."
    hide a
    hide v
    with dissolve
    "With this Vivian pushes Tal out the door."

    scene city_late with fade

    show a rage at righty with dissolve
    a "Oh, so Lua's welcome and I'm not??"
    show v impatient at lefty, faceright with dissolve
    v "I did not say that!"
    show v at faceleft
    hide v with moveoutleft
    play sound "audio/doorslam.mp3"
    "Vivian slams the door shut."
    show a angry_bounce
    a "Fine, be that way!"
    hide a with dissolve
    play sound "audio/knock_angry2.mp3"
    "Tal gives the door a couple of kicks." with hpunch
    a "I hope your shop burns down with you still in it!!"
    "She yells a few more death wishes, but gets ignored."
    "Tal finally decides to leave, after she throws her bouncy ball at the door, and it bounces back to hit her in the face."
    show a bored_bounce at righty with dissolve
    a "Ah, who cares about you anyway."
    show shop
    show v ukidding at center
    with dissolve
    v "............................................."

    scene entry with fade

    "Tal returns home."
    show a bored_bounce at lefty, faceright
    show l oh at righty
    with dissolve
    l "You're back sooner than expected."
    show a think
    a "Vivian didn't feel like hanging out..."
    show l lol
    l "Is that so."
    show a rage
    play sound "audio/_thunk.mp3"
    a "That is so!! And she said you can go stalk her yourself next time!" with hpunch
    show l ugh
    l "Stalk her? I do not stalk her."
    show l whatever
    l "I'm merely interested from a business point of view."
    show a miffed
    a "Okay, well the store had no one in it when I was there so..."
    show l oh
    l "Figures. Was she working on anything interesting?"
    show a rage
    play sound "audio/echodull.mp3"
    a "I told you she didn't exactly wanna chat!!" with hpunch
    show l complain
    l "I don't understand why she's being so difficult."
    show a angry_bounce
    a "Yeah me neither! What's her problem??"
    show l playful
    l "Probably the fact that she's a talentless hack whos business is sinking by the minute."
    show a bored_bounce
    a "Yeah, whatever..."
    show l smilesmile
    l "...Exactly. Who cares?"
    show l miffed
    l "By the time I finish my magnum opus, she'll be begging to get in on it!"
    show a think
    a "And I'm begging not to hear another word about it."
    show l ugh
    l "...Fine. I'm busy anyway."
    show l smile
    l "Want to help me out?"
    show a laugh_bounce
    a "Hahahah!! Dream on. I like my organs still intact."
    stop music fadeout 2.0
    show l whatever
    hide a with moveoutright
    l "..............."

    play music "audio/10_goodlook.mp3" fadein 2.0
    scene home_dirty_night with fade

    "Meanwhile Thiu's collective existence wastes away watching cartoons and eating pizza."
    "The laptop screen shines light into the darkness."
    "Oh look! The heroes of the cartoon! They have a new member to their superhero team!! Captain Backstab!"
    show s ohwell at righty, faceright
    show h smile at lefty, faceright
    with dissolve
    s "(He's evil...)"
    show h kindasmile
    h "I bet he's evil."
    show s yeahok
    s "...."
    hide h
    hide s
    with dissolve
    "Oh my god! It's been seven episodes! How could you betray us Captain Backstab!?"
    show s bitetongue at righty, faceright
    show h unhappy at lefty, faceright
    with dissolve
    s "(How the hell are they even surprised?)"
    show h unamused
    h "Oh c'mon! How the hell are they surprised!?"
    show s yeahok
    s "............"
    hide h
    hide s
    with dissolve
    "But wait! It wasn't Captain Backstab after all! He was being framed all along!!"
    show s scold at righty, faceright
    show h miffed at lefty, faceright
    with dissolve
    s "(Bullshit.)"
    show h bleh
    h "That's some bullshit."
    show s ticked
    s "............................"
    show h sorry
    h "....What? You keep giving me the evil eye!"
    show s explain at faceleft
    s "You keep parroting my thoughts and it's annoying."
    show h laugh
    h "Oh? Hahah!! I had no idea."
    show s sad
    s "(Well I guess it makes sense given-)"
    show h shruglaugh
    h "But y'know, that makes sense given we're the same person!"
    show s fuckyou
    play sound "audio/surprise.wav"
    s "Ugh, {i}stop{/i}..! Just stop talking!!" with hpunch
    show s embarrassed
    show h lol
    h "Oh? Again? Hahahah!!"
    show h explain
    h "Anyway, this begs the question..."
    show s surprise
    show h argue
    play sound "audio/echolong.mp3"
    h "WHY AREN'T WE SCREWING YET!?" with hpunch
    show s doubleflip_angry
    play sound "audio/_impact.mp3"
    s "YOU TRIED TO KILL ME, YOU ASSHOLE!!" with vpunch
    show h smug
    h "Hah. Like I ain't ever tried to kill myself before!"
    show h unhappy
    h "More importantly! Why don't you want to have sex!?"
    show h confused
    h "We jack off almost everyday!!"
    show s ticked
    s "I don't know. I just don't feel like it."
    show s sad
    s "I don't really feel like anything anymore."
    show s disapprove
    s "It's kinda like, I dunno, I'm depressed or something."
    show h unamused
    h "Alright, fine."
    show h unsure
    h "Though if you're supposed to have all my negativity, how was I so upset with you earlier?"
    show h confused
    h "I mean I'm over it now, but how did it get so bad?"
    show s explain
    s "How should I know? Jerkface did a crappy job with the spell, I guess."
    show h lol
    h "But that's great, isn't it?"
    show h explain
    h "If I can still be distressed, you can still be happy!"
    show h laugh
    h "You just need to learn to love yourself!"
    show h smilegentle
    h "And by \"love\" I mean--"
    show s fuckyou
    play sound "audio/_metal.mp3"
    s "Oh my god, GO FUCK YOURSELF!!" with hpunch
    show h argue
    play sound "audio/echo.mp3"
    h "I'm {i}trying!!{/i} Bitch won't put out!!" with vpunch
    show s dontcare
    show h whatever
    s "{i}Sighhhh{/i}..... Anyway."
    show s listen
    s "What are we going to do?"
    show s confused
    s "Like... We only have one ID and such. What if we both need to go to the hospital?"
    show s sad
    s "Or if one of us gets declared dead! What then?"
    show h surprised
    h "Oh right! That {i}is{/i} a problem."
    "These are the kinds of thoughts Thiu should've perhaps considered before he rushed headfirst into this mess."
    show s sorry
    s "I think we should merge back together."
    show s docile
    s "I'm sure if we pester Jerkface enough, he'll undo the spell."
    show h unhappy
    h "......Pass."
    show s scold
    s "\"Pass\"?! What do you mean \"pass\"!?"
    show s angry
    s "We shouldn't have split in the first place!!"
    show h bleh
    h "Yeah, I'm not going back to that headspace of yours."
    show s thefuck
    s "Mine!? It's ours!!"
    show s fuckyou
    s "You can't just cherry pick the good parts and lollygag along!"
    show h smilegentle
    h "That's not what you said yesterday."
    show s ashamed
    s "..........W-well... Yesterday's me was an idiot!"
    show s scold
    s "You on the other hand are just selfish!"
    show h mock
    h "Okaaaaay."
    show h laugh
    h "How about we drop this subject here for now?"
    show s think
    s "........"
    show h smilecalm
    h "Let's sleep on it! Maybe a solution comes in a dream!"
    show s sad
    s "...I guess."

    scene black with fade

    stop music fadeout 3.0
    "The Thius get some shut eye."
    "Or at least one of them does... The other is busy mulling over every bad experience he has ever had."
    "But unsurprisingly, no solutions reveal themselves that night."

    play music "audio/05_iwill.mp3" fadein 2.0
    scene home_dirty with fade

    "The next morning the happier half gets up nice and early."
    "And by the time the other half starts waking up, happy half is getting ready to rush out the door."
    show s shrug at righty with dissolve
    s "Huh? Where are you going?"
    show h smile at lefty, faceright with moveinleft
    h "I'm going to see Lua."
    show s docile
    s "If you don't want to merge back, then why? I hate that guy."
    show h laugh
    h "What? Noooo."
    show h shruglaugh
    h "Why would I hate the guy who made me this happy?"
    show s yeahright
    s "Because he made me this miserable."
    show h mock at faceleft
    h "Pshh, you were miserable the day you were born."
    show s worry
    s "Was not..."
    hide h with moveoutleft
    play sound "audio/doorclose.mp3"
    h "Well I'm going anyway! See you later!"

    scene black with dissolve

    "And off he goes."

    scene city_day
    show l oh at righty
    show h smile at lefty, faceright
    with fade
    l "Look who's back already."
    show h laugh
    h "Hellooo hello."
    show l bored
    l "I suppose you can come in."

    scene kitchen_day with fade

    show l oh at righty
    show h smile at lefty, faceright
    with dissolve
    l "So. To what do I owe this displeasure?"
    show h sneaky
    h "Did you come up with a way I can repay you yet?"
    show l pleased
    l "I did, actually."
    show l playful
    l "But you wouldn't agree to it."
    show h kindasmile
    h "...Try me?"
    show l chuckle
    l "Noooooo, no. It's awful, really."
    show l lol
    l "I just know you wouldn't have the guts for it."
    show h miffed
    h "No. What is it? I'll do it!!"
    show l smilesmile
    play sound "audio/Special (8).wav"
    l "Wonderful! It's a deal!"
    show l happy
    l "You are now my new potion tester!"
    show h confused
    h "Err... Wait..."
    show l think_pleased
    l "Ah, this is great!"
    show l down
    l "I've been really struggling ever since the last one... hmm... moved on, let's say."
    show h awkward
    h "So... What kind of potions do you make?"
    show l pity
    l "You'll see soon enough."
    show h nah
    h "................"
    show l mock
    l "Now. Since you're already here and oh, so willing!"
    show l smile
    l "Let's get right to it."
    show l lookup
    l "Help me grind up these berries."
    show h bleh
    h "Hold up. I thought I was a tester, not an assistant."
    show l fake_laugh
    l "Well you're certainly testing my patience right now..."
    show h nervous
    h "Oh... I mean... Fine, I guess."
    show l smile
    l "Say, how is it going with the other you?"
    show l sheepish
    l "I can't help but notice you aren't nearly as chipper as yesterday."
    show h unsure
    h "It's.... fine."
    show l ugh
    l "Ah. Wait. Stop."
    show h confused
    h "??????"
    show l oh
    l "Wash the mortar before you grind the other herbs."
    show h sorry
    h "Oh... Sorry."
    show l pleased
    l "What were you saying?"
    show l whatever
    l "No. Actually, forget that. I don't care about your domestic life."
    show l pity
    l "Just tell me what will you do with the other Thiu."
    show h unsure
    h "Oh... Well..."
    show h shruglaugh
    h "I'm not sure yet... but maybe..."

    menu:

        "Merge back.":

            show h explain
            h "I mean, I was talking to myself and--"
            show l lol
            l "Haha!"
            show h nah
            h "....That's... I meant me and the other me were talking."
            show l smug
            l "I know. You just sounds so dumb."
            show h smilelow
            h ".........So I was thinking about merging back together."
            show l oh
            l "Well that's a bad idea if I ever heard one."
            show h confused
            h "You think so..?"
            show l mock
            l "Guess you already forgot how miserable being you truly is."
            show h mock
            h "Well, while we're on the topic of my misery...."

        "Kill him.":

            show h unsure
            h "I might be better off without my other half..."
            show l oh
            l "That's what I've been trying to tell you."
            show h confused
            h "But he has like... half of my life force or something, right?"
            show l chuckle
            l "Correct."
            show h unhappy
            h "So if I kill him off, I can't get it back, can I?"
            show l pity
            l "No, you can not."
            show l playful
            l "But you're not getting it back by having him around either."
            show h sorry
            h "W-well yeah, but... I can get it if we merge back someday, right?"
            show l lookup
            l "I suppose you'd get what's left of it, yes."
            show l down
            l "But you'd also get back all your depression."
            show h unamused
            h "Actually, about that..."

        "Stay like this.":

            $ narcissus += 1

            show h smilecalm
            h "It's not so bad as it is..."
            show l smile
            l "Oh?"
            show h smileaway
            h "Yeah... It's, uhhh... "
            show h shruglaugh
            h "I mean don't you want a friend who you have everything in common with?"
            show l complain
            l "No."
            h "............................"
            show l pity
            l "And I especially wouldn't want one if it came with as much emotional baggage as your \"friend\"."
            show h unsure
            h "......Speaking of that baggage. I meant to ask you something."

    show h smilelow
    h "I thought you gave the other me all of my unhappiness."
    show h kindasmile
    h "But you didn't, right?"
    show l smug
    l "No, I did."
    show l smilesmile
    l "All you had at {i}that{/i} point in time."
    show l playful
    l "But there is nothing stopping you from accumulating new unhappiness."
    show l chuckle
    l "Especially with someone as gloomy as the other you around."
    show h unhappy
    h "......."
    show l mock
    l "Misery loves company, or so I've heard."
    show l pity
    l "And what miserable company you are. To yourself, that is."
    show h laugh
    h "....Ahahha.... Can we drop this subject?"
    show l ugh
    l "Honestly, just kill the bastard. I really need some fresh ingredients."
    show h confused
    h "...What?"
    show l smile
    l "What?"
    show h sorry
    h "Wait what?? What are we making??"
    show l happy
    l "Oh this!! This is the cure for aging!"
    show l sheepish
    l "It's a work in progress, but I think I've gotten the ingredients down!"
    show l down
    l "Sadly, they're all deadly poison..."
    show l miffed
    l "I'm trying to come up with a nonlethal formula."
    show l smilesmile
    l "And that's where you come in, my dear tester!"
    show l happy
    play sound "audio/Potion Drink (3).wav"
    l "Say \"Aaaah\"!"
    show h confused
    stop music fadeout 2.0
    h "(Oh man... I'm going to die, aren't?)"

    scene home_dirty with fade
    play music "audio/06_gaslight.mp3" fadein 2.0

    "Meanwhile back at home..."

    show s thefuck at righty
    play sound "audio/echowhip.wav"
    s "Man! I want to die!!" with hpunch
    show s angry
    s "(I'm so bored!! When is the other me coming home?)"
    show s down
    s "(I was kinda hoping we could hang out...)"
    show s sad
    s "(I could finally play all those local co-op games I've always wanted to try...)"
    show s smile
    s "(Or I could go eat at those restaurants I'm too anxious to go to alone!)"
    show s ashamed
    s "(Or even just... I don't know. Anything.)"
    show s thefuck with vpunch
    play sound "audio/echolow.mp3"
    s "{i}Tch.{/i} Screw you, other me!"
    show s ticked
    s "(He knows how lonely I am but left anyway!!)"
    show s tocry
    s "(..............I get it though.)"
    show s think
    s "(I would leave me behind too if I could...)"
    s "................................"
    show s hurt
    s "(I'm so pathetic......)"
    show s bigsad
    play sound "audio/_impact.mp3"
    s "({i}God,{/i} I'm so pathetic!!)" with hpunch
    hide s with dissolve
    "Once Thiu's pity party starts, it can last for hours on end."
    stop music fadeout 2.0
    "This one is no exception."

    scene home_dirty_night with fade
    play music "audio/04_cantelope.mp3" fadein 2.0
    play sound "audio/opendoor.mp3"
    "Once the sun has already set, other Thiu makes his way back home."
    show h unwell at righty with dissolve
    h "Ughhh.... I'm home...."
    show h urp
    h "Oh god, I'm gonna hurl..."
    show h confused at faceright
    h "Huh? Why is it so dark in here?"
    show h sorry at faceleft
    h "Hey me are you home--- Oh."
    hide h with dissolve
    "Thiu witnesses his other self sitting catatonic on the kitchen floor."
    show h nah at righty with dissolve
    h "(Oh, great...)"
    show h laugh
    h "...Um, hey there. What'cha up to?"
    s "..................................."
    hide h with dissolve
    "The more miserable Thiu doesn't even bother to lift his gaze to look at the other."
    show h unhappy at righty with dissolve
    h "(Ugh, c'mon... I'm way too nauseous to deal with my bullshit right now...)"
    show h whatever
    h "............"
    s ".................."
    show h unsure
    h "{i}Sigh....{/i}"
    show h smilelow
    h "(What did I use to want when I got like this?)"
    show h nah
    h "(\"Death\" is what I would say but...)"
    show h sneaky
    h "(Ahhh, I'm such a little drama queen...)"
    hide h with dissolve

    menu:

        "Mock yourself.":
            show h mock at righty with dissolve
            h "You know living is fully optional, right?"
            s ".................................."
            show h miffed
            h "You don't want to be here? Fine. Don't."
            show h shruglaugh
            h "Every single person who ever lived on this earth is either dead or going to die."
            show h whatever
            h "Fast forward your life, who cares."
            show s bitetongue at lefty, faceright with dissolve
            s "...........Are you seriously telling me to off myself right now?"
            show h kindasmile
            h "Makes you mad, doesn't it?"
            show h explain
            h "Why is that?"
            show s embarrassed
            s ".......You don't get it at all."
            show s ticked
            s "And that's the worst thing you could've said to me."
            show h unamused
            h "I'm not gonna reward this kind of behavior with hugs and kisses, if that's what you were looking for."
            show s disapprove
            s "I was looking to die, actually."
            show h smilegentle
            h "Hmm. Is this it then?"
            show s sad
            s "I don't know."
            show h smug
            h "Yeah you do. Yes or no. Pick one."
            show s bitetongue
            s "I don't know."
            show h miffed
            h "No, don't give me that. Do you want to die right now or not?"
            show h explain
            h "You know I'm fully willing to assist you if--"
            show h surprised
            show s thefuck
            play sound "audio/_impact.mp3"
            s "I SAID I DONT KNOW!!" with vpunch
            show s fuckyou
            s "I don't know you fucking self-important bastard!! You think you're so smart!?"
            show h laugh
            h "Oh wow, hahaha!"
            show s doubleflip_angry
            play sound "audio/_hiss2.ogg"
            s "Arrogant little shit, coming here telling me what to do!!"
            show s explain
            show h smilelow
            s "So easy for you to say! You got the good end of the stick!"
            show s bigsad
            play sound "audio/_metal.mp3"
            s "{b}OF COURSE I DON'T WANT TO DIE!!{/b}" with hpunch
            show s desperate
            s "Idiot!! Of course I don't!!"
            show s bitetongue
            s "But that doesn't mean I want to live either!"
            show s yeahright
            s "So I don't know!"
            show s listen
            s "You tell me!"
            show h smile
            h "Me?"
            show s thefuck
            s "Yeah, you!! What do you want to do?!"
            show h smilelow
            h "Well..."
            show h shruglaugh
            h "I want to clean up that shirt. The sleeve's all bloody."
            show s embarrassed
            s "....................."
            show h smilelow
            h "Will you let me fix it?"
            show s sorry
            s "..............................................."
            show s down
            s "...I don't think you can. It's all dried up already."
            show h explain
            h "You won't let me even try?"
            show s ticked
            s "............Fine."
            show h sneaky
            h "Alright. C'mon then, there's body wash in the bathroom..."

            scene bathroom with fade

            "Happier Thiu pulls sadder Thiu's hand under the falcet."
            "And unleashes cold water upon the bloody sleeve."
            play sound "audio/_increase.mp3"
            s "AHH NO NO!! No, wait, STOP!" with vpunch
            s "Let me take it off!! Let me take it off!!"
            h "No need. It's just the sleeve."
            play sound "audio/_impact.mp3"
            s "AHH!! IT STINGS!! LET GO!! GOD, IT HURTS!!" with hpunch
            show h unamused at lefty, faceright with dissolve
            h "I said I'd clean it. I didn't say it'd be pleasant."
            show s fuckyou at righty with dissolve
            s "There was no need to do it this way!!"
            show s disapprove
            s "What is wrong with you!?"
            show h awkward
            h "Actually I'm really nauseous."
            show s confused
            s "Huh???"
            hide h
            hide s
            with dissolve

        "Be kind to yourself.":

            $ narcissus += 1

            show h mock at righty with dissolve
            h "I know you don't really care, but..."
            show h kindasmile
            h "Lua's gonna be pissed once he finds out you got blood all over his shirt."
            s ".........................."
            show h explain
            h "C'mon, up up! We can still salvage it."

            scene bathroom with fade

            "Happier Thiu drags sadder Thiu to the bathroom."
            "Where he proceeds to try to wash the shirt."
            show h sorry at lefty, faceright with dissolve
            h "Ahhh, or maybe not."
            h "It's all dried up already."
            show h unhappy
            h "Just how long where you sitting there?"
            show s sad at righty with dissolve
            s "...................."
            show h smilegentle
            h "Hmm? Half an hour? Two hours?"
            show h mock
            h "Your ass must be so sore!"
            s "........................"
            show h smilelow
            h "Nothing huh?"
            show h shruglaugh
            h "Well I'm going to list some things that you like."
            show h explain
            h "You're bound to want to live after you remember all this!"
            show s worry
            s "Ughhhhh... I don't want to hear it."
            show h smug
            h "Chips! And soda!"
            show h laugh
            h "Ice cream, cinnamon rolls..."
            show h shruglaugh
            h "And ice cream on cinnamon rolls!"
            show h mock
            h "French toast, lemon cheese cake..."
            show h sneaky
            h "Pizza, fries, and chocolate.."
            show h confused
            h "Lasagna, and those-..., what were they..?"
            show h smilelow
            h "Those little almond cookie things..."
            show s confused
            s "...What? Macarons?"
            show h shruglaugh
            play sound "audio/_nervousbubbles.mp3"
            h "Yes, macarons!!" with vpunch
            show s ticked
            s "You're just listing food!"
            show h smug
            h "Okay fine! Watching porn is pretty exciting too."
            show s thefuck
            play sound "audio/echodull.mp3"
            s "JUST STAB ME ALREADY!" with vpunch
            show s desperate
            s "Just like yesterday! You wanted to, right!?"
            show h lol
            h "Yes. About time."
            show h smile
            h "But, oh no, what's this??"
            show h shruglaugh
            play sound "audio/_laugh.mp3"
            h "My free stabbing offer has expired! Tooooooo bad!"
            show s fuckyou
            s "Why would it expire!?"
            show s bigsad
            play sound "audio/isbad.mp3"
            s "I'm still stupid, and ugly, and nobody likes meeeeee!!" with hpunch
            show s hurt
            s "I deserve a hammer to the head!!"
            show h smilelow
            h "Wow, thanks."
            show s confused
            s "Thanks??"
            show h nah
            h "Yeah. Keep on insulting me, no biggie."
            show s embarrassed
            s "Obviously I'm not talking about you!"
            show h smilegentle
            h "Really? Explain that to me."
            show s ticked
            s "Don't play dumb! I mean {i}me{/i} and you know it!!"
            show h kindasmile
            h "And who do you think I am?"
            show s sorry
            s "......I don't know. Something better."
            show h urp
            play sound "audio/_thunk.mp3"
            h "!!!" with hpunch
            show s embarrassed
            s "What?"
            hide h
            hide s
            with dissolve

    play sound "audio/vomit.wav"
    "Thiu starts unceremoniously puking into the toilet bowl."
    show s surprise at righty with dissolve
    s "....................."
    show h unwell at lefty with dissolve
    h "Ughh my god... Sorry. I've been eating poison all day..."
    show s angry
    s "What kind of idiot does stupid stuff like {i}that{/i}?"
    show h sorry at faceright
    h "Hahah... Look who's talking..."
    show s scold
    s "Yeah, I'm looking at him alright."
    show h nervous
    h "It's just that Lua made me his poison tester..."
    show s disapprove
    s "And you agreed to that {i}because{/i}....?"
    show h unamused
    h "I really don't want to owe a guy like that any favors..."
    show h smileguilty
    h "So I'm just getting it over with."
    show h urp
    h "Oh no...!"
    hide h with dissolve
    show s worry
    play sound "audio/vomit.wav"
    s "............................."
    scene black with fade
    show puke1:
        xalign 0.5 yalign 0.2
    with dissolve
    s "Guess I really am stupid..."
    play sound "audio/_nervousbubbles.mp3"
    h "HAHAHAH!!" with vpunch
    h "Oh god......"
    h "There's nothing left anymore, it's just stomach acid now..."
    h "It hurts..."
    play sound "audio/Special (8).wav"
    show puke2:
        xalign 0.5 yalign 0.2
    hide puke1
    with dissolve
    s "Well...."
    s "I think you managed to salvage the shirt..."
    stop music fadeout 2.0
    h "Well good. Don't mess it up again..."

    play music "audio/steady.mp3" fadein 2.0
    scene home_dirty_night with fade

    "As they lay down to sleep, sadder Thiu thinks to himself..."
    s "(Actually isn't this kinda like a sleepover?)"
    s "(Maybe we should get snacks and watch a scary movie or something!)"
    s "(Well, it's kinda late now... Maybe tomorrow?)"
    s "(We can get chips and soda! Maybe ice cream...)"
    s "(Heh..!)"
    s "(If it's like this, then maybe staying separate is alright.)"

    "Happier Thiu on the other hand thinks about something entirely different."
    h "(Ugh, this is exhausting...)"
    h "(What's the point of separating all that junk from myself if I'm the one who has to deal with it anyway.)"
    h "(Well I guess it's easier to manage when I'm not the one actively having a meltdown...)"
    h "(But still! This crap cost me half my life.)"
    h "(...If only the other me was a little more stable.)"
    h "(I wouldn't mind merging back...)"

    scene black with fade
    stop music fadeout 2.0
    "And that's how that night went."

    scene shop with fade
    play music "audio/01_rideout.mp3" fadein 2.0

    "Legend says, that if the first face you see in the morning belongs to Lua, your day is gonna suck."
    "This legend originates from Vivian's shop."
    "The very shop Lua is currently entering."

    play sound "audio/enter_shop.mp3"
    show l happy at righty with moveinright
    l "Hello!"
    show v ukidding at lefty, faceright with dissolve
    v "........................................"
    show l chuckle
    l "Nothing? Let me try again."
    hide v
    hide l
    with dissolve
    "Lua exits and re-enters the store."
    show v ukidding at lefty, faceright with dissolve
    play sound "audio/enter_shop.mp3"
    show l happy at righty with moveinright
    l "{b}Behold!!{/b} I have come to grace your humble shop with my amazing presence."
    show v unimpressed
    v "Go away."
    show l smilesmile
    l "And I missed you too, Vivian."
    show l down
    l "I can't believe you turned Tal away the other day. Weren't you best friends or something?"
    show v impatient
    v "Go away."
    show l angry_explain
    l "\"Go away, go away...\" Is that all you have to say?"
    show v heh
    v "Go away."
    show l oh
    l "Go away."
    show v pissed
    v "........."
    show l mock
    l "......What else?"
    show v think
    v "Fine... What do you want?"
    show l bored
    l "Must I always want something to visit you?"
    show v down
    v "I don't know. Must you?"
    show l pity
    l "Yes. I want to talk."
    show v ohyeah
    v "Fine. Say what you have to say. And then leave."
    show l ugh
    l "Vivian, sometimes this attitude, I swear..."
    show v heh
    v "............Well?"
    show l lookup
    l "Well! Seeing as you're not one for pleasantries, I'll cut to the chase."
    show l oh
    l "I've resumed working on our project."
    show v down
    v ".................................Why?"
    show l happy
    l "And it is going well!"
    show l playful
    l "So well, in fact, that I've chosen to put aside our petty squabbles."
    show v pissed
    v "\"Petty squabbles\"?!"
    show v impatient
    v "Is that how you see it!?"
    show l down
    l "Please, can we not start about that again?"
    show v pissed
    v "I can't believe you! What happened to--"
    show l lol
    l "You're awfully talkative for someone supposedly giving me the silent treatment."
    show v sigh
    v "....Just get out of my store."
    show l sheepish
    l "No, no, I'm sorry. Honestly."
    show l lookup
    l "I didn't mean to call it a petty squabble, I meant, hmm..."
    show l whatever
    l "Well, I guess I meant to call it whatever you wanted me to call it."
    show v worry
    v "Just leave."
    show l angry_explain
    l "Vivian, I am giving you a very generous offer right now. I'd suggest you don't waste my kindness."
    show v pissed
    v "I also consider me keeping quiet about your business really generous, so I suggest you stop bothering me."
    show l lol
    l "And I consider your silence a given, considering how deeply involved you were in my business."
    show v ukidding
    v "....I'm not going to start this pissing match with you."
    show v unimpressed
    v "And I'm not interested in working with you again."
    show v impatient
    v "So thank you for the offer, but keep the credit!"
    show l smilesmile
    l "I'll let you think about it."
    show v think
    v "No need. Please leave."
    show l pity
    l "I'll let you anyway."
    show l playful
    l "Goodbye for now, I really wish you'd drop by sometimes."
    show l chuckle
    l "And you misspelled \"incantations\" on your window ad, there is no \"s\" in the middle."
    show v pissed
    play sound "audio/_metal.mp3"
    v "Argh!! Just go!!" with hpunch
    hide l
    hide v
    with dissolve
    stop music fadeout 2.0
    "Feeling like the smug bastard he is, Lua exits the shop."

    play music "audio/02_outof.mp3" fadein 2.0
    scene home_dishless with fade

    "Meanwhile Thiu is musing about his depression."
    show h unsure at righty with dissolve
    h "(I think loneliness and lack of future, are the main causes of my misery.)"
    show h unamused
    h "(But obviously I'm going to be lonely with such a shit personality and no social skills...)"
    show h whatever
    h "(Maybe if dad hadn't kicked my ass every time I opened my mouth, I would've learned to hold a conversation...)"
    show h confused
    h "(...And then there's also my awful diet and lack of exercise.)"
    show h unhappy
    h "(If I could get some of this crap under control, we could merge back and I could take it from there...)"
    show h unwell
    h "(Lua said our life force got split too. So if we stay like this, I'll die in my forties.)"
    show h nah
    h "(And that's a generous estimate given my lifestyle so far.......)"
    hide h with dissolve
    "He watches his other self play video games."
    show h whatever at righty with dissolve
    h "(I don't think other me has it in him to fix anything though...)"
    show h nah
    h "(If I leave him to his own devices, I can go live a nice short life somewhere.)"
    show h unsure
    h "...{i}Sigh.{/i}"
    show h laugh
    h "Hey me?"
    show s docile at lefty, faceright with dissolve
    s "Huh? Yeah?"
    show h smile
    h "What'cha playing?"
    show s disapprove at faceleft
    s "You have eyes, don't you?"
    show h fuckyou
    play sound "audio/_hiss1.ogg"
    h "(I'm trying to make conversation, stupid!!!!)"
    show h awkward
    h "Ahh... Okay.... But weren't we stuck in that one?"
    show s dontcare
    s "Yeah, that's why I'm grinding levels! I'm almost at 75."
    show h argue
    play sound "audio/_hiss2.ogg"
    h "(STOP WASTING MY LIFE. SSSSSSSSSTUPID!!!)"
    show h sorry
    h "Umm... Hey, can you pause it for a bit? Let's chat."
    show s ohwell
    s "Go ahead. I'm listening."
    hide h
    hide s
    with dissolve
    "Thiu is too busy crafting equipment to lift his gaze from the screen."
    show h whatever at righty with dissolve
    h "......................Okay."
    show h miffed
    h "(Forget this.)"
    show h unsure
    h "Just letting you know I'm going over to Lua's again."
    hide h with dissolve
    "Now the game gets paused."
    show s shrug at lefty, faceright
    show h unsure at righty
    with dissolve
    s "A-again? Why??"
    show h kindasmile
    h "Like I said yesterday, I'm--"
    show s scold
    s "How long do you have to do the poison thing?"
    show h pissed
    h "(Yeah fucking talk over me, why not!)"
    show s docile
    s "....Me?"
    show h shruglaugh
    h "I don't know. It's up to Lua."
    show s ticked
    s "Lua, Lua, Lua... I'm getting sick of the name."
    show h unhappy
    h "Yeah? I'm getting sick of a lot of things too..."
    show s confused
    s "...Huh?"
    show h sorry
    h "Ahhh, sorry! That came out wrong."
    show h laugh
    h "Poison! Ah, that's what I meant!"
    show h lol
    play sound "audio/_laugh.mp3"
    h "I'm getting sick off poison, hahhah! Badum-tsssh!"
    show s sorry
    s "Oh.... Right."
    show s shrug
    s "Well, um... "
    show s ohwell
    s "...I don't know what to say."
    show h whatever
    h "Me neither."
    show h explain
    h "Now go back to your video game, don't slit your wrists, and I'll be back before you know it!"
    show s laugh
    play sound "audio/Special (8).wav"
    s "Hehe! Okay!"
    show h surprised
    h ".........."
    show s smile
    s "Bye bye."
    show h sorry
    stop music fadeout 2.0
    h "Uh... Yeah! Bye!"

    play music "audio/03_partisan.mp3" fadein 2.0
    scene city_day with fade

    show h puzzled at lefty, faceright with dissolve
    h "(That was-... He was smiling, right??)"
    hide h with dissolve
    "As Thiu ponders on that, he spots Lua."
    show h smug at lefty, faceright
    show l oh at righty
    with dissolve
    h "Oh... It's weird seeing you out and about."
    show l miffed
    l "We're not all homebodies like you."
    show h shruglaugh
    h "Well, I was just about to come over."
    show l angry_explain
    l "Pretty shitty of you to keep dropping by unannounced."
    show h kindasmile
    h "............I-.. thought we're working on something though?"
    show h mock
    h "But if it was a one time thing, heyyy! No complaints!"
    show l complain
    l "Don't be ridiculous."
    show l bored
    l "Not all poison kills you immediately."
    show l mock
    l "I should give you at least a week to see if you drop dead or not."
    show l miffed
    l "And should your existence continue, then I want to try another batch on you."
    show h sorry
    h "Oh... okay..."
    show h unsure
    h "........................"
    show l whatever
    l "..................."
    show h nervous
    h "Sooooo..."
    show h smileaway
    h "See you in a week, then?"
    show l ugh
    l "I thought you're coming over."
    show h unhappy
    h "(Oh my god, make up your mind!)"
    show l angry_explain
    l "Well?"
    show h mock
    h "I'll pass, you seem busy."
    show l complain
    l "Like I'll let you jerk me around like this!"
    show l ugh at faceright
    l "You said you're coming over, so over you'll come!"
    show h fuckyou
    h "(Then why'd you even ask!?!?!?)"

    scene entry with fade

    show h smilelow at lefty, faceright
    show l oh at righty
    with dissolve
    h "Are you having a bad day or something?"
    show l playful
    l "Whatever gave you that impression?"
    show h nah
    h "I don't think I did anything to warrant this kind of treatment."
    show l ugh
    l "Pray, tell, what kind of treatment do you think you deserve exactly??"
    show h unsure
    h "Uhh... well......"
    show a smug at right with moveinright
    a "Sheesh, she said no, huh?"
    show l bored at faceright
    l "..........Yes, as a matter of a fact, she did."
    show l angry_explain
    l "But that's got nothing to do with anything."
    show a grin_bouncy
    a "Yeah yeah, of course not. Just throwing a hissy fit for fun."
    show l complain
    l "Yes. It's delightful!"
    show l ugh
    l "Now piss off, the both of you."
    show h confused
    h "Wha-huhhh?? You made me walk all the way here for nothing??"
    show l bored
    l "Tough, isn't it?"
    show h unhappy
    hide l with moveoutright
    h ".................."
    show a laugh_bounce at righty with moveinright
    a "Hahah!! What a sourpuss, right?"
    show h unamused
    h "What crawled up his ass?"
    show a think
    a "Ahh, it's just Vivian. Don't worry about it..."
    show h puzzled
    h "(Who's Vivian???)"
    show h awkward
    h "Ummm.... Okay...?"
    show a laugh
    a "Anyway! You seem to be doing fine!"
    show a smile_bounce
    a "How's life like after being split in half?"
    show h mock
    h "Let's just say it has its challenges..."
    show a grin_bouncy
    play sound "audio/_laugh.mp3"
    a "Hahah!! I bet!"
    show a playing
    show h smile
    a "If I got split in half, I'd probably become an assassin!"
    show a smug
    a "Because I could make myself seen, while the other me does the killing."
    show a excited
    a "So I'd have the perfect alibi every time!! Hahah!!"
    show h nah
    h "Riiight, right... Of course."
    show h kindasmile
    h "Why not do just that then?"
    show a bored_bounce
    a "Are you kidding me? That'd cost me half my life!"
    show a laugh_bounce
    a "Only an idiot would make that trade! Hahahah!!"
    show h smilelow
    h "..............."
    show a think
    a "Anyway, guess what! I've spent the last few days washing a wall."
    show a laugh
    a "It turns out permanent marker doesn't come off that easy, who'd have thought, hahha!!"
    show h smile
    h "You're talking about when we drew on the wall together?"
    show a listening
    a "Wait... I drew with you?"
    show h laugh
    h "Yeah, right after I got split! We tried drawing cats with our eyes closed."
    show a ohshit
    a "That was you??"
    show h sorry
    h "Yeah..?"
    show a think
    a "Weird, I could've sworn I was drawing with the happy half."
    show h miffed
    h ".............I {i}am{/i} the happy half."
    show a ohshit
    play sound "audio/_thunk.mp3"
    a "..............................."
    show a laugh_bounce
    a "Aaaah, okay! Sorry! Hahahah!!"
    show a playing
    a "It's just you look so alike, HAHA!!"
    show h unsure
    h "......................Yeah."
    show a approve
    a "Don't mind me! And don't mind Lua either."
    show a listening
    a "He'll brood for a bit, and then he'll act like none of this ever happened."
    show a smile_bounce
    a "So don't worry about it. You can go home or something."
    show h nervous
    h "Alright, I'll see you around then?"
    show a laugh_bounce
    stop music fadeout 2.0
    a "Yup! See you later!"

    play music "audio/07_battle.mp3" fadein 2.0
    scene city_day with fade

    show h confused at center with dissolve
    h "(......Do I look that down?)"
    show h unhappy
    h "(That's bad...)"
    show h unwell
    h "...................................."
    show h shruglaugh
    h "(Aaaah, it's fine! It's fine!!)"
    show h unsure
    h "(It's just that I'm still kinda weak from yesterday. That's all!)"
    show h laugh
    h "(For now, let's just focus on making the other me a little less miserable!)"
    show h mock
    h "(Food! We'll cheer up with some food!)"
    show h smile
    h "(Now what should I get for me and myself?)"
    hide h with dissolve

    menu:

        "Sweets and treats.":

            $ narcissus += 1

            show h sneaky at center with dissolve
            h "(That's right. I deserve it after everything that has happened!)"
            show h nah
            h "(Jesus what a mess I'm in... Of course I look a little down today.)"
            show h kindasmile
            h "(And other me, well... His life sucks so bad in general I should buy him a whole bag of candy.)"
            show h smilelow
            h "(Yeah... Maybe he'll even smile for me again?)"


        "Something healthy.":

            $ healthy = True

            show h laugh at center with dissolve
            h "(Yeah, I'll get something healthy!)"
            show h nah
            h "(Then other me too will get some energy to... I dunno, {i}do{/i} something!)"
            show h unsure
            h "(If he'd just work with me, I'm sure we could improve our life...)"
            show h unhappy
            h ".....{i}Sigh.{/i}"


    scene black with fade
    stop music fadeout 2.0
    "And so, Thiu goes to do some shopping."

    play music "audio/05_iwill.mp3" fadein 2.0
    scene home_dishless with fade

    "But how is our little bundle of sorrows doing?"
    "As one might guess, he has spent the entire day with the video game."
    "But try as he might, he can't clear a secret boss."
    "And he must clear it. Otherwise he can't 100\% the game!!"
    "And that would mean his whole life has been for nothing."
    show s thefuck at righty with dissolve
    s "Argh! Who balanced this piece of crap!?"
    show s explain
    s "I can't stand this battle music anymore! Duu-de-duu-de-dee, annoying!"
    show s bitetongue
    s "I'd rather drink poison than play another minute!!"
    show s yeahok
    s "(Yeah, drink poison, just like the other me.)"
    show s sorry
    s "........"
    show s worry
    s "(....He was mad at me this morning, wasn't he?)"
    show s think
    s "(Why is that?)"
    show s docile
    s "(...I don't get it. And how's that possible?)"
    show s ashamed
    s "(It's literally me. I should know all about him...)"
    show s yeahok
    s "(Ahhhhh... Wait.)"
    show s dontcare
    s "(Is it because I don't help him clean?)"
    show s explain
    s "(Is it still about that? I didn't take myself for such a petty person.)"
    show s whatever
    s "(And it's not even that big of a mess in here.)"
    show s down
    s "(If I just picked up the dirty clothes, it'd already be so much cleaner.)"
    show s worry
    s "(..............................Then do it.)"
    show s sad
    s "(Nah, what's the point? It doesn't matter anyway.)"
    show s whatever
    s "(...It matters to the other me.)"
    show s yeahright
    s "{i}Tch.{/i} (So what. Let him pick them up then.)"
    show s embarrassed
    s "(...But he'd probably be happy if I did it.)"
    show s bitetongue
    s "(But probably not because the house would still be a mess!)"
    show s angry
    s "(So whether I pick up the clothes or not, doesn't matter either way.)"
    show s thefuck
    s "(Arrghh!! If it doesn't matter either way, then do it!)"
    show s ticked
    s "(There is no reason not to do it!!)"
    show s explain
    s "(Can't you do this much you absolute waste of space!?)"
    show s thefuck
    s "(Just get off your lazy ass and do it!)"
    show s scold
    s "(See that hoodie? Pick that up!)"
    s "(Pick up only the hoodie and take it to the laundry basket.)"
    s "(We can consider that a win.)"
    show s disapprove
    s "(Well that's just stupid, why would I only pick up one item?)"
    show s listen
    s "(That'll really impress the other me!)"
    show s down
    s "(Just really bloody highlight what an absolute piece of sh--)"
    show s thefuck
    play sound "audio/_increase.mp3"
    s "(ARGHH, STOP STOP STOP {b}STOP!!{/b})" with hpunch
    show s embarrassed
    s "(Just pick up the damn laundry, do it! Do it now you piece of shit!! DO IT!!)"
    hide s with dissolve
    "After a bit more of bullying himself into it, Thiu picks up all the dirty laundry."

    scene bathroom with fade

    "He unlovingly shoves them all into the washing machine."
    "It takes but a minute, but he feels like he has completed a herculean task!"
    show s smile at lefty, faceright with dissolve
    s "Hahah!! Look at that!!"
    show s makenice
    s "Am I an adult or what?"
    show s nervous_smile_away
    s ".............."
    show s bigsad
    play sound "audio/echowhip.wav"
    s "(Oh lord, what kind of a loser feels proud over laundry!?)" with vpunch
    show s thefuck
    s "(This is what you're {i}supposed{/i} to do!! Fucking dumbass!)"
    hide s with dissolve
    "There is no winning against Thiu's powers of self loathing."
    play sound "audio/opendoor.mp3"
    h "I'm home!"
    show s embarrassed at lefty, faceright with dissolve
    s "Ah, err... W-welcome home?"
    show h laugh at righty with moveinright
    h "There you are! I bought food!"
    "The washing machine makes an unholy amount of noise as it spins."
    show h smile
    h "Oh? You're doing laundry?"
    show s down
    s "Uh... y-yeah... I guess....."
    h "..........."
    s ".........."
    show h smilelow
    h "(Oh man, I really want to make a snide remark about hell freezing over or something but....)"
    show s bitetongue
    s "(I bet he'll say something snarky about hell freezing over and I'll feel like moron for doing any of this...)"
    show h shruglaugh
    play sound "audio/_nervousbubbles.mp3"
    h "...I'm surprised the washing machine still works, honestly."
    show s surprise
    s ".................."
    show s laugh
    play sound "audio/special.wav"
    s "Oh, ahah... Yeah."
    show s makenice
    s "I mean... I guess it's pretty old. Didn't I buy it used too?"
    show h smilecalm
    h "Yeah, I did. From the previous tenant."
    show s whatever
    s "Though I guess it was more like he left it here and demanded I pay for it..."
    show h unamused
    h "Can't believe I paid for it..."
    show s yeahright
    s "I can! The dude was scary!!"
    show h mock
    h "Yeah, yeah. Everyone is scary to you."
    show h smilegentle
    h "Anyway, thanks for doing the laundry."
    show h smileaway
    h "The house looks much nicer already."
    show s shy
    s "Oh!! Aha.. ha... Y-yeah!! No problem!!"
    show h laugh
    h "Yeah, I appreciate it."
    show h kindasmile
    h "And guess what you're going to appreciate."
    show s embarrassed
    s "...Uhhh?"
    show h shruglaugh
    play sound "audio/Special (8).wav"
    h "FOOD! That I've lovingly picked up just for you!!" with hpunch
    show h lol
    h "Haha, I wanted to say just for me, but I bet you'd misunderstand."
    show s docile
    s "Uhh... what?"
    show h sneaky
    stop music fadeout 2.0
    h "Yeah, exactly."

    play music "audio/13_where.mp3" fadein 2.0
    scene home_laundryless_night with fade

    if healthy == True:
        "Thiu is proud to present himself a take-out box filled with grilled fish and some salad."
        show s yeahok at righty with dissolve
        s ".....................What is this filth?"
        show h shruglaugh at lefty, faceright with dissolve
        h "A healthy meal full of nutrients!"
        show s yeahright
        s "I'm not hungry..."
        show h smug
        h "Yes you are!!"
        show h mock
        h "I went out of my way to buy this for you!"
        show s doubleflip_angry
        play sound "audio/_hiss2.ogg"
        s "WHY?! To bully me??" with vpunch
        show s disapprove
        s "You know goddamn well I can't stand fish or vegetables!"
        show h sneaky
        h "I'm taking care of myself!"
        show h unamused
        h "Isn't that precisely what you want?"
        show s think
        s "But can't you be more like..."
        show s explain
        s "\"Aweeee you poor thing. Take it easy! Here's candy and games and my unconditional love and support!\""
        show h nah
        h "Sure, if you were an infant."
        show s embarrassed
        s "Oh c'mon."
        show h unhappy
        h "I'll bake you a pizza if you give the fish and salad a try."
        show s scold
        s "..........."
        h "..........."
        hide s
        hide h
        with dissolve
        "Begrudgingly, Thiu takes the meal."
        show s disapprove at righty with dissolve
        s "I can't even bake."
        show h shruglaugh at lefty, faceright with dissolve
        h "Pssssh, whatever! The internet will tell me how."
        show h smile at faceleft
        h "Let's see, what do I need for it anyway?"
        hide s
        hide h
        with dissolve
        "Thiu rummages through the kitchen cabinets."
        show h confused at lefty with dissolve
        h "How old is this flour--"
        show h surprised
        play sound "audio/_thunk.mp3"
        h "WHOAH! There's bugs in it!?!" with hpunch
        hide h with dissolve
        "Other Thiu munches on some fish and watches his other self google pizza dough instructions."
        show h confused at lefty with dissolve
        h "...Wait. I need a bowl? Think a pot will do instead??"
        show s ohwell at righty with dissolve
        s "..........."
        show h miffed
        h "And a dough scraper..? The heck is that?"
        show h nervous
        h "I mean we have a spatula..."
        show s embarrassed
        s "(Look at this moron.)"
        show s ashamed
        s "(What are you even doing..?)"
        show h mock
        h "..........Actually y'know what? I should leave this baking stuff to the professionals."
        show h laugh at faceright
        h "I'm just gonna order--"
        show s whatever
        s "No. Make it."
        show h kindasmile
        h "Huh? Really? There's like worms in the flour."
        show s explain
        s "I'm already eating fish, might as well eat worms too."
        show h smile
        h "How is the fish by the way?"
        show s sad
        s ".........It's okay, I guess."
        show h sneaky
        h "Ha! Good. It's good for you."
        show s listen
        s "Yeah, you're eating the rest."
        show h lol
        h "Nah, that's okay. I really think I'm gonna order that pizza."
        show s scold
        s "No, you're eating the damn fish!!"
        show h explain
        h "No, no! I'm okay. You can throw the rest away."
        show s thefuck
        play sound "audio/_metal.mp3"
        s "YOU EAT WHAT YOU'RE GIVEN!!" with vpunch
        show h lol
        play sound "audio/_nervousbubbles.mp3"
        h "Oh, god, I'm getting flashbacks. Hahaha!!"
        show s laugh
        s "That's right! \"You'll either eat it or you'll cry and eat it!\""
        show h shruglaugh
        h "Nooo, don't whoop my ass dad! Hahahah!!"
        show s dontcare
        s "Eat the fish or I'll kill your parakeet."
        show h unsure
        h "....Don't bring that up. That one still hurts."
        show s confused
        s "Really? I thought you wouldn't feel it."
        show s docile
        s "Since I got all the bad stuff."
        show h confused
        h "That one is more like... Hmm..."
        show h unamused
        h "I remember it and the pain re-ignites?"
        show h pissed
        h "Like, fuck man. How could he do that?"
        show s sorry
        s "\"I bought it and I'll kill it if I want to.\""
        show h whatever
        h ".............."
        s "..............."
        show h bleh
        h "...Ah, give me the fish. I'll eat it."
        show s ohwell
        s "I finished it already..."
        show h laugh
        h "Oh? Well thank you!"
        show s yeahok
        s "And I'm still expecting that homemade pizza."
        show h mock
        h "Okay but I'm not using the flour we have."
        show h smilecalm
        h "Wanna drop by at the store together?"
        show s makenice
        s "I guess. And we can buy more fish."
        show h smilelow
        h "Don't some people put tuna on a pizza?"
        show s explain
        s "Gross. We're not doing that..."

        scene black with fade

        "Pizza is made that night and it sucks."
        stop music fadeout 2.0
        play sound "audio/Special (8).wav"
        "The Thius are proud of it anyway."

    else:
        "Thiu hands himself a shopping bag full of cheap candy."
        show h shruglaugh at lefty, faceright
        play sound "audio/Special (8).wav"
        h "Tadaaah!!"
        show s docile at righty with dissolve
        s ".............????"
        show h mock
        h "Well? Look at this! A bag of treats!"
        show h explain
        h "Isn't this a dream come true?"
        show s down
        s "I-... you really bought all this for me?"
        show h laugh
        h "Yeah, yeah!! A bag of short-term happiness!"
        show h lol
        h "Eat that dopamine, baby!"
        show s think
        s "Wow..."
        show s yeahright
        s "Doesn't this like... make you twice as miserable after the sugar spike is over?"
        show h smilegentle
        h "Weeeell, if you don't want it..."
        show s confused
        s "N-no! No! I want it! I'll eat them!"
        show h sorry
        h "....I'll say I was expecting you to be a little happier."
        show s disapprove
        s "That's like expecting a dog to be a cat."
        show h kindasmile
        h "It's candy!! How is this not thrilling?"
        show s angry
        s "Maybe if I was a kid."
        show h unamused
        h "Oh, bullshit."
        show h sneaky
        h "I have a very vivid memory of wishing to be coddled up and given candy and hugs and pity!"
        show s ashamed
        s "........This memory is a true one, yes."
        show h explain
        h "So? What's not to like? The candy has arrived!"
        show s stopcrying
        s "...{\i}*Sniff*{/i} Yeah."
        show h surprised
        h "H-huh!?!"
        show h puzzled
        h "What's wrong!?"
        show h nervous
        h "This is literally the opposite effect from what I wanted..."
        show s bigsad
        play sound "audio/_nervousbubbles.mp3"
        s "Aaaahhh, I don't know! Sorry, I don't know!"
        show s desperate
        s "I can't believe someone bought me something nice!"
        show h smilelow
        h "Not sure if I count as \"someone\" but yeah, sure."
        show h mock
        h "Hand picked with love and care!"
        show h unamused
        h "I even spent time at the pick-n-mix making sure I got only red and yellow gummies. None of that green stuff."
        show s bigsad
        s "{i}*Sob*{/i} Oh my god..."
        show s thefuck
        play sound "audio/_impact.mp3"
        s "{b}Let's get married!!{/b}" with vpunch
        show h lol
        play sound "audio/_laugh.mp3"
        h "HAHAHAHAHA!!!" with hpunch
        show s doubleflip
        s "Shut up! You just don't understand."
        show h smug
        h "Yes yes... Now stop bawling. I look really stupid with that expression."
        show s dontcare
        s "Yeah well, instead of looking at my stupid face, let's watch a movie or something."
        show s laugh
        s "That way we at least have an excuse to stuff our faces with sugar."
        show h laugh
        h "Sounds good to me!"

        scene black with fade
        stop music fadeout 2.0
        play sound "audio/special.wav"
        "Thius pretend to watch a movie while working their hardest to develop a fatty liver disease."

    play music "audio/08_why.mp3" fadein 2.0
    scene home_laundryless with fade

    "The next day, other Thiu is surprised to wake up with the other half still in the house."
    show s confused at righty with dissolve
    s "....You're not going to Jerkface's today?"
    show h smilelow at lefty, faceright with dissolve
    h "Yeah, not today..."
    show h confused
    h "He said he wants to wait a week before he knows if my organs fail or something."
    show s laugh
    play sound "audio/_laugh.mp3"
    s "Alright, finally!!"
    show h unhappy
    h "Umm....?"
    show s smile
    s "We can finally hang out!"
    show h sorry
    h "....We've been hanging out every evening though?"
    show s shrug
    s "No, no! Like... I don't know. Go somewhere together!"
    show s sorry
    s "Like people do when they have friends..."
    show h smilelow
    h "Ah."
    show h smilecalm
    h "Okay..."

    if healthy == True:

        show h shruglaugh
        h "I'm just surprised you're willing to exit the house again!"
        show h smug
        h  "This is like two days in a row! I'm impressed."

    else:

        show h smilegentle
        h "I'm just surprised you're willing to exit the house..."

    show s confused
    s "I-!! I go out sometimes!"
    show s ashamed
    s "Like when I go to the store and-... go to another store."
    show s embarrassed
    s "I go to grocery stores... the pharmacy... even the gas station sometimes if everything else is closed."
    show s explain
    s "See? I go to all kinds of places."
    show h sneaky
    h "Pretty wild."
    show s doubleflip
    s "Screw you! I went to Vivian's shop too!"
    show h confused
    h "Huhhh???"
    show s nervous_smile_away
    s "And we chatted and had tea and everything."
    show s disapprove
    s "So it was almost like a date even!"
    show h sorry
    h "Okay, hold up. Who is Vivian?"
    show s confused
    s "Huh?? She's the other mage? The one with the legal store."
    show h laugh
    h "Aaaaah! Ms. Mage!!"
    show h lol
    h "When did you go see her?? I'm shocked."
    show s yeahok
    s "When I got locked out of the house."
    show h shruglaugh
    play sound "audio/_laugh.mp3"
    h "Hahahha! Okay that makes more sense."
    show s think
    s "Come to think of it she said she was interested in this spell."
    show h whatever
    h "Why'd you have to go and tell her about it?"
    show s docile
    s "I--!! Well jesus... Sorry?"
    show s sad
    s "I take that as you don't wanna go visit her."
    show h bleh
    h "I take that as you do."
    show s down
    s "....Maybe? I mean... I wanna show you off."
    show h laugh
    h "Pfffth, hahahha!! What??"
    show s thefuck
    s "I-! I have two selves!! Maybe she'll think we're cool!"
    show h lol
    play sound "audio/_laugh.mp3"
    h "HAHAHHAHAHA!!!" with hpunch
    show h mock
    h "No way she'd think that."
    show s ticked
    s "S-she might!! She might!! She's a mage!!"
    show h kindasmile
    h "Alright then, let's see."
    show s scold
    s "We'll see!!"

    hide s
    hide h
    with dissolve
    stop music fadeout 2.0
    "And so they went to see."

    play music "audio/09_doit.mp3" fadein 2.0
    scene shop with fade

    play sound "audio/enter_shop.mp3"
    show v smile at lefty, faceright with dissolve
    v "Welcome."
    show s nervous_smile at righty with moveinright
    play sound "audio/echo.mp3"
    s "Uhhh... H-HELLO!!!!" with hpunch
    show v smile_closed
    v ".........Hello hello."
    show h mock at right with moveinright
    h "So smooth. So cool."
    show s yeahright
    s "S-shut up! I'm anxious enough already..."
    show v smile
    show h smilegentle
    v "Well, it's certainly interesting to see the both of you at once."
    show s surprise
    s "YES!! Yes, that's right!"
    show s shy
    s "This is my other half and he is cool!"
    show v unimpressed
    v ".........Sure."
    show h laugh
    h "Aww, thanks. I feel so cool right now."
    show s docile
    s "....................."
    show h kindasmile
    h "Hmm?? What's up me? Did you freeze? That's not cool."
    show v smile
    v "No, no. It's cool as ice."
    show v heh
    v "Now can I get you two popsicles something specific, or are you just browsing?"
    show h smile
    h "....You don't happen to have anything that stops vomiting?"
    show v think
    v "You'd probably find something more suitable at a pharmacy..."
    show h smilelow
    h "Hmm... I'm looking for something more specific..."
    show h shruglaugh
    h "Like, let's say I ate something poisonous..."
    show v ohyeah
    v "You don't want to suppress that kind of vomit."
    v "That's how your body is trying to rid itself of the poison. So just puke."
    show h nervous
    h "Hmmm... Then how about something that makes all the poison come out at once?"
    show v unimpressed
    v ".........................."
    show v down
    v "I don't know. Get a gastric lavage?"
    show h unamused
    h "That's not a very magical solution..."
    show v impatient
    v "I don't understand why you're looking for magic when science has you covered."
    show h whatever
    h "I don't know... It seemed fitting since it's magic making me ill..."
    show v ukidding
    v "......................Oh?"
    show s sad
    s "Hey me? Can we go now...?"
    show h unhappy
    h "Not right now, I'm having a conversation."
    show s ashamed
    s "But I'm getting really anxious..."
    show h unsure
    h "Here are the keys, go home."
    show s hurt at faceright
    s "Ughhh... C-can you walk me there? Please?"
    show h miffed
    h "(Oh, for fuck's sake... What even happened?? He was fine a minute ago!)"

    menu:

        "Go home.":

            $ narcissus += 1

            show h smilelow
            h "............Alright."
            show v down
            v "You're leaving?"
            show h shruglaugh
            h "Yup! Thanks for the advice, I'll puke it all out happily next time!"
            show v think
            v "Next time..?"
            show v shock
            v "Wait, what kind of magic is making you sick?"
            show h mock at faceright
            h "Don't worry about it!"
            show v worry
            v "If someone put a curse on you I can--"
            play sound "audio/enter_shop.mp3"
            hide s
            hide h
            with moveoutright
            h "Thanks! Bye byeeee!!"
            show v ukidding
            v "........................"
            hide v with dissolve

            stop music fadeout 2.0
            "Thius leave Vivian to be all confused by herself."
            "Really cool."

            play music "audio/12_looking.mp3" fadein 2.0
            scene home_laundryless with fade

            show h argue at righty with dissolve
            h "What was that!?"
            show s bigsad at lefty, faceright
            play sound "audio/_impact.mp3"
            s "I DON'T KNOW!!" with vpunch
            show s desperate
            s "I'm so embarrassed!!"
            show h angry
            h "Well, yeah. That was rude as hell."
            show s docile
            s "Sorry!"
            show h nah
            h "It's not me you should apologize to."
            show s bigsad
            play sound "audio/echodull.mp3"
            s "Aaaaaah!!!" with hpunch
            show h unsure
            h "{i}Sighh{/i}....."
            show h shruglaugh
            h "Well whatever. It didn't sound like she could help me anyway."
            show h sneaky
            h "Or that she thought we're cool."
            show s thefuck
            play sound "audio/_increase.mp3"
            s "AAAAAAAAAAAAAAAAAAAAAAAAAAAAHHH!!" with hpunch
            show s ticked
            s "Oh my god I'm so mortified!! What was I thinking??!"
            show s desperate
            s "I must cease my existence, for I can never recover from this humiliation!"
            show h mock at faceright
            h "Yeah, yeah. That's nice honey."
            hide h with moveoutright
            show s confused
            s "W-where are you going???"
            "Thiu goes to sit on the bed. He pulls the blanket over himself."
            h "Come. We must hide from the world now."
            show s docile
            s "Huh??"
            play sound "audio/_thunk.mp3"
            h "Hurry! Before you die from shame!!" with vpunch
            show s shrug
            s "What!??!"
            hide s with dissolve
            "Other Thiu comes under the blanket as well."
            show blanket:
                xalign 0.5 yalign 0.2
            with dissolve
            h "We may never leave from under here again."
            s "....Goddammit. I wish we at least had some soda then."
            h "Okay hold up."
            hide blanket with dissolve
            "Thiu goes to grab a bottle from the fridge."
            show blanket_pop:
                xalign 0.5 yalign 0.2
            with dissolve
            h "Alright, now we're ready."
            s ".............Excellent. I guess."
            h "Now, in the safety of our cocoon..."
            hide blanket_pop
            with dissolve
            show h argue at righty
            play sound "audio/echolow.mp3"
            h "What happened??" with vpunch
            show h unhappy
            show s desperate at lefty, faceright with dissolve
            s "Ughhh..... I don't knooooow!!"
            show s embarrassed
            s "It was so awkward!!"
            show s shrug
            s "From the moment I opened my stupid mouth it was over!"
            show s tocry
            s "And then I stand there like an idiot while you chat."
            show s think
            s "Like ho hum, sure wish I had something to say!"
            show s dontcare
            s "But nooooooooooo. I'm too busy pulling my foot out of my mouth!"
            show s sad
            s "And with each passing moment the hot red shame ramps up until the whole place is on fire!!"
            show h sneaky
            h "Damn. Can't get any less cool than that."
            show s thefuck
            s "ARGHH! Shut up! I never wanna hear the word \"cool\" again!!"
            show h lol
            play sound "audio/_laugh.mp3"
            h "Hahahah!!!" with vpunch
            hide h
            hide s
            show blanket_pop:
                xalign 0.5 yalign 0.2
            with dissolve
            s "And now I'm here in the cocoon. From which I may never emerge from."
            h "But you got soda."
            s "Right."
            h "Since I just took it from the fridge, the soda is..."
            hide blanket_pop
            show h sneaky at righty
            with dissolve
            h "........{i}Cool.{/i}"
            show s embarrassed at lefty, faceright with dissolve
            s "..........Have mercy. I'm dying inside."
            show h lol
            play sound "audio/_laugh.mp3"
            h "HaHHahaHAhahAHAH!!!" with hpunch
            show s smiledown
            s ".....Stupid."
            show h kindasmile
            h "Yeah, I am. Nothing new under the sun."
            show s yeahok
            s "Or the blanket."
            show h smilelow
            h "Yes. Vivian will never be under our blanket."
            show s bigsad
            play sound "audio/_increase.mp3"
            s "Screw you Vivian! I am too cooooooooooooool for you! Aaaah!"
            show h mock
            h "Cool as a cucumber!"
            show s explain
            s "I am all of the cucumber's coolness combined!!!"
            show h explain
            play sound "audio/surprise.wav"
            h "KING OF THE CUCUMBERS, AM I??!!" with hpunch
            show s fuckyou
            play sound "audio/echolong.mp3"
            s "YES MY CUCUMBER IS THE BIGGEST IN THE UNIVERSE!!!!" with vpunch
            show h laugh
            play sound "audio/echowhip.wav"
            h "AND THE COOLEST!!" with hpunch
            show s desperate
            play sound "audio/_impact.mp3"
            s "AAAAAAAAA!!" with vpunch
            show h lol
            play sound "audio/_metal.mp3"
            h "AAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!" with hpunch
            hide h
            hide s
            with dissolve
            "The screaming and nonsense continues for the rest of the day."
            "Much to the upstairs woman's dismay..."
            stop music fadeout 2.0
            "But Thiu is not anxious anymore."

            play music "audio/10_goodlook.mp3" fadein 2.0
            scene home_laundryless_night with fade

            show s sad at righty with dissolve
            s "Ahhh... who cares if I'm a lame loser."

            if healthy == True:

                show h unamused at lefty, faceright with dissolve
                h "You're still on about that? God. Just eat your damn fish."
                show s listen
                s "I {i}am{/i} eating it!! Turns out I like fish, huh! Who'd have thought??"
                show s dontcare
                s "Now I'm going to be super healthy overnight because I ate fish!"
                show h smug
                h "Nice. Add some broccoli sprouts and we'll be immortal."
                show s sad
                s "I don't know about that but..."

            else:

                show h unamused at lefty, faceright with dissolve
                h "You're still on about that? God. Just eat your damn candy."
                show s sorry
                s "Can't believe we still have candy..."
                show s whatever
                s "We're going to die if we keep living like this..."
                show h smug
                h "Since when was I concerned about that?"
                show s sad
                s "Well... I don't know..."

            show s worry
            s "I'd at least like to live to see the season finale of Captain Backstab Origins...."
            show s disapprove
            s "So I don't know... Maybe we can fix some things up a bit."
            show h surprised
            h "....."
            show h smilegentle
            play sound "audio/Coins (2).wav"
            h "Sure. Sounds good."
            show h laugh
            h "And then let's hit the gym too and get all beefed up!"
            show h mock
            h "Maybe Vivian will then give us a second glance!"
            show s dontcare
            s "I don't need no Vivian. From now on I'll only love myself!"
            show h sorry
            h "Awww, thank you!"
            show s ticked_shy
            play sound "audio/_hiss1.ogg"
            s "I--!! You know goddamn well I meant me!!"
            show h shruglaugh
            h "And here I thought you hated me!"
            show s doubleflip_angry
            play sound "audio/_hiss2.ogg"
            s "You thought right!"
            show h sneaky
            play sound "audio/special.wav"
            h "Well I love you too!"
            show s embarrassed
            s ".......What?"
            show h puzzled
            h "In theory anyway."
            show h smile
            h "Like I have to take care of you, therefore I care about you."
            show s confused
            s "I--- wh--??"
            show h confused
            h "No wait... I guess hospitals take care of people without love."
            show h smilelow
            h "But I don't get paid to care about you so it's different."
            show s ashamed
            s "What the hell are you on about??"
            show h bleh
            h "Ahh, listen... It's complicated."
            show s thefuck
            play sound "audio/_hiss2.ogg"
            s "Arrrghh!! Forget this! Forget this whole discussion!!"
            show h lol
            h "Rude! I'm sorting out my feelings here!"
            show s fuckyou
            s "Blow them out your ass! This is why no one likes you!!"
            show h laugh
            play sound "audio/_nervousbubbles.mp3"
            h "HAH HAHA!!" with vpunch

            if narcissus > 3:

                show s ticked_shy
                s "(I can't believe my heart skipped a beat over this shit!!)"
                show s embarrassed
                s "(What's wrong with me?!)"

            hide h
            hide s
            with dissolve
            stop music fadeout 2.0
            "The Thius go to sleep."

        "Stay.":

            $ reishi = True

            show h pissed
            h "No, I'm in the middle of something."
            show s tocry
            s ".........."
            show h smilecalm
            h "This won't even take that long, just count those trinkets or something."
            show s hurt at faceright
            s "....O-okay..."
            hide s
            hide h
            hide v
            with dissolve
            "Other Thiu goes to count glass charms and cry."
            show v think at lefty, faceright
            show h smile at righty
            with dissolve
            v "...Is he okay?"
            show h laugh
            h "No. Where were we?"
            show v worry
            v "....You said it's magic that's making you sick."
            show v ukidding
            v "Are you cursed or something?"
            show h shruglaugh
            h "Haha, maybe?"
            show h nervous
            h "Because of reasons, I drank a magic potion and have been feeling kinda ill ever since."
            show v ohyeah
            v "What potion was it?"
            show h nah
            h "Well it was supposed to be a cure for aging, but god knows what it actually was..."
            show v shock
            v "...................."
            show h awkward
            h ".....Um... What? What is it?"
            show v impatient
            v "You're so lucky to be alive."
            show h confused
            play sound "audio/_thunk.mp3"
            h "HUH?!?!" with hpunch
            show v pissed
            v "Why on earth would you do that? Didn't you learn your lesson last time?"
            show h unsure
            h "I'm sorry, what???"
            show v impatient
            v "I told you!! I told you the first time you were here, do {i}not{/i} get involved with Lua!"
            show h surprised
            h "Huh? How'd you know it was him?"
            show v pissed
            v "How daft are you!?"
            show h unhappy
            h "Hey!! I owed him a favor, okay??"
            show h whatever
            h "What's it to you anyway?!"
            show v sigh
            v "...................You're right. I'm sorry."
            show v worry
            v "It's none of my business..."
            show h bleh
            h "Well-... well it doesn't really matter."
            show h nah
            h "I guess I'll just wait it out. I'm not really as sick as yesterday or anything."
            show h explain
            h "And then the next time I'll just puke faster."
            show v ukidding
            play sound "audio/echodull.mp3"
            v "\"Next time\"!?" with vpunch
            show h unamused
            h "Uhh... Because it's a work in progress?"
            show v impatient
            v "I have no words."
            show v ohyeah
            v "You're beyond help."
            show h smug
            h "Okay then! Then that was probably everything."
            show h kindasmile
            h "Y'know this is a pretty bad track record for you."
            show v think
            v "Excuse me?"
            show h sneaky
            h "I've been here twice, and both times I got disappointed."
            show v down
            v "I can't help someone who refuses to listen to my advice!"
            show h unamused
            h "Yeah yeah. At least Lua gets shit done."
            show v unimpressed
            v "Sure. If making things worse counts, then yes. He gets shit done."
            show h fuckyou
            h "Screw you."
            show h pissed
            h "C'mon me, we're leaving."
            show s hurt at right with moveinright
            s "Aughh!! Finally!"
            show v think
            v "Wait! Better Thiu!"
            show h unsure
            h "Yeah?"
            show v impatient
            v "I said \"better\"."
            show h mock at faceright
            play sound "audio/_laugh.mp3"
            h "Hahah, wow. Fuck you."
            hide h with moveoutright
            show s shrug
            s "Uhh... m-me??"
            show v smile
            v "Here. Try this."
            hide v
            hide s
            with dissolve
            "Vivian hands Thiu a bag of weird grounded muss."
            show s docile at righty with dissolve
            s "Umm.... uhh???"
            show v heh at lefty, faceright with dissolve
            v "It's tea I made with a small spell to reduce anxiety."
            show s sorry
            s "I-- for me??"
            show v gentle
            v "Yeah. I thought you'd find it useful."
            show s shy
            s "(Fuck. What do I say??? Thank you?? Just thank you?? Or that I'm happy???)"
            show s embarrassed
            s "Er... um... uhh...."
            show s shrug
            s "....C-cool?"
            show v unimpressed
            v "Oh yeah. It's pretty cool. Try it hot though."
            show v smile
            v "This one's free, but if you like it, come buy another batch!"
            show s confused
            s "Wait... Are you selling me drugs?"
            show v heh
            play sound "audio/_nervousbubbles.mp3"
            v "HAhahaha!!" with vpunch
            show v smirk
            v "No! This is a legal store! It's just enchanted reishi mushrooms."
            show s makenice
            s "Oh... Okay."
            show s nervous_smile_away
            s "I'll give them a try..."
            show v smile
            v "Yup. Let me know how that goes!"
            show s docile
            s "Y-yeah! Yeah okay!! ....And uh... Bye...."
            show v smile_closed
            v "Come again!"
            hide s
            hide v
            with dissolve
            play sound "audio/enter_shop.mp3"
            "Thiu exits the shop stumbling over his feet like he stumbled over his words."

            scene city_day with fade

            show s thefuck at lefty, faceright
            play sound "audio/_increase.mp3"
            s "(FUUUUUUUUUUUUUUUUUUUUCK!!!!!)" with vpunch
            show s ticked
            s "(Oh my god she was being so nice and I couldn't even utter out a thank you!!)"
            show s angry
            s "(Bet she hates me now!)"
            show s sorry
            s "(Though she did say come again...)"
            show h unhappy at righty with moveinright
            h "What did she want?"
            show s nervous_smile
            s "She gave me some tea to try."
            show h confused
            h "Huh. Okay?"
            show h smilegentle
            h "Well... Good job?"
            show s docile
            s "What?"
            show h laugh
            h "Good job, y'know? Wasn't this like a big thing to you? Go visit someone."
            show s smile
            play sound "audio/_nervousbubbles.mp3"
            s "T-that's right!! It was!!"
            show h smile
            h "Let's go home. You can try that tea."
            show s makenice
            s "Yeah! Let's try some."
            show h sneaky
            h "Nah, you try it. I'm good."
            show s disapprove
            s "....Huh?"
            show h bleh
            h "That Vivian's a cunt."
            show s laugh
            play sound "audio/_laugh.mp3"
            s "Pffft!! You're just upset she told you off!"
            show h unhappy
            h "Yeah, I am! What about it?"
            play sound "audio/Special (8).wav"
            show s laugh with vpunch
            s "Hahahah!!"

            scene black with fade
            stop music fadeout 2.0
            "Thiu returns to his nest and half of him drinks some mushroom tea."

    play music "audio/11_bitch.mp3" fadein 2.0
    scene shop with fade
    "The next day, Vivian is messing up her spells left and right."
    show v sigh at righty
    v "(Ahhh, focus. Focus.)"
    show v unimpressed
    v "(So Lua is working on the project again. So what?)"
    show v down
    v "(That's up to him.)"
    show v pissed
    v "(And if that half-split doofus wants to help him, so be it.)"
    show v worry
    v "(..........Even if that's exactly what I thought last time before Lacy----)"
    show v impatient
    v "(No. It's not my problem.)"
    show v pissed
    v "(Besides I bet Lua is working on the potion just to get under my skin anyway!)"
    show v ukidding
    v "(He even came around just to rub it in my face.)"
    show v unimpressed
    v "(I'm not playing his game!! I don't give a rat's ass.)"
    hide v with dissolve

    "Vivian is too frustrated to work on her spells, so she decides to clean up the store instead."
    "One swift broom sweep later, a bunch of Vivian's merchandise goes crashing onto the floor."
    "She had knocked them over by accident."
    "Yes, by accident of course. Would be pretty stupid to do it on purpose."

    show v think at righty
    v "..........................."
    hide v with dissolve

    "She stubbornly keeps cleaning for a few more hours."
    "Those spiderwebs on the ceiling? Gone."
    "Dust in the air ventilation system? Gone."
    "Several hours later the whole shop is sparkling!"
    "How satisfying!"
    "But Vivian isn't satisfied at all."
    "Try as she might, she can't clean away the mess in her head."

    show v impatient at righty with dissolve
    stop music fadeout 2.0
    v ".............Fine."

    scene city_late with fade
    play sound "audio/ding.mp3"
    "She rings Lua's door bell."
    l "Just a second!"
    play sound "audio/dingx3.mp3"
    v "......................"
    "And does it again."
    play sound "audio/ding_spam.mp3"
    "And again."
    "And again, and again, and again, and again, again...."
    play music "audio/05_iwill.mp3" fadein 2.0
    show v unimpressed at lefty, faceright
    show l angry_explain at righty
    with dissolve
    l "I heard you the first ten times, you--!!" with vpunch
    show l oh
    l "..........Oh. What are {i}you{/i} doing here?"
    show v heh
    v "I thought you said I should drop by sometime."
    show l ugh
    l "That was a lie. Goodbye."
    show l at faceright
    show v gentle
    v "So, how are the things with the potion? Good progress?"
    show l smile at faceleft
    l "Ah. I see. You've changed your mind."
    show l smilesmile
    l "But as it just so happens, I have also changed my mind, and am no longer willing to let you assist me."
    show v ohyeah
    v "I was under the impression you were working on your own."
    show v pissed
    v "But a little bird flies by and tells me you have another \"assistant\"."
    show l bored at faceright
    l "Fascinating. Goodbye."
    hide v
    hide l
    with dissolve
    "Lua attempts to close the door, but Vivian forces her way in."

    scene kitchen_late with fade

    show l angry_explain at lefty, faceright with dissolve
    l "..............So, would you like some coffee then? Hmm??"
    show v heh at righty with dissolve
    v "Thank you, I'd love some."
    hide l
    hide v
    with dissolve
    play sound "audio/echodull.mp3"
    "Lua slams the coffee pot on the table like the passive-aggressive bitch he is."
    "Half of the coffee spills over the table."
    show v think at righty
    show l complain at lefty, faceright
    with dissolve
    l "{b}Enjoy.{/b}"
    show v worry
    v "Thanks..."
    show l bored
    l "Drink. And leave."
    show v unimpressed
    v "I guess this is your way of repaying my hospitality from last time."
    show l miffed
    l "That it is."
    show v ohyeah
    v "That's fine. Are you done yet?"
    show l oh
    l ".........."
    show v down
    v "Because if you are, I'd like to talk like adults."
    show l whatever
    l "If you're here to convince me to stop my research, don't bother."
    show v unsure
    v "I'm not telling you not to work on it."
    show v ohyeah
    v "But I {i}am{/i} telling you not to hurt anyone while you're at it."
    show l playful
    l "Fear not, I'm not hurting anyone."
    show v pissed
    play sound "audio/echodull.mp3"
    v "{b}BULLSHIT!!{/b}" with vpunch
    show v impatient
    v "That guy!! The Thiu! He came over the other day! You're using him as a tester, aren't you?!"
    show l lookup
    l "He's got a big mouth, huh..."
    show v pissed
    v "So you admit it! What are you doing!? You're going to kill him!"
    show l fake_laugh
    l "Ah, who cares. There's a spare for him anyway."
    show v down
    v "That's besides the point..."
    show v ukidding
    v "Keep this up and I'm going to report you!"
    show l chuckle
    l "Then why come here to announce your intentions?"
    show l mock
    l "Oh wait. It's another one of your empty threats."
    show v think
    v "........."
    show l ugh
    l "I have enough dirt on you to bury you in it."
    show l playful
    l "So please. Go right ahead. See what happens."
    show v worry
    v "{i}Tch...{/i}"
    show l down
    l "I really don't know why you're getting involved in this."
    show l think_pleased
    l "Did you just want my attention?"
    show v impatient
    v "Up yours..."
    show l oh
    l "Was that all then?"
    show v unsure
    v "..........................."
    show l smilesmile
    l "Okay! You know your way out."
    show l mock
    l "And don't be so sad, I have good intentions you know."
    show l playful
    l "I just thought what a shame it was to come this far, just to drop our research."
    show l sheepish
    l "I'm sure poor Lacy would roll in her grave if I did."
    show v impatient
    v "Shut up."
    show l lol
    l "Hahahha! Oh, she was so dedicated to it, wasn't she?"
    show v pissed
    play sound "audio/_impact.mp3"
    v "Shut the hell up, you scum of the earth!!" with hpunch
    show l smug
    l "That's what this is all about, isn't it?"
    show l mock
    l "Your redemption arc, is that what you're after?"
    show l playful
    l "\"Oh, let me save this random suicidal lost cause, and surely dear sister forgives me.\""
    show v impatient
    v "I have not an ounce of guilt over what {i}YOU{/i} did to her!!"
    show l chuckle
    l "What did I do?? She asked to help out. She wanted to do it, do you understand?"
    show v ohyeah
    v "Of course she'd want to help you. She was in love with you!"
    show l lookup
    l "Oh, she was? I had no idea."
    show v impatient
    v "Again, with this bullshit! You knew!!"
    show v down
    v "You knew and figured, heyyy! Now here's an easy target! Let me try the poison on her!"
    show l ugh
    l "Poison? Vivian, we both know it's not poison."
    show v ukidding
    v "It {i}is{/i} poison in the state that it's in now!"
    show l complain
    l "Fine. But did you ever stop to think maybe she drank it to help you?"
    show l oh
    l "To aid your precious research. After all, this potion wasn't even my idea."
    show v pissed
    v "Don't spin this around! It's all your fault! I wasn't going to make anyone drink it until I knew it worked!"
    show l lol
    l "Except the rats."
    show v shock
    v "..................."
    show l playful
    l "Poor little critters. You're such a monster."
    show v cry
    v "I-!! I don't want to hear that from someone like you!!"
    show l pity
    l "Aww... I'm sorry. I didn't mean to hurt you."
    show v pissed
    play sound "audio/surprise.wav"
    v "And that's the biggest lie yet!!" with hpunch
    show l fake_laugh
    play sound "audio/_laugh.mp3"
    l "Hahahah!!!" with vpunch
    show v down
    stop music fadeout 2.0
    v "I'm done!"
    hide v with moveoutleft

    play music "audio/07_battle.mp3" fadein 2.0
    scene entry with fade
    show a listening at lefty, faceright with dissolve
    show v down at righty with moveinright
    a "...Huh?"
    show v shock
    v "...!"
    show a excited
    a "Oh my god, Vivian! You're here!"
    show a approve
    a "I had no idea! I would've come home sooner!"
    show v cry
    hide v with moveoutleft
    show a listening at faceleft
    a ".....???"

    scene kitchen_late with fade
    show l pleased at righty with dissolve
    show a miffed at lefty, faceright with moveinleft
    a "......What did you say to Vivian? She was crying."
    show l happy
    l "I suppose she was just that happy to see you."
    show a bored_bounce
    a "Yeah right... Why didn't you call me? I wanted to hang out with her too!"

    scene black with fade

    "Yes, mage drama. Very interesting."
    stop music fadeout 2.0
    "But it has very little to do with our hero Thiu."

    scene home_laundryless with fade
    play music "audio/03_partisan.mp3" fadein 2.0
    "Thiu has spent the last several days playing video games."

    show s angry at righty with dissolve
    s "Oh my god! Again!"
    show s thefuck
    s "How do you keep finding me so fast!? You're looking at my screen!!"
    show h laugh at lefty, faceright with dissolve
    h "Hahaha! I am not! You just suck at this game."
    show s listen
    s "No, you're looking at my half of the screen!!"
    show h explain
    h "Nope! You just suuuuuck."
    show s scold
    s "NO!! You're looking at my screen! And guess how I know that?"
    show h smilegentle
    h "Yeah?"
    show s yeahright
    s "Because I'm looking at your screen..."
    show h lol
    play sound "audio/_laugh.mp3"
    h "HAHAHAHHAHA!!" with vpunch
    show h kindasmile
    h "Well maybe you're the one who got all of our cheating attributes."
    show s doubleflip
    s "Yeah, right. Go wait in the bathroom while I hide my character!"
    show h nah
    h "Aaaah, that's a hassle. Let's just play something else."
    show s scold
    s "Ooooh yeah! Now you wanna switch, what a coincidence!"
    show h smug
    h "No one likes a sore loser y'know?"
    show s disapprove
    s "No one likes a cheater either!"
    show h sneaky
    h "Which, by they way, you just admitted to being. You sore cheating loser."
    show s yeahok
    s "..........Damnit. You're right."
    show h lol
    play sound "audio/_laugh.mp3"
    h "Hhahaha!!"
    show s laugh
    play sound "audio/_nervousbubbles.mp3"
    s "HAH HAHAH!!" with vpunch
    hide h
    hide s
    with dissolve
    "There is nothing particularly funny about any of this."
    "But the Thius are laughing like maniacs."
    "If this was a group of friends, Thiu would be the one constantly cracking jokes to make the others laugh."
    "But everyone would just laugh to be polite. No one would think he is funny."
    "And then he would go at it all day long, blissfully ignorant of how annoying he is being."
    "Then Thiu would not be invited to hang out again."
    "But since there are only Thius here now, he is having the time of his life."

    if narcissus > 3:
        #undone
        show h smile at lefty, faceright with dissolve
        h "Alright, what do you want to play next?"
        show h explain
        h "I'm sick of playing this dumb game that you suck at cheating."
        show s sad at righty with dissolve
        s "........."
        hide s
        hide h
        with dissolve
        stop music fadeout 2.0
        "But other Thiu is deep in thought."
        show h sorry at lefty, faceright with dissolve
        h "Me??"
        play music "audio/01_rideout.mp3" fadein 2.0
        show s nervous_smile at righty with dissolve
        s "Huh?? Yeah, yeah. Whatever."
        show h mock
        h "Oookay. Well if it's whatever I'll go with--"
        show s sad
        s "Hey me? I have a question..."
        show h smile
        h "...Sure?"
        show s nervous_smile_away
        s "Y'know on the first day after we got split...."
        show s shy
        s "You, uhh... kept suggesting something..."
        show h confused
        h "What..? Something???"
        show s ticked_shy
        s "........Y'know. {i}Something.{/i}"
        show h laugh
        play sound "audio/_nervousbubbles.mp3"
        h "{b}Ohhh!!{/b} You mean the sex!"
        show h lol
        h "Yeah, don't worry about that! Hahah!!"
        show s embarrassed
        s "I'm not worried... I'm just wondering if that offer is still on the table."
        show h sorry
        h "....................Huh?"
        show s nervous_smile
        s "I-I-I mean!! You were joking then, right?"
        show h unsure
        h "Well, no... That was different..."
        show h nah
        h "I mean there was an opportunity to establish our relationship as such, but now..."
        show h unamused
        h "Now it'd just be weird."
        show s hurt
        s "Oh... Yeah... Right."
        show h whatever
        h "..........."
        show s down
        s "..........."
        show s bigsad
        play sound "audio/_impact.mp3"
        s "{b}You think I'm ugly!!!{/b}" with vpunch
        show h bleh
        h "{i}Groaaaaaaaaan!!{/i}"
        show h argue
        h "YES! But that's not it!"
        show s desperate
        s "I knew it!! I always thought I'm ugly too!!"
        show h explain
        h "I know! But listen!"
        show h smug
        show s tocry
        h "Back then it was like, duhh, it's masturbating, right?"
        show s disapprove
        s "It still is, isn't it?"
        show h confused
        h "Well... Yes, but no, but..."
        show h mock
        h "Now there's, like, all this extra package, like... Y'know?"
        show s confused
        s "I don't."
        show h smileguilty
        h "Like you're almost like someone else now, y'know?"
        show s ashamed
        s "So?"
        show h puzzled
        h "Ahhhh. You don't understand!"
        show h sorry
        h "Like... After we split, I didn't think of you as anything!"
        show s embarrassed
        s "..............................."
        show h nah
        h "I thought you're just an extension of my hand or something."
        show h shruglaugh
        h "Something that got cut off like a lump of cancer, y'know?"
        show s ticked
        s "Oh my god..."
        show h sneaky
        h "Except this lump still moves around and has a warm hole! I could fuck it before killing it, y'know?"
        play sound "audio/_impact.mp3"
        show s thefuck
        s "OH MY FUCKING GOD!!" with hpunch
        show h confused
        h "But now you're like... a real person with feelings and stuff."
        show s bigsad
        play sound "audio/isbad.mp3"
        s "Am I just a tumor to you!?" with vpunch
        show h unhappy
        h "No! And that's the problem here!!"
        show s yeahright
        s "I can't believe my ears!"
        show h unamused
        h "Like now I have to consider do I want to have sex with someone like you?"
        show s doubleflip_angry
        s "Hooooooly fucking shit! I always knew you're awful, but this takes the cake!!"
        show h angry
        h "Hey, let's not pretend like you're not me!"
        show h fuckyou
        h "If you got to be the happy half, you'd have had the same exact thoughts!"
        show s ticked
        s "I can't believe myself! I'm the worst!!"
        play sound "audio/_laugh.mp3"
        show h laugh
        h "HAhaHAHAH!!" with hpunch
        show h sorry
        show s angry at faceright
        h "Where are you going?"
        show s scold at faceleft
        s "I can't handle stupid of this magnitude!!"
        show h puzzled
        h "No, no, wait! I'm sorry!"
        show h nervous
        h "Don't be like that, me!"
        show h awkward
        h "Why are you so mad about this??"
        show h bleh
        h "Look, it's fine! I'll screw you if it keeps you from slitting your wrist?"
        show s thefuck
        play sound "audio/_hiss2.ogg"
        s "{b}Oh my god, no!!{/b}" with vpunch
        show s fuckyou
        s "You don't get it at all!!"
        show s ticked
        s "God!! You're so stupid and horrible!!"
        show h fuckyou
        play sound "audio/_hiss1.ogg"
        h "I AM!! Just like you!"
        show s thefuck
        s "You're supposed to understand me! You're me for christ's sake!!"
        show h argue
        h "But I don't understand! You need to spell it out for me!"
        show s bigsad
        play sound "audio/echo.mp3"
        s "I CAN'T, OKAY?!" with hpunch
        show h puzzled
        h "........"
        show s docile
        s "Aaaaah, I don't--! I don't understand either!"
        show h sorry
        h "O-kaaay...?"
        show s ashamed
        s "Ugh, I don't know... It's just lonely."
        show s sad
        s "I miss you... I think."
        show h nah
        h "Okay, but I'm right here though?"
        show s disapprove
        s "Yeah, you sure are! You genius."
        show h angry
        h "Hey screw you! You're the one having another goddamn meltdown."
        show h argue
        h "What am I supposed to do?? I've tried everything! You're never happy!"
        show s explain
        s "Bullshit, I'm happy right now!"
        show h whatever
        h "Well jesus... Could've fooled me."
        show s doubleflip
        s "I can be happy and sad and lonely and mad at the same time!"
        show h unsure
        h "If you say so..."
        show s sad
        s "{i}Sighh.....{/i}"
        show h sorry
        h "How about this..?"
        show h awkward
        h "Let's merge back."
        show s confused
        s ".............Huh?"
        show h smileguilty
        h "I mean that's probably why you're lonely anyway."
        show h shruglaugh
        h "I wanted to merge back after you're a little less.... um... well, less shit."
        show h unsure
        h "But it's probably fine now too."
        show h smile
        h "So how about it? Let's be just one person again, okay?"
        show s listen
        s "......................................Absolutely not."
        show h confused
        play sound "audio/echo.mp3"
        h "HUHHH?!" with hpunch
        show s explain
        s "Look at me! I'm a bloody wreck!"
        show s ticked
        s "Who's gonna stick around if not you!?"
        show s ticked_shy
        s "I--- you should-...."
        show s docile
        s "Y-you should be my boyfriend..!"
        show h surprised
        h "........."
        show h shruglaugh
        h "....Bwahah!"
        show h laugh
        play sound "audio/_nervousbubbles.mp3"
        h "HAH HAHAHA HAHA HA!!!" with vpunch
        show h lol
        play sound "audio/_laugh.mp3"
        h "HAHAH AHA HAAHHAHA HAHAH HAHAHAH!!" with hpunch
        show s ashamed
        s "W-what's funny?"
        show h laugh
        h "Dating yourself!!"
        show h lol
        play sound "audio/_nervousbubbles.mp3"
        h "Oh my god, HAHAHA!!" with vpunch
        show h shruglaugh
        h "That's so pathetic!"
        show h laugh
        h "Heehehe!! Oooh, I can't breath!! HAhhaha!!"
        show s scold
        s "Oh yeah??"
        show s doubleflip_angry
        play sound "audio/_metal.mp3"
        s "Well screw you! {b}Die{/b}!!" with vpunch
        show s embarrassed
        s "I'm out of here!"
        hide s
        hide h
        with dissolve
        play sound "audio/doorslam.mp3"
        "Thiu storms out of the house."
        show h laugh at lefty, faceright with dissolve
        h "Oh man, heh hehee!"
        h "............."
        show h puzzled
        h "...Maaaan. Now what??"
        show h unhappy
        h "(He wants a romance, are you kidding me??)"

        menu:

            "Think about it.":

                $ narcissus += 1

                show h unamused
                h "(Ahhhh, what the crap...)"
                show h pissed
                h "(What is wrong with him?)"
                show h bleh
                h "(Who wants to date themselves?)"
                show h unhappy
                h "(I don't!)"
                show h unsure
                h "(..........Or do I?)"
                show h confused
                h "(I mean obviously he does, so I do. But...??)"
                show h puzzled
                h "??????????????????????????????"
                hide h with dissolve
                "Unfortunately Thiu.exe has stopped responding."
                stop music fadeout 2.0
                "Nothing more to see here."

            "Don't even think about it.":

                show h bleh
                h "(This is beyond stupid.)"
                show h pissed
                h "(I won't waste another minute thinking about dumb crap like this.)"
                hide h with dissolve
                "That's what Thiu told himself."
                stop music fadeout 2.0
                "And then proceeded to waste time thinking about dumb crap like that anyway."

        play music "audio/02_outof.mp3" fadein 2.0
        scene city_day with fade

        show s angry at center, faceright with dissolve
        s "(Oh my god, I'm such an idiot!)"
        show s ticked
        s "(The other me, that is!!)"
        show s explain
        s "(What kind of ass backwards logic is that!?!?)"
        show s bitetongue
        play sound "audio/_hiss2.ogg"
        s "(I'M NOT A CANCER!!)" with vpunch

        scene shop with fade
        play sound "audio/enter_shop.mp3"

        show v down at lefty, faceright with dissolve
        v "Welcome."
        show s think at righty with moveinright
        s "Hello, I'm back and I'm not cool at all!"
        show v ohyeah
        v ".....Yeah?"
        show v smile
        v "Well being cool isn't everything. Don't worry about it."
        show s confused
        s ".....Wh-.. Huh??"
        show v unimpressed
        v "I mean you look pretty upset over it."
        show s ticked_shy
        s "Ugh, it's not about that."
        show s desperate
        s "I just got dumped!"
        show v smirk
        v "For being uncool?"
        show s scold
        s "Arghh! No!!"
        show s think
        s "I don't get it! Honestly. The other me..."
        show s yeahright
        s "Everything is all fine and dandy when he wants to screw!"
        show s thefuck
        s "But when I do, suddenly it's a crisis!"
        show v down
        v "..........I really must insist on this great therapist..."
        show s dontcare
        s "No. I just needed to get out the house."
        show s sad
        s "...But I really don't have anywhere else to go so.... Hello."
        show v impatient
        v "That better not be you asking to stay the night."
        show s docile
        s "I--? N-no! Or I don't think so??"
        show v unimpressed
        v "Which one are you anyway?"
        show s makenice
        s "Huh?"
        show v ohyeah
        v "The one who can't use a phone?"
        show s yeahok
        s "...I'd be hard pressed to call your clunky hunk-a-junk a phone."
        show v heh
        v "Alright, it's you. The sad one."
        show s ohwell
        s "Can't you tell just by looking?"
        show v think
        v "I don't know. Neither of you struck me as that happy..."
        show s think
        s "...........{i}Sigh.{/i}"
        show v smile
        v "...Want some tea?"
        show s sorry
        s "Sure..."

        hide s
        hide v
        with dissolve
        "Tea is had. It's really awkward."
        "Thiu would certainly be having a panic attack if he was aware of just how awkward this all is."
        "But luckily he is preoccupied with thinking about being rejected. By himself."
        "Now there's a loser it I ever saw one."

        show v unsure at lefty, faceright with dissolve
        v "So..."
        show v down
        v "You guys still working with Jerkface?"
        show s explain at righty with dissolve
        s "I guess other me is..."
        show v ukidding
        v "I was just thinking about what you told me the other week."
        show v ohyeah
        v "That since you didn't write a contract, Jerkface keeps changing the terms."
        show s docile
        s "Yeah, why?"
        show v smirk
        v "I'm just saying there {i}is no contract.{/i}"
        show s sorry
        s "............"
        show v heh
        v "Meaning you're obligated to do fuck-all."
        show s sad
        s "Well... I mean yeah but..."
        s "Lua doesn't see it that way...."
        show v ohyeah
        v "What is he going to do? Sue you? For not paying for his illegal magic?"
        show v unimpressed
        v "If anything, it looks like he cursed you, rather than you bought a spell from him."
        show s dontcare
        s "Ahhh.... I don't know...."
        show v impatient
        v "{i}Tch.{/i}"
        show s confused
        s "W-what??"
        show v pissed
        play sound "audio/_impact.mp3"
        v "Look, you spineless little--!" with vpunch
        show s surprise
        s "......"
        show v worry
        v "No. Sorry. Disregard that."
        show s docile
        s ".........Okay..."
        hide v
        hide s
        with dissolve
        "Thiu will never, ever disregard that."
        "The word \"spineless\" is now forever engraved in Thiu's heart."
        "Moving on."

        show v sigh at lefty, faceright with dissolve
        v "Look... The other you is going to end up dead at this rate."
        show v worry
        v "It's not even a matter of if, but when. Because that potion is years away from working."
        show v ohyeah
        v "And while you might think it's easier to just let Lua do whatever..."
        show v down
        v "The other you might feel a little differently."
        show v gentle
        v "So just relay to him what I said, okay?"
        show s sad at righty with dissolve
        s "Yeah... Okay..."
        show s sorry
        s "Thank you?"
        show v heh
        v "You're welcome."
        show v think
        v "Now if only you'd take my advice this time..."
        show s ohwell
        s "............Is this like a territory thing?"
        show v unimpressed
        v "Is it a what now?"
        show s nervous_smile
        s "Between you and Lua. Since you're both running magic shops."
        show s shrug
        s "Are you just competing for customers, or why the animosity?"
        show v pissed
        v ".........I'm sorry? How is that any of your business?"
        show s bitetongue
        s "Well... You're all up in my business too..."
        show v heh
        v "I can sit back and let you get yourself killed too, if you prefer."
        show s nervous_smile
        s "Ah, no no! Sorry!"
        show v ukidding
        v "Besides, how can I not be all up in your business, when you barge in here spouting all about it?"
        show v think
        v "Including your bizarre sex life. Or lack thereof."
        show s ticked_shy
        s "A-Alright!! Alright, okay! You've made your point."
        show s ashamed
        s ".....And sorry. I'm sorry...."
        show v smile_closed
        v "Don't worry about it. I've heard worse."
        show v gentle
        v "Want some more tea?"
        show s smile
        stop music fadeout 2.0
        s "..........Yes."

        play music "audio/09_doit.mp3" fadein 2.0
        scene city_day with fade

        "While Thiu is busy sipping tea and planning how to escape his past mistakes,"
        "...other Thiu is busy coming up with new mistakes."
        show h pissed at center, faceright with dissolve
        h "(Okay what the crap am I supposed to do now??)"
        show h unhappy
        h "(Other me doesn't want to merge back anymore!)"
        show h unwell
        h "(How did that happen!? I thought that was the goal all along!)"
        show h bleh
        h "(I mean... I never told him that's the goal, but shouldn't he have known? Being me and all?)"
        show h puzzled
        h "(....Do {i}I{/i} want to merge back?)"
        show h unhappy
        h "(Or maybe I should be asking do I want to date myself?)"
        show h laugh
        play sound "audio/_nervousbubbles.mp3"
        h "..............pfft. HAhahahha!!"
        show h smilelow
        h "(Who needs to even think about something like that??)"
        show h miffed
        h "(Me.)"
        show h pissed
        h "(I need to think about that, stop laughing you jackass!)"
        show h unsure
        h "(Aaaaaah, I don't know. I mean I'm kinda awful and not someone I'd want to date...)"
        show h unamused
        h "(But it's not like anyone else is going to want to date me either.)"
        show h whatever
        h "(Plus at least we'd agree on everything...)"
        show h argue
        h "(No wait. I don't think we've agreed on anything though!? What the hell.)"
        show h laugh
        h "(But I don't know. I think I'm kinda great too.)"
        show h smilelow
        h "(Or at least I wouldn't be ruining anyone else's life.)"
        show h mock
        h "(And we can play games together. And have the same kinks I guess.)"
        show h unamused
        h "(Aaaaah, but I'm kinda not attractive at all...)"
        show h whatever
        h "(But it's not like I'm shallow or anything either so-???)"
        show h bleh
        h "(Okay fine, I'm fucking shallow but whatever. Other me seems he'd settle for me just fine!)"
        show h miffed
        h "(Goddamn this isn't going anywhere. I don't know what I want at all.)"
        show h nah
        h "(I need a sign!)"
        show h laugh
        h "(Yes, a sign that I can interpret to be whatever my subconscious conjures up!)"
        show h unamused
        h "(Because heaven forbid I make my own decisions.)"
        show h kindasmile
        h "(No, that would mean I have agency over my own life.)"
        show h miffed
        h "(And {i}that{/i} would mean I'm responsible for my own decisions.)"
        show h bleh
        h "(And {i}THAT{/i} means everything I do matters, and I much prefer nihilism.)"
        show h laugh
        h "(So a sign it is!)"
        show h confused
        h "(But where can I get a good sign...)"
        hide h with dissolve

        "Thiu's gaze lands on a bulk vending machine."
        "You know the things. The little vending machines for gumballs, candy, and trinkets."
        "The bouncy ball one is almost empty for some reason... But the toy capsule one looks promising."

        show h smilelow at center, faceright with dissolve
        h "(Alright this is it then.)"
        show h sneaky
        h "(My future costs a couple quarters.)"
        hide h with dissolve
        "Thiu puts a coin in the slot along with his fate."
        "And out comes...................."

        if narcissus == 6:

            $ together = True

            play sound "audio/special.wav"
            show ring:
                xalign 0.5 yalign 0.2
            with dissolve
            play sound "audio/echolong.mp3"
            h "(A RING, {b}ARE YOU KIDDING ME?!{/b})" with vpunch
            "Thiu tries to come up with several interpretations, but is unable to."
            "The vending machine gods have spoken."
            hide ring
            show h mock at center, faceright
            with dissolve
            h "(Okay fine. Whatever.)"
            show h shruglaugh
            h "(I always loved myself anyway!)"
            show h whatever
            h "(Except all those times when I didn't.)"
            show h laugh
            h "(But no matter! Clearly we're meant to be together!)"
            show h shruglaugh
            h "(...Probably as a whole person, but hey.)"
            show h sneaky
            h "(I'll never be lonely again!)"
            hide h with dissolve

        else:

            play sound "audio/Special (8).wav"
            show hand:
                xalign 0.5 yalign 0.2
            with dissolve
            "...One of them... sticky hand stretchy toys."
            "......Yaaaay?"
            h "(Huh... The heck does this mean?)"
            menu:

                "A hand shake.":

                    hide hand
                    show h confused at center, faceright
                    with dissolve
                    h "(Hmmm, a hand shake is like... it's like a formal meeting type of thing.)"
                    show h puzzled
                    h "(So I should have a business relationship with the other me..?)"
                    show h kindasmile
                    h "(Or maybe it's a hand shake after an argument. \"Let's be friends again.\")"
                    show h laugh
                    h "(Or better yet, it's a sign of agreement!)"
                    show h shruglaugh
                    h "(Okay okay, we should work together and agree to merge back!)"
                    show h sneaky
                    h "(Perfect!! That's exactly what I want.)"
                    show h laugh
                    h "(Thank you vending machine gods! I have seen the light!!)"
                    hide h with dissolve

                "A hand job.":

                    hide hand
                    show h confused at center, faceright
                    with dissolve
                    h "(So.... I need to jack off?)"
                    show h unsure
                    h "(But like... alone or with myself?)"
                    show h unwell
                    h "(This is too ambiguous. What a lousy sign.)"
                    show h smile
                    h "(Actually, maybe it's not the fact that this toy is shaped like a hand...)"
                    show h laugh
                    h "(Maybe it's more about how stretchy it is!)"
                    show h lol
                    h "(And then that would mean that my patience has been stretched thin.)"
                    show h unhappy
                    h "(Yeah, it has, hasn't it?? I've worked so hard.)"
                    show h unamused
                    h "(I've been babying the other me long enough, and now he springs this completely unreasonable expectation on me?)"
                    show h pissed
                    h "(Screw that. I'm not doing that!)"
                    show h bleh
                    h "(We're merging back whether he likes it or not!)"
                    hide h with dissolve

                "A hand in marriage.":

                    if narcissus > 4:

                        $ together = True

                        hide hand
                        show h confused at center, faceright
                        with dissolve
                        h "(I'm.... getting married I guess.)"
                        show h awkward
                        h "(To myself.)"
                        show h smilegentle
                        h "(Me and myself together forever.)"
                        show h unhappy
                        h "(...................Goddamit.)"
                        show h smileguilty
                        h "(Though somehow I guess I'm a little happy too.....)"
                        show h shruglaugh
                        h "(I mean I'm a safe bet, right? I know me pretty well and all.)"
                        show h smilelow
                        h "(And there is this sense of belonging, if nothing else.)"
                        hide h with dissolve

                    else:

                        hide hand
                        show h unamused at center, faceright
                        with dissolve
                        h "(Nah, I don't know.)"
                        show h miffed
                        h "(I mean this toy is all stretchy and nasty, and what are you even supposed to do with this?)"
                        show h whatever
                        h "(Slap your friends?)"
                        show h kindasmile
                        h "(I think this is a sign that if I start a romance with myself, we'll fight a lot.)"
                        show h lol
                        h "(And lots of bitch slaps will ensue.)"
                        show h sneaky
                        h "(Yeah, I'll go with that. That's what this sign was.)"
                        show h shruglaugh
                        h "(Sorry self, no romance for us! Hahahah!!)"
                        hide h with dissolve

        "Thiu returns home to find the other one waiting by the door."
        show s scold at righty with dissolve
        show h laugh at lefty, faceright with moveinleft
        h "Ohhh!! Crap!! I didn't figure you'd be back so soon! Hahahah!!"
        show s explain
        s "Yeah. I should've taken the keys..."
        show h smug
        h "See? This is what happens when you keep running away crying!"
        show s angry
        s "Just open the damn door! And I wasn't even crying!!"
        show h sneaky
        stop music fadeout 2.0
        h "Oh yeah, sure you weren't."
        hide h
        hide s
        with dissolve

    else:

        show h smile at lefty, faceright with dissolve
        h "Anyway, my horrible self. How was the tea?"
        show s smile at righty with dissolve
        s "Great! I think it's working, actually."
        show s sorry
        s "Like... I was panicking over something stupid earlier."
        show s nervous_smile
        s "But then I drank the tea and was like, huh, maybe it doesn't matter if the neighbors think my door is ugly."
        show h smug
        h "What do you mean? That's the only thing that matters in life!!"
        show h sneaky
        h "Especially since we have no control over it!"
        show s shy
        s "...Do you think I should go thank her?"
        show h smilelow
        h "I suppose."
        show s think
        s "I mean she went out of her way to make me this blend..."
        show h smile
        h "I suppose."
        show s sad
        s "So... I mean I have to go buy more anyway..."
        show h smilecalm
        h "I suppose."
        show s scold
        s "You suppose and suppose! Can't you see I'm trying to make you tell me to go!!"
        show h smug
        h "I suppo--"
        show s thefuck
        play sound "audio/echo.mp3"
        s "AAAHH!! Fine! Fine I'll go! I don't even need your approval anyway!" with vpunch
        show h laugh
        h "I-"
        show s yeahright
        s "SUPPOSE that my own approval is your approval anyway, good bye!"
        show h explain
        h "Okay but what the hell am I supposed to approve here?"
        show s docile
        s "..................."
        show s sorry
        s "That... I don't even know."
        show s confused
        s "Aren't you like the main Thiu?"
        show h confused
        h "I am??"
        show s sad
        s "Yeah. So I can't just go around doing whatever I want with your life."
        show h nah
        h "Hooold up. Hold up."
        show h unhappy
        h "{i}I'm{/i} the main Thiu??"
        show h bleh
        h "No matter how you slice it, you have more of the qualities I'd consider to be The Thiu."
        show s dontcare
        s "Really? Like what?"
        show h smilelow
        h "Uhh... Misery?"
        show s embarrassed
        s "God! Thiu is more than my misery! Thiu was the person who existed {i}before{/i} the misery came along!"
        show s sad
        s "I'm just a disease or something."
        show h miffed
        h "No."
        show s listen
        s "Explain."
        show h sneaky
        h "No."
        show s explain
        s "Well aren't you helpful today..."
        show h nah
        h "I don't know how exactly, but your logic is crap."
        show h mock
        h "Actually the whole \"Main Thiu\" concept is a load of crap."
        show h unhappy
        h "I can't believe you had such a crappy thought..."
        show s hurt
        s "..........Yeah I'm pretty crappy!! That's why you wanted to get rid of me, wasn't it!?"
        show h nervous
        h "Ooooh my god, okay let's not go there."
        show h smile
        h "How about you go get some more magic tea?"
        show s ashamed
        s "....................Fine."
        show h sneaky
        h "Actually..... I take that back, let's go there."
        show s docile
        s "Huh??"
        show h puzzled
        h "I think we're doing pretty okay lately, aren't we?"
        show s think
        s "...........I--.... Compared to what??"
        show h smilecalm
        h "Before we split."
        show s down
        s "I'd say it's about the same, really."
        show h shruglaugh
        h "Yeah! Think about that."
        show h smile
        h "Your depression is back to being just about the same."
        show h explain
        h "Even though all the happiness was given to me, and you hit rock bottom."
        show h smile
        h "So wouldn't that mean if we merge back now, we'd be way better off?"
        show s sorry
        s ".................................."
        show s sad
        s "...But..."
        show s disapprove
        s "It's not like you {i}want{/i} to merge back..."
        show h sneaky
        h "Maybe I do, maybe I don't."
        show s yeahright
        s "Ugh. What a cop-out of an answer..."
        show s whatever
        s "I'm going to buy some tea..."
        show h shruglaugh
        h "Good luck! You can do it! You're so brave!"
        show s thefuck
        play sound "audio/_hiss2.ogg"
        s "Arghhh!! Condescending!! So condescending!!"
        show h laugh
        h "Hahaha!!"
        show h smug
        h "Godspeed! Main Thiu!"
        show s worry
        stop music fadeout 2.0
        s "...I'm not."

        play music "audio/12_looking.mp3" fadein 2.0
        scene city_day with fade

        show s worry at center, faceright with dissolve
        s "I'm not the main Thiu... right?"
        hide s with dissolve

        menu:

            "I'm main Thiu.":

                show s think at center, faceright with dissolve
                s "I guess by the amount of baggage, I'd be more Thiu than other me."
                show s ohwell
                s "Since if he only carries my happy pieces, he'd be way smaller than me."
                show s sad
                s "So if it's about which one of us has more essence or something, it'd be me..."
                show s sorry
                s "But man... I don't want to be the main Thiu..."
                show s hurt
                s "I don't want The Thiu to be someone like me..."

            "He is main Thiu.":

                show s whatever at center, faceright with dissolve
                s "No, he is definitely the main one."
                show s docile
                s "I used to be happy once. Before life happened."
                show s down
                s "And I remember I was much more like the other me."
                show s yeahright
                s "And all this crap I drag around in this half of the soul is just... junk."
                show s bitetongue
                s "I'm just some personification of Thiu's sickness."
                show s stopcrying
                s "............................"

            "Neither or both are.":

                show s explain at center, faceright with dissolve
                s "The existence of \"The Thiu\" ended the second we got split up."
                show s whatever
                s "So either we're both him, or neither of us is."
                show s dontcare
                s "This isn't even something worth thinking about."
                show s ashamed
                s "Yeah... That sounds about right..."

        show s docile
        s "But I guess it doesn't really matter anyway..."
        show s down
        s "I want to merge back."
        show s sad
        s "Then everything will make sense again..."

        scene shop with fade
        play sound "audio/enter_shop.mp3"
        show v smile_closed at lefty, faceright with dissolve
        v "Welcome."
        show s makenice at righty with moveinright
        s "H-hi!"
        show v gentle
        v "Didn't expect you back so soon."
        show s nervous_smile_away
        s "Ahahah... Yeaaah. I have no life so..."
        show v think
        v "....Okay?"
        show s ticked
        s "(Crap. Maybe announcing my loser status isn't a great conversation starter....)"
        show s nervous_smile
        s "Um... I tried the tea! It's was yes thanks!"
        show v unimpressed
        v "...I'm sorry, what?"
        show s ashamed
        s ".....It-... Yes, it was good. Thanks for asking..."
        show v ohyeah
        v "I didn't ask, but okay."
        show v heh
        v "Glad to hear it."
        show s down
        s "...........Mmmmyup."
        show v pleased
        v "So, I guess you're here to buy some more?"
        show s whatever
        s "(I wasn't. But I guess I am now....)"
        show s nervous_smile
        s "Y-yeah! That's right..."
        show v smile_closed
        v "Here you go."
        show s smiledown
        s "Thanks!"
        show v unsure
        v "By the way, can I ask you something?"
        show s confused
        s "Yes?"
        show v think
        v "Why is the other you agreeing to drink poison?"
        show s ohwell
        s "Oh, that... It's how we pay Jerkface for splitting us up."
        show v ukidding
        v "Okay but why?"
        show s listen
        s "....What do you mean why?"
        show v down
        v "You told me the other week that there was no written contract."
        show v ohyeah
        v "So why pay him anything?"
        show s docile
        s "Wait... I can do that? Just not pay??"
        show v ukidding
        v "Yeah, he can't prove you owe him anything."
        show v unimpressed
        v "Much like you can't prove he screwed you over."
        show v impatient
        v "So why are you paying him for screwing you over?"
        show s ticked_shy
        "Suddenly Thiu feels really, really dumb."
        show s worry
        s ".....Why {i}am{/i} I paying him?"
        show s explain
        s "Screw that guy! I don't owe him squat!!"
        show v smirk
        v "Exactly. He is nothing but trouble."
        show s dontcare
        s "If anything, he's the one who should undo this stupid spell!"
        show s thefuck
        play sound "audio/_hiss1.ogg"
        s "How do I sue this guy!? I should report him somewhere!!"
        show v shock
        v "Err... well... Maybe don't go that far..."
        show s confused
        s "Huh??"
        show v think
        v "I-- it's..."
        show v smile_closed
        v "I-I mean that costs a lot of money, doesn't it? Suing."
        show s down
        s "....Ugh. You're right."
        show s sad
        s "I wouldn't even know how to get the whole process started..."
        show v unsure
        v "(Oh, thank fuck...)"
        show v gentle
        v "Well. Don't you worry. I can try to help you undo the spell."
        show s docile
        s "I thought you knew nothing about banned magic?"
        show v smile
        v "........................Don't worry about that."
        show v heh
        v "Just stay away from Lua. I can figure out one half-assed spell like this."
        show s dontcare
        s "Double assed."
        show v ukidding
        v "....What?"
        show s laugh
        s "My ass got split in half, so now I have two asses!"
        show v unimpressed
        v "................"
        show s nervous_smile
        s "It was a double assing spell."
        show v ohyeah
        v "..............................Okay."
        show s explain
        s "Ah, screw you! Other me thinks I'm funny!!"
        show v think
        v "It just didn't make much sense, that's all."
        show s makenice
        s "Well... I'll tell other me what we talked about."
        show v smile
        v "Good. I'll start looking into lifting the spell."
        show s nervous_smile_away
        s "Thank you! And... I guess... Bye bye?"
        show v heh
        v "Bye bye."
        play sound "audio/enter_shop.mp3"

        hide v
        hide s
        with dissolve
        "Thiu leaves the store happy."
        "Sure he made an ass out of himself yet again."
        stop music fadeout 2.0
        "But at this point he has done it so many times, it doesn't really matter anymore."

    play music "audio/13_where.mp3" fadein 2.0
    play sound "audio/opendoor.mp3"
    scene home_clean with fade

    show s docile at lefty, faceright with dissolve
    s "............Was it always this clean in here?"
    show h smile at righty with dissolve
    h "Oh yeah, I took the trash out."

    if together == True:

        show h smilegentle
        h "Speaking of which, I'll take you out too!"
        show s fuckyou
        s "Oh yeah, you wanna fight?!"
        show h unhappy
        h "?????"
        show s scold
        s "I'd consider our last one my win so--"
        show h argue
        play sound "audio/surprise.wav"
        h "Argh, no! {b}No, stupid!!{/b}" with vpunch
        show h bleh
        h "I meant out on a date!! For fuck's sake..."
        show s confused
        s "............Oh."
        show s embarrassed
        s "O-oh?!"
        show h whatever
        h "I guess this is about as romantic as it gets around here, huh?"
        show h unhappy
        h "Is this the rest of my life then?"
        show s shy
        s "Ahahah...."
        show h kindasmile
        h "Well? Is it?"
        show h smilelow
        h "I mean I'm fine if it is. So is it?"
        play sound "audio/Special & Powerup (23).wav"
        hide s
        hide h
        show hug at center with hpunch
        s "AWWW YES!!"
        s "Yeah, it is!!"
        h "Alright then? Our happy never after."
        play sound "audio/_nervousbubbles.mp3"
        s "Hehee!!" with vpunch
        hide hug
        show s smiledown at lefty, faceright
        show h sneaky at righty
        with dissolve
        h "So what happens now?"
        show s smile
        s "Now I'm going to talk about Vivian!"
        show h nah
        h "..................Ooookay."

    else:

        show s makenice
        s "Oh... Thanks?"
        show s smile
        s "It looks all nice now. Our room."
        show h unamused
        h "Yeah, well I hope it stays that way."
        show s yeahok
        s "....Kinda sounds like you're blaming me."
        show h kindasmile
        h "\"Kinda\"? I {i}am{/i} blaming you."
        show s explain
        s "Blame away, I'm also blaming you for something!"
        show h whatever
        h "And that is?"
        show s fuckyou
        play sound "audio/echolong.mp3"
        s "You're wasting our life force by drinking poison for no reason!!" with vpunch
        show s listen
        s "Vivian said so!"

    show s worry
    s "She told me, that since there's no written contract, Lua can't really demand we pay him anything."
    show s makenice
    s "So... You don't need to eat poison anymore."
    show s scold
    s "And frankly, you fucking idiot! Why'd you do it in the first place!?"
    show h bleh
    h "Hey, someone had to pay!"
    show s whatever
    s "Apparently not!"


    if together == True:
        jump narcissus

    else:
        jump merge


label merge:

    show s listen
    s "Vivian even said she'll undo the spell for us."
    show s smile
    s "She just needs some time to figure it out."
    show h unhappy
    h "Yeah, well I wonder what that's gonna cost."
    show s whatever
    s "She's nice! I'm sure it's something reasonable."
    show h kindasmile
    h "Yeah, she's so nice to us for no reason, I think we're getting scammed."
    show s yeahright
    s "A fine judge of character you are! You already got scammed by Jerkface. {i}Twice!{/i}"
    show h sneaky
    h "That's right, I'm learning from past experiences here."
    show s think
    s "Aaaaah, okay fine. But can we stop drinking the poison anyway?"
    show s explain
    s "I'd like to merge back to a body with the organs still functioning."
    show h smilelow
    h "So I guess it's just agreed now that we're going to merge back?"
    show s embarrassed
    s "It isn't?"
    show h shruglaugh
    h "I don't know. Is it?"
    show s docile
    s "Yeah? I mean I'm fine now, right? I thought you said so."
    show h smilegentle
    h "I didn't exactly say \"fine\" but I guess so..."
    show h sorry
    h "So now what? We just... wait?"
    show s whatever
    s "That's right! We sit with our thumbs up our asses and wait."
    show h nah
    h "Oooor we could just ask Lua to merge us back."
    show s yeahright
    s "\"I'm learning from past experiences!\""
    show h laugh
    h "Youuuuuu can shut the hell up!"
    show s laugh
    play sound "audio/_nervousbubbles.mp3"
    s "Hahaha!!" with hpunch

    scene black with fade
    stop music fadeout 2.0
    "Despite almost being smart enough not to, Thiu goes to visit Lua."

    play music "audio/02_outof.mp3" fadein 2.0
    scene entry with fade

    show l pity at righty
    show h smile at lefty, faceright
    with dissolve
    l "You just keep on dropping by uninvited."
    show h laugh
    h "I won't be long this time."
    show l bored
    l "And didn't I tell you we can't make the next batch of poison yet?"
    show h nervous
    h "About that!"
    show h mock
    h "Me and I decided we want to merge back."
    show l playful
    l "Oh, you did, huh? {b}So what?{/b}"
    show h shruglaugh
    h "Well I figured that if I'm getting the spell undone, I shouldn't have to pay for it."
    show l smilesmile
    l "Sorry. No refunds."
    show h smilegentle
    h "That's fine I guess. Can you just merge us back anyway?"
    show l smug
    l "Well, as it just so happens, this set-up works better for me."
    show l fake_laugh
    l "No one's going to come knocking if you kick the bucket, y'see."
    show l chuckle
    l "So no. I don't think I'll be merging you back."
    show h smileguilty
    h "............................Oh."
    show h whatever
    h "(Well it was worth asking I guess...)"
    show h kindasmile
    h "Okay then. It's been fun, but let's not hang out anymore."
    show l sheepish
    l "Alright. See you next week!"
    show h confused
    h "Err, no. I'm saying we won't."
    show l oh
    l ".....Excuse me?"
    show h sneaky
    h "I think helping you out once was a payment enough."
    show h mock at faceleft
    h "So I wish you all the best and goodbye!"
    show l angry_explain
    l "Hoooold on a minute, my friend."
    show l complain
    l "You think that's up to you?"
    show l ugh
    l "You agreed to help me, and it's up to me to specify when that helping is done."
    show h smilelow at faceright
    h "Hmmmm nope! I think it's finished now."
    show h smug
    h "And if you don't like that, I guess you can take me to court."
    show l whatever
    l "......................."
    show h laugh
    h "Hahah!! So I guess that's that."
    show l miffed
    l "Someone's feeling cocky today..."
    show l chuckle
    l "Just what made you change your mind like this, I wonder?"
    show h sneaky
    h "I just don't feel like dying anymore I guess."
    show l mock
    l "No, of course not. That's the other you."
    show h laugh
    h "Nope! He doesn't want to die either."
    show l lookup
    l "You sure change your mind a lot, I see..."
    show h smug
    h "And if you change your mind about merging me back, let me know!"
    show l oh
    l "I wouldn't hold my breath if I were you."
    show h mock at faceleft
    h "Okay, that's fine. You're not the only mage in town anyway."
    hide h with moveoutleft
    h "See you around!"

    scene kitchen_day with fade
    show a laugh_bounce at righty with dissolve
    show l miffed at lefty, faceright with moveinleft
    a "Someone's in a great mood I see."
    show l smilesmile
    l "..............Do you ever just get an urge to rip someone's head off?"
    show a think
    a ".....Uhh?"
    show l angry_explain
    l "Because I do! I'm having it right now!"
    show a ohshit
    a "Ooookay. I'm gonna go and take my head elsewhere now..."
    show l ugh
    l "Can you believe it!? That idiot what's-his-name!!"
    show a listening
    a "Who? Thiu??"
    show l complain
    l "Yes! I know for a fact that he has shit for brains!"
    show l angry_explain
    l "Why would he suddenly decide he doesn't want to help me finish the potion!?"
    show a smile_bounce
    a "There there, don't be sad."
    show l complain
    play sound "audio/_metal.mp3"
    l "And the \"bohoo sue me\"? {b}Fuck you!!{/b}" with vpunch
    show a grin_bouncy
    a "Some dumbass is a dumb ass. So what?"
    show l whatever
    l "I just don't appreciate being talked to like that!"
    show l ugh
    l "Who does this guy think he is?? And who does he think he is talking to!?"
    show l angry_explain
    l "I ought to curse his ass!!"
    show a laugh_bounce
    a "Yeah, go for it!"
    show l bored
    l "Speaking of petty curses, I bet Vivian--"
    show a listening
    a "......You bet Vivian what?"
    show l fake_laugh
    l "{i}You bet{/i} she's gonna get a piece of my mind!"
    show l ugh
    l "There's no way this isn't her fault somehow!"
    show a miffed
    stop music fadeout 2.0
    a "Okay whatever. Just leave me out of it."

    play music "audio/11_bitch.mp3" fadein 2.0
    scene shop with fade

    "And what was Vivian up to?"
    "She was busy reverse engineering Lua's splitting spell."
    "It wasn't going very well..."
    show v down at lefty, faceright with dissolve
    v "And what happened then?"
    show s shrug at righty with dissolve
    s "I don't know. I was unconscious."
    show v unsure
    v "You didn't see him prepare anything before hand or something?"
    show s sorry
    s "No, it was all very sudden..."
    show s whatever
    s "One moment I'm in mid-air, and the next everything hurts."
    show s angry
    s "And then it's already morning and I'm two people..."
    show v think
    v "What about the other you? Does he remember anything?"
    show s dontcare
    s "No."
    show v worry
    v "......Hmm. This gives me very little to start off with...."
    show s down
    s "But you can still do it, right?"
    show v down
    v "Probably..."
    show v ohyeah
    v "It's just gonna take a little longer."
    show s docile
    s "How much longer?"
    show v unimpressed
    v "I'm guessing just a couple years."
    show s surprise
    play sound "audio/_impact.mp3"
    s "YEARS!!" with hpunch
    show v think
    v "??????"
    show s nervous_smile
    s "I- I thought this was gonna be all over with in a few days or so!"
    show v impatient
    v "What on earth made you think that?"
    show s listen
    s "Jerkface made it look easy!"
    show v down
    v "Of course it's going to be easy if you already know the spell!"
    show s sad
    s "{i}Sighhhh{/i}....."
    show v ukidding
    v "It takes a whole lot longer to start from scrath!"
    show v sigh
    v "And even then, it might not be a spell I can pull off."
    show s docile
    s "And it's not even certain!?"
    show v unsure
    v "No. Though I'm pretty confident."
    show s yeahright
    s "I don't know if I'm going to live that long..."
    show v smile_closed
    v "I'm sure you've got thirty or so years still..."
    show s worry
    s "But I'm burning two lives at once."
    show s sad
    s "So I'll only have our combined left-overs once we merge."
    show v ohyeah
    v "Yeah. Sucks to screw up, doesn't it?"
    show s disapprove
    s "Wow, thanks. That's really---"
    play sound "audio/enter_shop.mp3"
    show l oh at center with moveinright
    l "............................."
    show s confused at right
    play sound "audio/_thunk.mp3"
    s "Ah! What are you doing here?" with vpunch
    show l miffed
    l "Piss off you extra."
    show v heh
    v "....Can I help you?"
    show l angry_explain
    show s think
    play sound "audio/_metal.mp3"
    l "I can only take so much of your shit Vivian!" with vpunch
    show v unimpressed
    v "I don't recall giving you any shit, seeing as I don't give a shit."
    show l mock
    l "Now {i}that's{/i} some bullshit!"
    show l complain
    l "Why are you so hellbent on ruining my research?"
    show l oh
    l "I told you I'll let you in on it if you want, so--"
    show v pissed
    play sound "audio/echo.mp3"
    v "I don't want in on it!!" with hpunch
    show l ugh
    l "Then why are you getting in my way? Moral obligation? Oh, please."
    show v impatient
    v "I don't owe you any explanations."
    show l miffed
    l "And I don't owe you any more of my time."
    show l happy at faceright
    l "Come along Thiu. {i}You{/i} still owe me quite a bit."
    show s confused
    s "H-huh??"
    show l smilesmile
    l "Don't tell me you forgot? You haven't paid me for splitting your soul."
    show s bitetongue
    s "O-other me already told you! I don't need to pay you anything!"
    show s docile
    s "R-right Vivian??"
    show v ohyeah
    v "Right."
    show l sheepish
    l "Right, right. Other you paid me already."
    show l complain
    l "But obviously I'll be taking payments from the both of you."
    show s sorry
    s "But--?? Um... Vivian said...?"
    show l whatever
    l "It's awfully hypocritical of Vivian to expect me to dish out spells for free, isn't it?"
    show v think
    v "............................"
    show l playful
    l "But relax, I'm not asking for anything as oh, so horrendous, as aiding me to cure aging!"
    show l angry_explain at faceleft
    show v unimpressed
    l "No, that would make our dear friend Vivian upset."
    show s nervous_smile
    s "Um... so what is it then?"
    show l chuckle at faceright
    l "Well that's what we're going to have to discuss."
    show l sheepish
    l "So come along."
    show s docile
    s "Ummm? Viv?"
    show v ohyeah
    v ".............Go ahead, you made a deal."
    show s scold
    s "You sure switched your tone fast!"
    show v down
    v "Just wash his dishes or something and that's that."
    show l fake_laugh at faceleft
    l "Well no wonder your shop is going under if your spells are that cheap!"
    show v ukidding
    v "I'm taking into consideration how much the other half paid you already."
    show v smirk
    v "Don't be so petty."
    show l complain
    l "You tell me all about petty, \"Viv\"!"
    show s docile
    s "Umm... What should I-..?"
    show l oh at faceright
    l "Move, that's what."
    hide v
    hide l
    hide s
    with dissolve

    stop music fadeout 2.0
    "Lua drags Thiu back home with him."

    play music "audio/03_partisan.mp3" fadein 2.0

    scene kitchen_day with fade

    show s down at lefty, faceright
    show l oh at righty
    with dissolve
    s "S-so, uhhh.... What now?"
    show l happy
    l "Coffee. Would you like some?"
    show s yeahok
    s ".....Not really."
    show l lol
    l "Weird, I remember you really liking it! Hahah!!"
    show s scold
    s ".........................."
    show l smilesmile
    l "Don't be so nervous. Let's figure out a payment, shall we?"
    l "Go ahead, my friend. Suggest something."

    menu:

        "Wash dishes.":

            s "Dishes."
            show l miffed
            l ".......I don't think I have enough dishes to cover the cost."
            show s dontcare
            s "I can wash them several times I guess."
            show l pity
            l "You're not nearly as funny as you think you are."
            show s fuckyou
            s "The only joke here is this contract we're supposedly making..."

        "Cash or credit.":

            show s sorry
            s "Originally you told me it was cash or credit, so..."
            show s worry
            s "And I already agreed to that, so..."
            show l think_pleased
            l "I suppose I did say that."
            show s scold
            s "Oh!! And other me already paid half, so it's only half price now!"
            show l smile
            l "Yes, you're right."
            show l playful
            l "Half a million it is, then!"
            show s thefuck
            play sound "audio/_metal.mp3"
            s "HALF A--!!!" with vpunch
            show l fake_laugh
            l "Hahahah!!"
            show s shrug
            s "You're kidding!!"
            show l pity
            l "So which will it be, my friend? Cash or credit?"
            show s disapprove
            s "I can't afford that!!"
            show s thefuck
            s "I'll--- it'd just be cheaper to sue your ass!"
            show l chuckle
            l "Then who's going to merge you back?"

        "Nothing.":

            show s nervous_smile_away
            s "I-I, uhh... I don't have to pay you anything..."
            show l mock
            l "Really?"
            show s sorry
            s "It's like, .... God, it's like-..."
            show s explain
            s "\"If only you had it in writing, my friend!\""
            show s disapprove
            s "\"You're learning so much today! Har har har...\""
            show l oh
            l ".................................Your memory is pretty sharp for someone so dull."
            show s fuckyou
            play sound "audio/_metal.mp3"
            s "Fuck you!" with vpunch

    show l complain
    l "I wouldn't make an enemy out of me if I were you."
    show l lookup
    l "Vivian is going to take quite a while to learn my spell."
    show l mock
    l "And then perhaps a little longer still to reverse it."
    show s think
    s "....................."
    show s docile
    s "But... Are you going to lift the spell?"
    show l playful
    l "I don't know. Guess we're here to plan this all out."
    show s down
    s "Then... I want the other me here too."
    s "So he can plan with us."
    show l smug
    l "Let's not pretend like you are two different people."
    show s disapprove
    s "....Then why do I need to pay twice?"
    show l oh
    l "Can we just sort this out already?"
    show s sad
    s "Ugh, no. I need time..."
    show l lol
    l "Yeah, no kidding. You're going to age twice as fast."
    show s docile
    s "...Is that how it works? I figured I'd just drop dead in my forties..."
    show s dontcare
    s "After I run out of soul fuel or whatever..."
    show l sheepish
    l "Of course not. You're burning through your soul from both ends."
    show l pity
    l "So you'll age up and wither away at double speed."
    show s angry
    s "Nice. Another detail I wish I had known."
    show l happy
    l "And another detail you would've known, had you asked!"
    show s ticked
    s "Goddammit..."
    show l smile
    l "Do you know what would help with your rapid aging?"
    show s confused
    s "Huh?? What??"
    show l mock
    l "The potion your other self was helping me test."
    show l playful
    l "What a shame that project is dead in the water now."
    show s sorry
    s "............Oh."
    show l lookup
    l "I honestly don't think it would've taken me that long to figure out the rest."
    show l chuckle
    l "Unlike Vivian I'm quite good at what I do."
    show l smilesmile
    l "So imagine if the other you helped me out testing it."
    show l fake_laugh
    l "Hell, the next batch might even be the winner!"
    show s sad
    s "........................................."
    play sound "audio/ding.mp3"
    show l happy
    l "Ah, excuse me. Must be another customer."
    hide l
    hide s
    with dissolve
    "While Lua goes to ruin someone else's life, Thiu reflects upon his situation."
    show s down at lefty, faceright with dissolve
    s "(........I-... It doesn't add up somehow.)"
    show s docile
    s "(Why would I age twice as fast? That doesn't make sense...)"
    show s bitetongue
    s "(Kinda feels like he just wants us to keep testing his potion...)"
    show s confused
    s "(But... what if it {i}is{/i} true, and I am aging at double speed??)"
    hide s with dissolve
    "Thiu feels like he is heading to a trap, or dead-end of some sort, no matter what."
    "He wishes he'd have bought another phone, so he could call himself to ask for his equally useless thoughts."
    show a laugh_bounce at lefty, faceright with dissolve
    a "Oh! I didn't know you were visiting!"
    show s sorry at righty with dissolve
    s "You were, uhh...."
    show a smile_bounce
    a "Tal! And you're the unlucky Thiu!"
    show s down
    s "Yeah I sure feel unlucky right now..."
    show a listening
    a "Oh. What's up?"
    show s hurt
    s "{i}Sighhhh....{/i} I don't know."
    show s yeahright
    s "Your brother is an ass..."
    show a laugh
    play sound "audio/_laugh.mp3"
    a "HAHAHAHA!!" with vpunch
    show a laugh_bounce
    a "Yup, he sure is!"
    show a smug
    a "What's the matter? Maybe I can help you out!"
    show s sad
    s "Probably not... Unless you can merge me and my other self back together."
    show a think
    a "Nah, sorry. My magic sucks so bad I gave up even trying."
    show s nervous_smile
    s "...Thanks anyway."
    show s worry
    s "It's my own fault. I didn't think things through..."
    show s scold
    s "And now even Vivian is saying to suck it up and just pay up somehow."
    show a listening
    a ".......You're friends with Vivian?"
    show s confused
    s "I guess? ...Or kinda?"
    show a smile_bounce
    a "Oh!! She say anything about me??"
    show s docile
    s ".....No, sorry."
    show a think
    a "Oh......"
    show s sad
    s "I mean... We're mostly trying to undo this split spell."
    show a angry
    a "Really?? Vivian is?"
    show s shrug
    s "Is... that like a bad thing?"
    show s explain
    s "(God, am I getting screwed over by her too???)"
    show a smug
    a "No, no! I was just surprised she was willing to touch banned magic again, hahah!"
    show s ohwell
    s "(.....\"Again\"?)"
    show a approve at faceleft
    a "Wait here."
    hide a with moveoutleft
    show s confused
    s "Huh?? Wait, what??"
    hide s with dissolve

    "Before Thiu can even comprehend what's going on, Tal returns with a backpack."
    "It's too small for whatever is inside, and the seams are just about to give..."

    show s docile at righty with dissolve
    show a laugh at lefty, faceright with moveinleft
    a "Okay, let's go!"
    show s disapprove
    s "Go where? I'm waiting for Lua..."
    show a bored_bounce at faceleft
    a "Yeah, you're gonna wait a while... C'mon!"

    scene entry with fade

    "Tal leads Thiu out right past Lua and some crying woman."
    "Lua notices, but is too busy selling the woman his awful services."
    "Thiu wants to tell her to run for the hills and never to come back, but figures it's none of his business."
    stop music fadeout 2.0
    "Plus it's not like he listened either, when told to stay away..."

    play music "audio/04_cantelope.mp3" fadein 2.0
    scene shop with fade

    "Thiu finds himself back at Vivian's shop."
    play sound "audio/enter_shop.mp3"
    show v gentle at lefty, faceright
    show s docile at righty
    with dissolve
    v "Well that was fast."
    show v smile
    v "What happened with-..."
    show a laugh_bounce at center with moveinright
    show s at right with moveinright
    a "Hellooooo Vivian!!"
    show v ukidding
    v ".......Why are you here?"
    show a grin_bouncy
    a "I heard you're dabbling with my brother's spell!"
    hide a
    hide s
    hide v
    with dissolve
    "Vivian gives Thiu a quick glance."
    "In just half a second she manages to convey both disappointment, betrayal, and hatred."
    show v pissed at lefty, faceright
    show s nervous_smile at righty
    with dissolve
    s "I--!! We were just chatting!"
    show s shrug
    s "I had no idea I wasn't allowed to talk about you??"
    show v sigh
    v "...Whatever."
    show a laugh at center with dissolve
    a "Don't be angry! Look what I have!"
    hide a
    hide s
    hide v
    with dissolve
    "Tal pulls Lua's spell book out of her bag."
    show v think at lefty, faceright
    show a approve at center
    show s sorry at right
    with dissolve
    a "You can borrow this if you'd like!"
    show v down
    v "..............."
    show v worry
    v "Why would you lend me this?"
    show s whatever
    s "(Yeah, it's not even hers to lend...)"
    show a miffed
    a "What do you mean why? I thought you wanted to know about the splitting spell."
    show v unsure
    v "......................."
    show v gentle
    v "...I'll make you some hot chocolate if you'd like."
    show a excited
    a "Aww yes!! Put marshmallows on it too!"
    show v unimpressed
    v "Okay, but they're pretty old."
    show a smug
    a "Sugar never expires!"
    hide a
    hide s
    hide v
    with dissolve
    "Thiu stands around awkwardly. He feels like a complete outsider."
    "Because he is."
    "Soon there is hot chocolate and chitchat about magic."
    "There is nothing what-so-ever that Thiu can add to the conversation."
    show s sad at righty with dissolve
    s "(This is just like the group assignments  back in school...)"
    show s down
    s "(I don't understand anything and nobody wants to talk to me.)"
    s "......................"
    show s nervous_smile
    s "Uhhh... So hey...?"
    show s nervous_smile_away
    s "S-should I go get the other me?"
    show a listening at lefty, faceright with dissolve
    a "Huh? What?"
    show s makenice
    s "If... Like if we're gonna try the spell..."
    show s sorry
    s "He should probably be around for that."
    show v down at left, faceright with dissolve
    v "...You want me to try the spell right now?"
    show s shrug
    s "I mean... We have the spell book..."
    show v think
    v "I'm just copying Lua's notes. I still need to study it myself."
    show s down
    s "Oh.... Okay.........."
    show s ashamed
    s "(Then why am I even here?!?! Should I just leave?!?!)"
    show a playing
    a "I think we should try it now!!"
    show a laugh_bounce
    a "It doesn't look that hard!"
    show v unsure
    v "Well... I'm not sure about this part about sewing the soul."
    show v ohyeah
    v "It doesn't explain how."
    show a listening at faceleft
    a "I dunno. A needle and a thread?"
    show v unimpressed
    v "Feels a bit weird..."
    show s sorry
    s "..............."
    show v ukidding
    v "Huh? You're still here?"
    show s nervous_smile
    s "Ahaha..... Yeaaaah....."
    show v think
    v "Aren't you going to get the other you?"
    show s whatever
    s "(What?? So we {i}are{/i} doing it now!?!?)"
    show s think
    s "Um... Yeah. I'll see you in a bit..."

    scene city_day with fade

    "Thiu removes himself from the shop."
    "The other two don't even notice and keep on chatting happily."
    "As Thiu suspected, his input wasn't needed at all."
    show s ashamed at center with dissolve
    s "(W-whatever! I don't mind at all!)"
    show s listen
    s "(I'm not interested in some dumb girl-talk anyway!!)"
    show s tocry
    stop music fadeout 2.0
    s ".........................."

    play music "audio/09_doit.mp3" fadein 2.0
    scene home_clean with fade

    show s sad at lefty, faceright with dissolve
    s "Hey me, you home?"
    show h smile at righty with dissolve
    h "Welcome home!"
    show s embarrassed
    s "That's right!! I'm welcome here!!"
    show h kindasmile
    h "..........Yeeeaaah?"
    show s makenice
    s "Listen, Vivian is going to undo this spell."
    show h laugh
    h "Oh? She already figured it out?"
    show s sad
    s "Don't worry about that... Let's just go."
    show h smilecalm
    h "...?"

    hide h
    hide s
    with dissolve
    "As Thiu puts on his shoes, the other feels a bit melancholic."
    "Well more melancholic than usual..."

    show h sorry at righty with dissolve
    h "....What's up?"
    show s docile at lefty, faceright with dissolve
    s "Huh??"
    show h nah
    h "You have that stupid look on your face again."
    show s ticked
    s "Up yours! I can't help your face looks stupid no matter what."
    show h smilelow
    h "Something on your mind?"
    show s down
    s "...........It's just..."
    show s sorry
    s "The house is gonna get quiet again, that's all..."
    show h bleh
    h "Quiet? Did you not hear the party downstairs last night?"
    show s scold
    s "The house as in our apartment! My room!!"
    show h sneaky
    h "Ooooohhh..!"
    show h laugh
    h "You mean after we merge back!"
    show s ashamed
    s "Yes..."
    show h shruglaugh
    h "I'm just happy you won't be hogging all the blanket anymore!"
    show s yeahright
    s "Goddammit. I'm trying to express something here, but all you care about is yourself..."
    show h lol
    h "Hahhah!! You think too much."
    show h smile
    h "C'mon, let's get going!"
    show s worry
    stop music fadeout 2.0
    s "......................{i}Sigh.{/i}"

    play music "audio/08_why.mp3" fadein 2.0
    scene shop with fade

    "Even before entering the store, Thiu can hear Tal and Vivian laughing."
    "It's like they're best friends now. Thiu doesn't understand."
    show a laugh_bounce at lefty, faceright with dissolve
    a "Ohh heeeey!! The whole Thiu is here now!"
    show s down at right
    show h smile at righty
    with dissolve
    h "Hello hello! I heard I was going to get merged!"
    show v smile at left, faceright with dissolve
    v "Right. This spells seems simple enough."
    show v smirk
    v "Or at least simpler than the double time one."
    show a laugh at faceleft
    play sound "audio/_laugh.mp3"
    a "HAHAHAH!! Ohh!! You remember that one time with the drunkard??" with hpunch
    show v heh
    play sound "audio/_nervousbubbles.mp3"
    v "Oh my god, don't even remind me! Hahah!!" with vpunch
    hide v
    hide a
    hide s
    hide h
    with dissolve
    "Apparently something hilarious has happened."
    "But Thiu would not know."
    show h shruglaugh at righty with dissolve
    h "Maybe you can fill me in on that one after I'm merged back."
    show v worry at lefty, faceright with dissolve
    v "Oh. Right! Sorry..."
    show v smile_closed
    v "Which body do you want to keep?"
    show h kindasmile
    h "Which body do I what now??"
    show v gentle
    v "You have two bodies now. Once I merge your soul, which body do you want to house it in?"
    show h unsure
    h "Oh..."
    show h sorry
    h "Let me think about it..."
    hide v with moveoutleft
    show h smile at lefty, faceright
    show s sad at righty
    with moveinright
    h "What do you think?"
    s "..............................."
    show h explain
    h "I think we should go with yours."
    show h laugh
    h "I mean I've been stabbed and poisoned."
    show h lol
    h "So yours is probably in better shape."
    s "......................................."
    show h sorry
    h "Hello?"
    show s think
    s "Huh? Yeah... Sure."
    show h smilelow
    h "What's wrong?"
    show h shruglaugh
    h "Ah, actually don't bother telling me, I'll know all about it in a minute."
    show h laugh
    h "I wonder what's it gonna be like, having two accounts of the same events, hahahha!!"
    show h smug
    h "Like when I tried to kill you, that's gonna be interesting."
    show s makenice
    s "Hey me..?"
    show h smile
    h "Yeah?"
    show s down
    s "Maybe we could stay like this..?"
    show h whatever
    h "......Say that again?"
    show s nervous_smile_away
    s "I'm just-... I mean, it's not that bad like this..."
    show h unamused
    h "How is having our life force split not \"that bad\"??"
    show s embarrassed
    s "It's not like we're doing anything particularly important with our life anyway..."
    show s sad
    s "A short life is fine too."
    show h nervous
    h "But wouldn't you rather have a longer one?"
    show s ticked
    s "Not if it's lonely..."
    show h awkward
    h ".................What... the hell is this conversation right now?"
    show h unhappy
    h "Why are we having this??"
    show s ashamed
    s "Let's not merge..."
    h "....................................."
    show s nervous_smile
    s "Let's not merge! I want to be friends."
    show h bleh
    h "For fuck's sake..."

    menu:

        "Merge.":

            show h nah
            h "I'll be your friend, okay?"
            show h smilelow
            h "But we'll do that as a one single person!"
            show s disapprove
            s "How the hell would that work!?"
            show h sneaky
            h "Easy! All you wanna do is play video games anyway."
            show h shruglaugh
            h "We can do that as a single person no problem."
            show s think
            s "It's not the same! I can't talk to you!"
            show s ticked
            s "And there's no feedback!! Like no one is there to react to me."
            show s embarrassed
            s "So it's lonely!"
            show h smilegentle
            h "Well once we're one I can make us some friends."
            show s sad
            s ".............{i}Sigh.{/i}"
            show h smug
            h "Think about it this way..."
            show h kindasmile
            h "Right now we're very similar. So of course we'll get along and whatnot."
            show s yeahok
            s "I don't think we've gotten along particularly well..."
            show h bleh
            h "Whatever. Give it a few years, and we'll become different people for sure."
            show h mock
            h "We might even become so different I'll want nothing to do with you."
            show h kindasmile
            h "And then we'll never hang out again."
            show s think
            s "..........."
            show h laugh
            h "But if we merge now, you'll never be alone no matter how much I hate you!"
            show s whatever
            s "Wow."
            show h sneaky
            h "Pretty convincing, huh?"
            show s explain
            s "Yeah, I guess...."
            show h lol
            h "Alright! Let's get this over with."

        "Don't merge.":

            stop music fadeout 2.0
            show h pissed
            h ".............{i}Sigh.{/i}"
            play music "audio/13_where.mp3" fadein 2.0
            show h unamused
            h "Feels like a bunch of effort was wasted just now."
            show s docile
            s "Huh?"
            show h argue
            h "Like we've been running around this whole time trying to merge."
            show h unhappy
            h "And now you throw this curve ball..."
            show s ticked
            s "Yeah? I changed my mind, what about it?"
            show h bleh
            h "So now what? You wanna just loiter around for the rest of our short lives?"
            show s worry
            s "What??"
            show h whatever
            h "Since we're not merging."
            show s makenice
            s "We're not?"
            show h unamused
            h "Apparently not."
            show s smile
            s "Really?!"
            show h mock
            h "Yeah. I can't believe it either."
            play sound "audio/Special & Powerup (23).wav"
            show hug at center, faceright
            hide s
            hide h
            s "YES!!" with vpunch
            h ".....??"
            hide hug
            show s shy at righty
            show h smilelow at lefty, faceright
            with dissolve
            s "Err, I mean, yeah! Yeah okay, whatever."
            show h sneaky
            h "Well I'm glad you're happy."
            show s smiledown
            s "You should be happy too! You're the happy one after all!"
            show h kindasmile
            h "Well honestly I think I'm kinda lukewarm now."
            show h unsure
            h "Like not particularly happy or sad."
            show s surprise
            s "Huh, I think I'm like that too."
            show s laugh
            s "Maybe it's like that... like that science thing?"
            show h nah
            h "I'm gonna need more details to understand what you're on about."
            show s smile
            s "Homeostasis! Our soul is balancing out! And becoming stable."
            show h lol
            play sound "audio/_laugh.mp3"
            h "You're so full of shit, HAHAHAHAHA!!" with vpunch
            show s ticked_shy
            s "It--- I'm being so smart right now!"
            show h laugh
            play sound "audio/_nervousbubbles.mp3"
            h "No, dumbass! HAHAHA!! I bet that's not even the right word you're using!" with hpunch
            show s disapprove
            s "Like you'd know, you're as dumb as me!"
            show h shruglaugh
            h "If anything we're twice as dumb now."
            show s whatever
            s "Let's tell Vivian just how dumb we are."
            show h kindasmile at faceleft
            h "Hey Vivian!"
            hide h
            hide s
            with dissolve
            "Vivian and Tal stop telling inside jokes."
            show v heh at lefty, faceright
            show h smile at righty
            with dissolve
            v "Okay, which body is it?"
            show h laugh
            play sound "audio/Special (8).wav"
            h "Both!" with vpunch
            show v pissed
            v "...........I just told you--"
            show h shruglaugh
            h "That's fine! It's fine! Everything is fine like this."
            show h sneaky
            h "That is to say, thank you for all your efforts, but we're gonna stay like this."
            show v ukidding
            v ".........................Are you sure?"
            show v ohyeah
            v "You're going to die at your forties."
            show h lol
            h "That's fine. I'm too dumb to think that far."
            show v unsure
            v "....And you're both fine with that?"
            show s smile at right with dissolve
            s "Yeah... It's all fine."
            show v down
            v ".........."
            hide v
            hide h
            hide s
            with dissolve
            "Vivian looks at Tal. Tal just shrugs."
            show v think at lefty, faceright
            show h sneaky at righty
            show s smile at right
            with dissolve
            v "Well... Okay?"
            show v unimpressed
            v "But just make sure you understand, I'm not going to keep this offer open."
            show v impatient
            v "I'm not merging you back later if you refuse to do it now."
            show s sad
            s "That's fine, I-"
            show v down
            v "It even reads in Lua's notes, that it's gonna get harder, and harder to merge back as your soul adapts to being split."
            show s docile
            s "It's fine!"
            show h shruglaugh
            h "Yeah, what I said."
            show h mock
            h "Or he said."
            show h explain
            h "What we said."
            show s disapprove
            s "Now you're just being confusing on purpose..."
            show s smile
            show h lol
            play sound "audio/_laugh.mp3"
            h "Hahahha!!" with hpunch
            show v worry
            v ".....Well if you're sure."
            show a think at left, faceright with dissolve
            a "I should return Lua's book before he realizes it's gone..."
            show v smile at faceleft
            v "Right..."
            show v smile_closed
            v "Thanks for bringing it anyway."
            show a laugh_bounce
            a "No problem!!"
            show a smug
            a "I'll bring my bouncy ball collection next time!"
            show v unimpressed
            v "I see you intend to come again..."
            show a bored_bounce
            a "That's right! So buy some fresh marshmallows. Those old ones were kinda gross."
            show v ukidding
            v "Who would've thought? It's not like I told you so or anything."
            show a rage
            a "Quiet you! I was being polite okay? I'm nice like that!"
            hide v
            hide h
            hide a
            hide s
            with dissolve

            "Thiu figures this conversation has nothing to do with either of him."
            stop music fadeout 2.0
            play sound "audio/enter_shop.mp3"
            "So he leaves with a short bye-bye that goes barely noticed."

            play music "audio/09_doit.mp3" fadein 2.0
            scene home_clean with fade

            show h shruglaugh at righty with dissolve
            h "Here we are again!"
            show h sneaky
            h "And it's not quiet at all."
            show s smiledown at lefty, faceright with dissolve
            s "Yeah..."
            show s worry
            s "So what do you wanna do about Jerkface?"
            show s whatever
            s "He was hassling me for a payment..."
            show h confused
            h "But I already paid?"
            show s think
            s "He said I need to pay too."
            show h unamused
            h "Yeah, that's not happening."
            show h fuckyou
            h "He can consider us not suing his ass a payment."
            show s dontcare
            s "Like we'd have the money to sue anyway."
            show h mock
            h "We should get a job or something."
            show s docile
            s "What? To sue him??"
            show h laugh
            h "No, no. To have a life for ourselves."
            show h sneaky
            h "Since there's two of us now. And I'd like to move somewhere we have a little more space."
            show h sorry
            h "I mean... We need another bed."
            show h whatever
            h "And maybe an actual kitchen table, rather than whatever that IKEA thing sticking out the wall is."
            show s ohwell
            s "And a parakeet."
            show h surprised
            h "You want a parakeet?"
            show s makenice
            s "Yeah..."
            show h mock
            h "You can get a parakeet once you've proven you can take care of yourself first...."
            show s fuckyou
            s "What the hell, who put you in charge?"
            show h smilegentle
            h "Me. I'm the main Thiu after all."
            show s disapprove
            s "Says who!? I never agreed to that!!"
            show h shruglaugh
            h "Tooooo bad! You wanted me around so here I am!"
            show s ashamed
            s "Oh god, I've made a mistake..."
            show h lol
            play sound "audio/_nervousbubbles.mp3"
            h "HahahHAAH!! That's nothing new." with vpunch

            scene black with fade

            "Whether it was a mistake or not, this was Thiu's new life."

            scene halved with fade

            $ persistent.halved = True

            "Stuck with himself, and possibly a parakeet."
            "Together they had an okay-ish, albeit a bit short life."
            "Half-assing everything the whole way through."

            "HALVED END."

            window hide
            pause

            play sound "audio/Coins (21).wav"

            return

    show h laugh at righty, faceleft
    show s listen at right
    show v unimpressed at lefty, faceright
    with moveinleft

    h "Okay! We've decided! We'll keep other me's body."
    show s confused
    s "Wait, we decided that??"
    show h nah
    h "Yeah, wish you had listened..."
    show v smile
    v "Okay. We can start whenever you're ready."
    show h smug
    h "We're ready."
    show s makenice
    s "We are?"
    show h sneaky
    h "Yes."
    show v smile_closed
    stop music fadeout 2.0
    v "Alright. I'll do my best..."
    hide v
    hide s
    hide h
    with dissolve
    play music "audio/06_gaslight.mp3" fadein 2.0
    "Thiu gets a bad feeling the second his body is back to floating in mid-air."
    "And even though he gets a soul sucking kiss from Vivian, he's just not happy about it."
    scene black with fade
    "Something isn't right..."
    "..................."
    ".............................."
    "..........................................."
    stop music fadeout 2.0
    a "Heeeeey! Anybody there??"
    play music "audio/08_why.mp3" fadein 2.0
    scene shop with fade
    a "Ah! He moves!"
    s "??????"
    show a laugh_bounce at lefty, faceright with dissolve
    a "Good evening!"
    show a smug
    a "You weren't out nearly as long as last time."
    show w doubt at righty with dissolve
    s "This..."
    show w explain
    h "You gave me the wrong body..!"
    show v down at right with dissolve
    v "I'm sorry! I tried putting your soul in the other one, but you wouldn't wake up!"
    show a think
    a "Or have a heart beat!"
    show v worry
    v "I was scared you weren't going to wake up at all..."
    show w awkward_smile at faceright
    s "It's okay..."
    show w explain_angry at faceleft
    show a ohshit
    play sound "audio/echolong.mp3"
    h "It's not okay!!" with vpunch
    show v think
    v "????"
    show w confused at faceright
    s "S-sorry! I didn't mean to yell!"
    show w miffed
    play sound "audio/echowhip.wav"
    h "{b}Yes I did!!{/b}" with vpunch
    show v shock
    v ".................."
    show a smug
    a "O-oh, Vivian! I think you've messed it up."
    show w doubt
    s "Ugh... Why is it so noisy..."
    show w annoyed
    h "Aaah, why is there an echo?"
    show w explain_angry
    play sound "audio/_hiss2.ogg"
    s "Shut up, shut up!!!" with hpunch
    show v ukidding
    v "....Ooooh shit."
    show a bored_bounce
    a "What? What happened?"
    show v shock
    v "I don't think the souls merged even though I stitched them together..."
    show a listening
    a "Looks fine to me though?"
    show v think
    v "How many Thius are in there?"
    show w awkward_smile
    s "One."
    show w miffed
    h "One!"
    show w awkward_laugh
    s "Or two..?"
    show w explain
    h "I knew we shouldn't have trusted Vivian to do this..."
    show w explain_angry at faceleft
    play sound "audio/_hiss2.ogg"
    s "Well I knew we shouldn't have merged at all!!"
    show w smirk
    h "That's funny. I could've sworn you were the one who wanted to merge the second we split."
    show w annoyed
    s "No! It's different now!"
    show a ohshit
    a "Ooooookay... What should we do?"
    show v shock
    v "Crap crap crap crap...."
    show a think
    a "And what do you wanna do about the corpse?"
    show v at faceright
    v "Crap crap crap crap crap......"
    show a miffed at faceleft
    a "I'm gonna put it in the freezer for now..."
    hide a
    hide v
    hide w
    with dissolve
    "Tal starts dragging one of Thiu's bodies towards the kitchen."
    "Well, if you can call it a kitchen. It's more like a break room that happens to have a sink and a fridge-freezer combo."
    "However, the freezer is far too small to fit a whole body."
    show a ohshit at lefty with dissolve
    a ".............Should I like hack this up or...?"
    show w explain_angry at righty with moveinright
    h "No! Hands off! I want that one!"
    show w miffed
    h "Move my soul to that one."
    show a angry at faceright
    a "Dude. This thing's been dead for like an hour. It didn't work before and it definitely wouldn't work now."
    show a rage
    play sound "audio/_thunk.mp3"
    a "Hey Vivian!! You got a butcher knife in here or something?" with vpunch
    show w surprise
    play sound "audio/_impact.mp3"
    h "Whoah whoah whoah!! You're really doing this in front of me??" with hpunch
    show w nervous
    s "I think... maybe we should just bury it. Like a proper corpse..."
    show w lookaway
    s "Y'know... Respectfully..."
    show a bored_bounce
    a "That's wasteful. We can turn this into ingredients."
    show w explain_angry
    play sound "audio/_metal.mp3"
    h "Ingredients for fucking what!?" with hpunch
    show a approve
    a "Well for example--"
    hide a
    hide w
    with dissolve
    stop music fadeout 2.0
    play sound "audio/enter_shop.mp3"
    "It's at that moment that Lua barges in the shop."
    play music "audio/02_outof.mp3" fadein 2.0
    "He does not look happy, to put it mildly."

    show l angry_explain at righty
    play sound "audio/isbad.mp3"
    l "Where's my spell book you petty thief!!!" with vpunch
    show v shock at left with dissolve
    v "Crap crap crap crap........"
    show l ugh
    l "........?????"
    show l complain
    l "Tal, are you here!?"
    hide v with dissolve
    show a laugh at lefty, faceright with moveinleft
    a "Hellooooooo, I'm here!"
    show l ugh
    l "I know you took it! Where is it!?"
    show a listening
    a "The book? Right here, don't worry!"
    hide a
    hide v
    hide l
    with dissolve
    "Tal hands over the book."
    show a think at lefty, faceright
    show l miffed at righty
    with dissolve
    a "No need to get so angry. I was only borrowing it."
    show l complain
    l "Why'd you bring it here of all places?"
    show a ohshit
    a "Well...."
    show l miffed
    l "....And what's wrong with Vivian?"
    show v shock at right with dissolve
    v "Crap crap crap crap crap......"
    show v at faceright
    show l fake_laugh
    l "Does she need to use the bathroom or something?"
    show a laugh_bounce
    play sound "audio/_laugh.mp3"
    a "HAHAHAHAH!!" with vpunch
    show a smile_bounce
    hide v with dissolve
    a "Nah, we tried to undo your spell!"
    show a smug
    a "But it didn't work, hhahah!"
    show a think
    a "Or I mean it {i}did{/i}, but not as we wanted."
    show l oh
    l "What happened?"
    show a listening at faceleft
    a "Go take a look in the back."
    hide l
    hide v
    hide a
    with dissolve
    "Lua goes to take a look in the back as instructed."
    "In there he sees Thiu observing his dead body with half a leg cut off."
    "There's blood everywhere."

    show w doubt at lefty, faceright with dissolve
    show l oh at righty with moveinright
    h "Lua, thank fuck!! Look what they did to me!"
    show w annoyed
    s "Go away!! This is all your fault!! If you hadn't split me in the first place--!!"
    l "................"
    show l chuckle
    l ".....Eheh!"
    show l fake_laugh
    show w surprise
    play sound "audio/_laugh.mp3"
    l "HAHaHHAHAahAH!!!" with vpunch
    show l lol
    show w miffed
    l "What a disaster!! HAHA!!"
    show l smilesmile
    l "My god, are you both in there separately?"
    show w annoyed
    s "....Yes. We're both in here."
    show w awkward_laugh
    h "Can you fix me??"
    show l smug
    l "HAH! Why would I? You haven't even properly paid me for my last spell."
    show l pity
    l "Sorry friend, you're on your own."
    show w doubt
    s "You can't just not that do--- err... I-I mean, umm...!"
    show l oh
    l "....Once more?"
    show w smirk
    h "You can't just leave me like this. You have to admit this is at least partly your fault."
    show w annoyed
    s "Y-yeah, what he said!"
    show l playful
    l "Not in the least. Everything would've been swell had you done everything as I advised from the beginning."
    show l mock
    l "That is, following through and killing your negative feelings."
    show l chuckle
    l "But no, here you are, saddled with yourself, poor thing."
    show l happy at faceright
    l "But it's not my problem. I bid you farewell!"
    show w confused
    s "N-no wait!"
    hide l
    hide w
    with dissolve
    stop music fadeout 2.0
    "Lua leaves Thiu with the bloody mess."
    show a bored_bounce at lefty, faceright
    show v shock at right, faceright
    with dissolve
    play music "audio/10_goodlook.mp3" fadein 2.0
    a "Ahh, relax, Vivian! It's not that bad..."
    show l smilesmile at center, faceright with moveinleft
    l "Vivian, I could take the corpse off your hands before it starts rotting?"
    v "Crap crap crap crap....."
    show l down
    l ".........Tal go chop the thing up, we're taking it."
    show a grin_bouncy at faceleft
    a "Already on it!"
    hide l
    hide a
    hide v
    with dissolve
    "She goes back to cutting the body up, much to Thiu's horror."
    "A bunch of different variations of \"What is wrong with you!?\" can be heard."
    show l lol at lefty, faceright
    show v shock at righty
    with dissolve
    l "Oh my goodness Vivian, you really screwed this one up, hahahha!!"
    show v cry
    v "...................{i}Sob.{/i}"
    show l smilesmile
    l "Aww, don't cry..."
    show v sigh
    v "..........I screwed up."
    show l chuckle
    l "Yup, I believe I just said that."
    show v cry
    v "I'm such a fuck-up."
    play sound "audio/surprise.wav"
    v "I knew I wasn't ready to lift the spell yet.... I knew!" with vpunch
    show l playful
    l "...............Well, you did it anyway. So..."
    hide l
    hide v
    with dissolve
    "If Vivian wasn't crying already, she sure is now."
    show l whatever at lefty, faceright
    show v cry at righty
    with dissolve
    l "Umm... Okay, look. It's not that bad, okay?"
    show l down
    l "I mean you messed up the mending a bit, that's all... "
    show l smug
    l "Besides that guy's all screwed up anyway, who's going to notice?"
    show v ukidding
    play sound "audio/_impact.mp3"
    v "Me!" with hpunch
    show v pissed
    v "Because unlike you I have a conscience!"
    show l lookup
    l "Okay then, have fun with that."
    show l oh
    l "I'm going to get my body bag ready. I'll see you in a bit."
    show v worry
    v "...Wait."
    show l down
    l "Waiting."
    show v shock
    v "Can you.... Would you fix it?"
    show l miffed
    l "I don't know Vivian. You haven't been exactly nice to me lately."
    show l pity
    l "So I don't know if I have it in me to bail you out this time, love."
    show v ukidding
    v "\"This time\"!? What's that supposed to mean!?"
    show l whatever
    l "I made Lacy disappear, didn't I?"
    show v unsure
    v ".............."
    show l oh
    l "Or did you not notice? Nobody came asking anything."
    show l playful
    l "Almost like-- {i}oh!{/i} Almost like I made everyone forget about her??"
    show v down
    v "I didn't forget her."
    show l smilesmile
    l "Now {i}that{/i} I can fix, if you'd like."
    show v worry
    v "............Ugh. No."
    show v impatient
    v "And I think you did that for your own sake..."
    show l chuckle
    l "My sake, your sake... Do you really want to argue about this again?"
    show v unsure
    v "No..."
    show v cry
    v "I just-..."
    show l oh at faceleft
    play sound "audio/_metal.mp3"
    h "That's going too far!!" with vpunch
    hide l
    hide v
    with moveoutright
    show w miffed at lefty, faceright
    show a bored_bounce at righty
    with moveinright
    a "What? The head??"
    show w explain_angry
    h "Yes!! Why would you do that?"
    show w explain
    h "I can't believe I thought you were nice before!"
    show w miffed
    h "You're a bloody nightmare!"
    show a angry
    a "I told you to stop looking!"
    show a bored_bounce
    a "And I'm not cutting it for fun! Cheeks have a lot of meat."
    show a miffed
    a "And the eyes can be used to cure someone else's sight."
    show a approve
    a "So it's all for a good cause."
    show w defa
    s ".........It's just... You should've asked me."
    show w explain
    h "And I would've said no!!"
    show a miffed
    a "Don't be selfish..."
    show w annoyed
    show a at center, faceright
    show l complain at right
    with moveinright
    l "Stop arguing. You're making a scene."
    show l down
    l "What if the neighbors or someone comes to check?"
    show a rage
    play sound "audio/_hiss1.ogg"
    a "Tell that to Thiu!!"
    show a miffed
    show l ugh
    l "Just hurry up and finish!"
    show w miffed
    s "I can't believe you people!"
    show l fake_laugh
    l "Quit your yapping. Consider your useless corpse as payment for my services."
    show a behind w
    show w explain_angry
    play sound "audio/echo.mp3"
    s "What am I paying for {b}now{/b}!?" with vpunch
    show l lookup
    stop music fadeout 2.0
    l "A fix, I suppose."
    hide w
    hide l
    hide a
    with dissolve
    play music "audio/commercialbliss.ogg" fadein 2.0
    "And with that, Thiu is in mid-air once more."
    "So far every time this has happened things have gone from bad to worse."
    "So you see, he isn't very confident he wants to let this happen again."
    "Before he can scream for help, his soul is pulled out of his body once more."
    "Lua undoes Vivian's mistakes and fixes Thiu's soul right up."
    "Thiu's poor soul has been through so many hacks and slashes at this point, it can barely withstand it."
    "So this would have to be the last time anyone ever tampers with it."
    stop music fadeout 2.0
    "Which, luckily for Thiu, it is."

    scene black with fade

    "Tal and Lua finish things up, while Vivian cleans up after them."
    "The trio works so efficiently, you'd have to wonder if they've done this before."
    "Yes. The answer is yes they have."
    "But that's neither here nor there."

    play music "audio/13_where.mp3" fadein 2.0
    scene city_late with fade

    show l pleased at righty
    show a smile_bounce at right
    show v unsure at lefty, faceright
    with dissolve
    l "You can send him home as soon as he wakes up."
    show l lookup
    l "And... Somehow make him shut up about all of it, okay?"
    show v think
    v "That's a lot to ask, he seems a bit loose lipped..."
    show l smug
    l "Aww, you'll figure something out."
    show l smilesmile
    l "Good night Vivian."
    show a laugh_bounce
    a "You should come over sometime!"
    show v smile_closed
    v "....I might."
    show a excited
    show l pleased
    play sound "audio/_nervousbubbles.mp3"
    a "Alright! I'll bake us some gingerbread cookies!" with vpunch
    show v gentle
    v "That sounds good."
    show a laugh
    a "Hehee! Good night!"
    show a at faceright
    show l at faceright
    hide a with moveoutright
    show v worry
    v "Lua?"
    show l chuckle at faceleft
    l "What is it? I'm kinda carrying something light sensitive and would like to get home quickly."
    show v unsure
    v "Thank you."
    show l oh
    l "........??"
    show v sigh
    v "For a lot of things..."
    show v ukidding
    v "Ah. Though I'm still mad too..."
    show l mock
    l "Yes, well... aren't you always mad about something or other?"
    show l lol
    l "Tal is going be really mad too if you don't show up after she makes those cookies."
    show v smirk
    v "Then I guess I have to."
    show l sheepish
    l "If you do, I can show you how far I got with our potion."
    show l smilesmile
    l "And guess what, no one even died this time!"
    show v ohyeah
    v "You say that while carrying a corp--"
    show l ugh
    play sound "audio/surprise.wav"
    l "{b}LET'S{/b} not talk so loud in public." with vpunch
    show v heh
    play sound "audio/_nervousbubbles.mp3"
    v "Heheh!!"
    show v gentle
    v "I look forward to seeing it..."
    show l pity
    l "Until then."
    show v pleased
    v "Good night."
    show l down
    play sound "audio/_metal.mp3"
    a "{b}HURRY UP LUA YOU WORTHLESS SACK OF SHIT!!{/b}" with hpunch
    show l angry_explain at faceright
    l "Wow, someone's getting her ass kicked tonight!!"
    hide v
    hide l
    with dissolve
    stop music fadeout 2.0
    "Lua and Tal go home."

    scene black with fade

    play music "audio/steady.mp3" fadein 2.0
    "Several hours later, Thiu is recovering consciousness..."
    t "........................."
    t "(Am I dead yet?)"
    t "(No, not yet. Did you want to be?)"
    t "(Not really... Just felt like I might be.)"
    t "(We're not.)"
    t "(We're still using \"we\"?)"
    t "(I don't know. Are we? It's just me now.)"
    t "(I want to keep saying we though.)"
    t "(Okay, but not in front of anyone.)"
    t "(Yeah... Or they'll send us back to therapy.)"
    t "(I don't know, maybe we need it.)"
    play sound "audio/_nervousbubbles.mp3"
    t "HAHAHAHA!!" with vpunch

    scene shop with fade

    show v gentle at righty with dissolve
    v "...You seem in a good mood."
    show v unsure
    v "Or insane...."
    show w awkward_smile at lefty, faceright with dissolve
    t "...At this point I don't even know myself."
    show w miffed
    t "Where's Lua and his psychopath of a sister?"
    show v smile_closed
    v "They went home."
    show v smile
    v "You can go home too, if you feel okay."
    show w defa
    t "....I guess."
    show v think
    v "Before you go though, I'd like to ask you something..."
    show w lookaway
    t "Yeah? Go for it."
    show v unimpressed
    v "Do you have a job?"
    show w nervous
    t "..................Uuuuuuh????"
    show v unsure
    v "It's just that if you'd like, I could hire you."
    show w doubt
    t "I don't--... I'm not exactly reliable..."
    show v ohyeah
    v "That's fine. You could pop in whenever."
    show v heh
    v "And I'll pay you for whatever hours you work."
    show w sad
    t "......Why though?"
    show v pissed
    v "Because I need you to sign a non-disclosure agreement."
    show w surprise
    t "..........."
    show w laugh
    play sound "audio/_laugh.mp3"
    t "HAHAHHA!!!" with vpunch
    show w smirk
    t "Yeah okay, that makes sense I guess."
    show v worry
    v "It'd also let me keep track of you. In case I did any damage..."
    show w awkward_smile
    t "Okay then.... I'll work for you."
    show w smirk
    t "Though I'm expecting the mushroom tea to be complementary."
    show v heh
    v "Sure, have as much as you'd like."
    show w nervous
    t "And I honestly think I'll be absent quite a bit..."
    show v think
    v "Like I said, that's fine."
    show w laugh
    t "Sounds good then."
    show v smile_closed
    v "Glad to hear it."
    hide v
    hide w
    with dissolve
    "And that's how that went."
    "After being put back together again, Thiu's life calmed down a bit."
    "He started working in Vivian's shop. Which, despite Lua's opinions, is doing quite okay."
    "This is a great opportunity for Thiu to hone his abysmal social skills."
    "And to earn some money, and working experience, and all that..."
    "Though honestly, he just feels happy to be part of the outside world again,"
    "...after rotting away in his hole of a home for a decade."
    "Overall Thiu is hopeful for the future. Maybe things will be okay?"

    scene merge with fade

    $ persistent.merge = True

    "And on the days he feels lonely and devastated, Thiu starts talking to himself."
    "The neighbors think he is a creepy weirdo, but at least Thiu understands Thiu."

    "MERGE END."

    window hide
    pause

    play sound "audio/Coins (21).wav"

    return

label narcissus:

    show h smilelow
    h "Aaaah, but Lua is kinda creepy..."
    show h sorry
    h "Who knows what he'll do if I just tell him off...."
    show s sorry
    s "You got a point..."
    show h unhappy
    h ".........................."
    show s sad
    s "....................................."
    show h mock
    h "How about--"
    show s docile
    s "Do you think--"
    show h laugh
    h "Oh, hahha!! You go first!"
    show s shrug
    s "What if you just never show up?"
    show h kindasmile
    h "Yeah, it's not like he knows where we live."
    show s smile
    s "Yeah yeah! Like... Let's just avoid the mage shops until we can move away!"
    show h unamused
    h "Exactly!! Screw this city anyway. It's not like I have a job, or friends, or anything here."
    show s dontcare
    s "That's right! We're here just because it's cheap! We can find another cheap shit hole to waste away in!"
    show h shruglaugh
    h "Let's elope!"
    show s laugh
    s "Yes!! Let's elope!!"
    show h lol
    play sound "audio/_laugh.mp3"
    h "HAHHA!!" with vpunch
    show s smile
    s "Let's start looking right now!"
    hide h
    hide s
    with dissolve

    "Thius open the laptop and browse for cheap apartments."

    scene black with fade

    "But as it turns out, you don't just get a place simply because you need one."
    stop music fadeout 2.0
    "Especially with a budget like Thiu's."

    play music "audio/07_battle.mp3" fadein 2.0
    scene home_clean with fade

    "So roughly a week later, Thius are still actively looking."
    "But someone was looking for them too."
    "And this someone had more success in his search."

    play sound "audio/knockfast.mp3"

    l "Open up. I know you're in there."
    show s confused at righty
    show h surprised at lefty
    with dissolve
    s "!!!"
    l "Open the door or I'll huff and puff your house down, hahha!!"
    show s worry
    s "........."
    show h unsure at faceright
    h "..............I'll get it."
    play sound "audio/opendoor.mp3"
    show h laugh at righty, faceleft
    hide s
    show l smile at lefty, faceright
    with dissolve
    h "Hiiiiii Lua! Fancy seeing you here!"
    show h smile
    h "In my house."
    show h smilelow
    h "Uninvited..."
    show l mock
    l "Yeah, it's uncomfortable, isn't it?"
    show l fake_laugh
    l "Remember that feeling the next time you want to barge in to my house."
    show h kindasmile
    h "...I didn't exactly plan on doing that anytime soon."
    show h nervous
    h "Or like... ever."
    show l lol
    l "That's weird. I could've sworn we had agreed you'd come help me out with a little potion."
    show l sheepish
    l "Did you forget? Breaks my heart, my friend."
    show h laugh
    h "Ahahha... Right... Mind if I ask?"
    show h unhappy
    h "How did you find out where I live?"
    show l playful
    l "I would not call myself a mage if I couldn't sense the residue of my own magic."
    show l smilesmile
    l "But the fact that this is your home was news to me. All though I kinda figured."
    show l chuckle
    l "It's cleaner than I thought in here."
    show h whatever
    h "....Thanks?"
    show l pleased
    l "Pleasantries aside, shall we get to work?"
    show l think_pleased
    l "I went ahead and prepared the new batch and all without you."
    show l smilesmile
    l "So all you have to do is come over and have a little sip."
    show l smug
    l "It won't take long."
    hide h
    hide l
    with moveoutleft
    show s ashamed with moveinright
    s "(Oh, crap... We're never getting rid of this jerk.)"
    show s confused
    s "(Isn't there something I can say??)"
    hide s thefuck with moveoutright
    show h shruglaugh at righty
    show l smug at lefty, faceright
    with moveinleft
    h "Actually... About the deal we made I--... uhhh...."
    show s ashamed at center
    show l smile at left, faceright
    show h surprised at right
    play sound "audio/echowhip.wav"
    s "ABOUT THAT!!" with hpunch
    show s nervous_smile
    show h unsure
    s "I-I had something I wanted to say about that!!"
    show l happy
    l "Oh? Hello miserable one."
    show l mock
    l "Haven't seen you since you ran off without as much as a goodbye."
    show s nervous_smile_away
    s "Right..."
    show s angry
    s "Anyway I wanted to say..."

    menu:

        "Claim the contract is invalid.":

            show s shrug
            s "It-!! Our contract doesn't even exist!"
            show s sad
            s "We don't owe you any favors, or money, or poison drinking, or anything!"
            show l lookup
            l "That's a bit rude."
            show l bored
            l "I gave you my time and effort."
            show l pity
            l "And you say I deserve no compensation at all?"
            show s dontcare
            s "Well... I'm not saying {i}that{/i}, but I don't think you deserve to poison the other me."
            show l lol
            l "My, who made you the divine judge of who deserves what?"
            show l smilesmile
            l "Maybe you should pull your head out of you ass?"
            show s embarrassed
            play sound "audio/_hiss2.ogg"
            s "I-???! {b}Fuck you man!!{/b}" with hpunch
            show h lol
            play sound "audio/_laugh.mp3"
            h "HAHAHA!!" with vpunch
            show s thefuck at faceright
            play sound "audio/_hiss1.ogg"
            s "And you laugh!? How dare you!"
            show h nervous
            h "Sorry, sorry!"
            show l chuckle
            l "If that was all you had to say, mind pissing off?"
            show l playful
            l "Us happy ones have business to attend to."
            show s confused at faceleft
            s "But-..? I--?? But there's no contract!"
            show l sheepish
            l "That's nice. Go tell someone who cares."
            show l think_pleased
            l "In the meanwhile, Thiu here needs to help me with something."
            show l pity
            l "But don't you worry, homebody. He won't be long!"
            show s ashamed
            s ".............."
            show h smilelow
            h "......Don't worry, me."
            show h smilecalm
            h "I was a bit sick last time, but it was okay."
            show h smilegentle
            h "I'll drink it one last time, and then we'll move out."
            show s hurt at faceright
            s "...{i}Sighhh.{/i}"
            show h shruglaugh
            h "Thanks for sticking up for us though. You're soooo brave! Hehe!"
            show s think
            s "And now you're making fun of me..."
            show h laugh
            h "Geez, I was not!"
            show h smile
            h "I'll see you in a bit!"
            show s sorry
            s "See you..."

            stop music fadeout 2.0
            scene black with fade

            "But as it just so happens, that batch of poison was quite bad."
            "Lua had gotten over confident seeing how well Thiu survived the previous one."
            "So this one was way too deadly. Thiu's life ended just like that."
            "Yup. Just like that."
            "And what did the remaining Thiu think about that?"
            "Well he wasn't very happy at all. His depression got the better of him."
            "I don't even wanna tell you this stuff, it all seems so melodramatic."
            "But that's what happened. It's all very saaaad, sad, sad."
            "What did Thiu think was going to happen when he made that statement about the contract?"
            "Did he expect Lua to go \"Aw, gee. You're right! Sorry mate! I'll just go now.\""
            "Well, since there are no more Thius left to play, it's game over."

            play sound "audio/_metal.mp3"

            "BAD END."

            return


        "Trick the bastard.":

            show s thefuck
            s "I told you already! I want this spell undone!"
            show h confused
            play sound "audio/echo.mp3"
            h "HUH?!" with vpunch
            show s explain
            s "Oh, shut up! Like this is somehow news to you!?"
            show h surprised
            h "!!!"
            show l bored
            l "You're still on about that?"
            show l complain
            l "What am I supposed to do?"
            show s scold
            s "Undo the damn spell, that's what!"
            show l playful
            l "Ahh, but here's the thing... Other Thiu here has already paid me and everything."
            show s fuckyou
            s "No he hasn't! You're clearly in the middle of it!"
            show s yeahright
            s "And like it matters anyway??"
            show l pity
            show s bitetongue
            l "Still, all of you agreed to this. Only half of you wants it reversed."
            show h pissed
            h "No, I'm fine with it."
            show h nervous
            h "I'd like to merge too..."
            show l down
            l "Really?"
            show h unamused
            h "Yeah... It's been pretty tiresome like this."
            show l fake_laugh
            l "Y'know I warned you about the tiresomeness."
            show l happy
            l "My other offer still stands, mind you."
            show l lol
            l "We can get it over with right now!"
            show h kindasmile
            h "No, that's okay. I'd like to regain all of my life force, so I'd rather merge."
            show l whatever
            l "Huh."
            show l smilesmile
            l "Well that's unfortunate... Because I don't feel like undoing the spell."
            show s confused
            s "Huh?"
            show l ugh
            l "What do you take me for? A vending machine?"
            show l playful
            l "Or better yet, what makes you think I {i}can{/i} reverse it?"
            show h confused
            h "Wait, what?? You can't??"
            show l down
            l "I can, obviously. But I don't think I ever said I can."
            show l chuckle
            l "Yet here you are assuming."
            show s angry
            s "Like it costs you anything anyway! Don't be so difficult!"
            show l mock
            l "I just don't feel like helping when I'm being asked this way."
            show s thefuck
            play sound "audio/_hiss2.ogg"
            s "{b}FINE!!{/b} We don't need your help anyway!"
            show s scold
            s "But don't expect other me to help you either, until you merge us back!"
            show h sneaky
            h "That's right! I won't test any poison until I'm whole again!"
            show l lol
            l "That's cute. You think you're so irreplaceable, do you?"
            show h unhappy
            h "........"
            show l smilesmile
            l "I'll sucker another moron into testing my potion, meanwhile you're stuck like that until the day you die."
            show l think_pleased
            l "Which, by they way, should be around your forties."
            show l mock
            l "So I wonder which one of us can afford to throw their weight around?"
            show l playful
            l "Kinda seems like-, {i}ohh!{/i}"
            show l happy
            l "Kinda seems like that would be me!"
            show s sad
            s ".........."
            show h unsure
            h "..............."
            show l playful
            l "Well, I hate to disappoint you, but it looks like you're going to remain split."
            show s confused
            s "What! Why?!"
            show l ugh
            l "Because I say so."
            show l pity
            l "Goodbye my friends!"
            show l lol
            play sound "audio/_laugh.mp3"
            l "Hahahahhaha!!!" with vpunch

            hide h
            hide s
            hide l
            with dissolve
            stop music fadeout 2.0
            "Lua laughs all the way back home."

            show h smilelow at righty
            show s docile at lefty, faceright
            with dissolve
            h ".............."
            show s smile
            play music "audio/13_where.mp3" fadein 2.0
            s "...................Heh."
            show h lol
            play sound "audio/_nervousbubbles.mp3"
            h "What a moron!" with vpunch
            show s laugh
            play sound "audio/_laugh.mp3"
            s "HAHA HAH HA HAAHAH!!!" with hpunch
            show h shruglaugh
            play sound "audio/_nervousbubbles.mp3"
            h "HAHAHAH!!! Oh man!!" with vpunch
            show s smile
            s "I can't believe it was that easy!"
            show h unsure
            h "All though he's right about us dying early."
            show s smiledown
            s "That's okay."
            show h puzzled
            h "........Not really though?"
            show s dontcare
            s "Whatever. We could choke on some spit tonight while brushing our teeth."
            show s explain
            s "And that might happen even if we merged."
            show s scold
            s "So what?"
            show h smilegentle
            h "Alright, I guess it's like that."
            show h sneaky
            h "Let's just be happy Lua is off our backs."
            show s laugh
            play sound "audio/_laugh.mp3"
            s "That's right!!"
            s "Now we can play video games and watch movies and hang out!"
            show h smile
            h "And eat fish and go for walks and learn to cook!"
            show s thefuck
            play sound "audio/_thunk.mp3"
            s "AND {b}SCREW!!{/b} Finally!!!" with vpunch
            show h lol
            h "And that too!"
            show s laugh
            play sound "audio/_nervousbubbles.mp3"
            s "HAHAHAHA!!"

            scene narcissus with fade

            $ persistent.narcissus = True

            "And that's how the Thius spend their days."
            "Friendless and without any goals in life."
            "But who needs friends when you can laugh at your own jokes?"
            "And as for goals, well... "
            "Maybe someone better can reach some, because Thiu is only reaching for the potato chips."
            "Ultimately, Thiu's life is an utter waste."
            "But he sure is happy to waste it with himself by his side."

            "COUPLE END."

            window hide
            pause

            play sound "audio/Coins (21).wav"

            return
