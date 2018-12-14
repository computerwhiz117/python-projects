# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character(_("Hana"), color="#c8ffc8")
define c = Character(_("Carla"), color="#c8ffc8")
define m = Character(_("Mei"), color="#c8ffc8")

# This is a variable that is True if you compared a visual novel to a book
# otherwise

default book = False


# Position for the characters

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

# The game starts here.

label start:

    # Start by playing music.
    play music "itty-bitty-8-bit.mp3"

    scene anime-classroom
    with fade

    "Remember class, there's an upcoming project that you need to present it's about showing your own program."
    "Be sure to make your program so you can present it to class."
    "Also this is to show yourself to the real world that you can write fantastic programs."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hana
    with dissolve

    # These display lines of dialogue.

    h "Geez I can't believe taking a programming class can be this hard."

    h "I'm really bad in programming and I don't even know what to do with the project my teacher is giving us."

    show hana at slightright

    show carla at slightleft
    with dissolve

    c "Hey I heard that you are not really good at programming."
    h "Yeah I'm very bad at programming."
    c  "Well there's a club that I'm opening up related to computer programming."
    h "Oh really then I'll go."
    c "Awesome"
    c "Oh we haven't know each other very well so I might as well introduce myself."
    c "My name is Carla and I am an expert in computers and I love programming."
    h "Oh really awesome."
    h "Well my name is Hana and I am interested in using computers but I don't program very well."
    c "Not to worry I'll make sure that you are ready to program when you join my club."
    h "Oh great I'm glad I found someone that can help me become a better programmer, so I'll definitely join your club."
    c "Right on, so let's go to the classroom where we can start our club especially that class is over."
    h "Alright"

    scene anime-classroom2
    with fade
    play music "theme-for-harold.mp3"

    show hana-smile at slightright
    with dissolve

    show carla-heroic at slightleft
    with dissolve

    c "Well now we can start our first club meeting"
    c "We are The Open Source Club"
    h "Awesome but...."

    menu:
        "What is open source?":
         jump question

        "Open Source!?":
         jump unsure

label question:
    show carla-lookin-at-you at slightleft
    with dissolve

    c "Well looks you don't know what open source is."
    c "I'll tell it to you this way."
    c "Open source means that the software can be shared by others for free."
    c "Like for example, I can share you the source code for a program that I created and you can review the code and make it better."
    h "Oh wow cool, so that means I can share software with others."
    h "Amazing, so that means we can share our code with each other."
    c "Exactly"
    c "It's basically the best way to learn how to code if you contribute to open source"
    h "Amazing I want to learn open source"
    c "Well you came to the right place, so let's start our club now."

    jump member

label unsure:
    show carla-lookin-at-you at slightleft
    with dissolve

    c "Looks like you never heard the term open source."
    c "Open source means that the software can be shared by others for free."
    c "There is also another term of computer software that's similar to open source which is called free software where the user can run, distribute, study, change, and improve the software."
    h "So there's two kinds of programs open source and free software."
    c "Pretty much, yeah."
    h "Oh wow cool, this seems very interesing."
    h "So if I learn open source and free software that means I can become amazing in computer programming"
    c "That's the beauty of free and open source no matter if you're a beginning programmer or an experienced programmer you can contribute to code and make it your own."
    h "So what are we waiting for, let's write some code."
    c "That's what I want to hear."
    c "So let's start our club now."

    jump member

label member:
    show carla at slightleft
    with dissolve

    c "Well Hana, I want to meet you another club member"
    show mei
    with dissolve

    m "Hello I'm Mei, I do love programming and I am ready to contribute to open source"
    show hana-happy at slightright
    with dissolve
    h "Nice to meet you Mei"
    c "First we are going to learn the basics of Linux and Git"
    c "Then we'll come out with ideas for our upcoming project for programming class"
    c "Finally we'll start writing our program"
    hide hana-happy at slightright
    with dissolve
    show hana-heroic at slightright
    with dissolve
    h "Alright let's do it"
    hide mei
    with dissolve
    show mei-heroic
    with dissolve
    m "I'm ready to go do some code"

    jump basic

label basic:
    show carla at slightleft
    with dissolve
    hide hana-heroic at slightright
    with dissolve
    show hana-smile at slightright
    with dissolve
    hide mei-heroic
    with dissolve
    show mei
    with dissolve

    c "So let's start with using Linux"
    c "Linux is basically a kernel and it's used on popular distributions especially Ubuntu"

    h "So Linux is a kernel that powers open source operating systems"
    c "Exactly"

    m "Also Linux powers servers and smartphones."
    h "Oh wow, I can't believe Linux is a major thing in the open source world."
    c "Yup and many developers use Linux to write software because it's open source."
    h "Cool."
    m "And Linux is the best OS to do programming."
    c "Now I want to talk about Git."
    c "Git is a version control system that track changes in your program."
    c "It's basically something where you just store your code like to git repository sites like GitHub."
    m "The best thing is anybody can look at your code and can contribute to it to make it better."
    h "This is amazing."
    h "So that means anybody can see my code especially when I'm coding."
    c "Yup and collaboration helps make your program better."
    c "So now I teached you the basics of Linux and Git now let's plan our project"

    jump project

label project:
    play music "heros-day-off.mp3"

    show carla-heroic at slightleft
    with dissolve
    c "Alright now let's work on our project."
    c "There are two ideas I have of writing our program one easy and the other is somewhat difficult."
    c "We can do a peer-to-peer file sharing program that allows the computer to share with each other via a server."
    c "Or we can do a web browser which is built on top of Chromium."
    c "The peer-to-peer program is going to be written in Java and Python which is easy and takes less time to work on because both of the programming languages are simple."
    c "The web browser has to be written in C and Python which even though Python is very easy to code but C can be difficult."
    c "We can complete the Python part in seconds but C is going to take us a lot of time to program in the club."
    c "So Hana and Mei which project you want to do?"

    menu:
        "Peer-to-peer program":

            jump transfer

        "Web browser":

            jump web

label transfer:

    show carla at slightleft
    with dissolve
    c "Alright the peer-to-peer transfer program it is."
    c "We'll have this project finished in no time because Java is easy as well as Python."
    show hana-happy at slightright
    with dissolve
    h "Oh yeah we are making a peer-to-peer program"
    m "I'm so excited!!!!"
    c "So we'll use our computers that I brought to class which are running Ubuntu."
    c "I even installed NetBeans and Atom so we can work on our program."
    h "So it's a laptop."
    c "Of course"
    m "Nice so we can work together on our program."
    c "That's right Mei."
    c "Since we are going to program in Java for the client-side of the peer-to-peer program."
    c "We barely have to compile everything because Java can run on a virtual machine."
    h "Nice so we can work on this program like a piece of cake."
    m "Oh yeah!!!!!"
    c "Now let's start programming."

    jump programming1


label web:
    show carla at slightleft
    with dissolve
    c "Alright web browser it is."
    c "Luckily we can use Python for the server-side of the project because it's easy."
    hide carla at slightleft
    with dissolve
    show carla-unamused at slightleft
    with dissolve
    c "But it's going to take us a lot of time to work on this project because C can somewhat be complicated."
    show hana-worried at slightright
    with dissolve
    h "Since the web browser can be a complex project, I'm worried that we might not be able to finish with the project at this time."
    show mei-worried
    with dissolve
    m "Oh no I didn't realized making a web browser can be complicated, I thought it was going to be easy."
    hide hana-worried at slightright
    with dissolve
    show hana-angry at slightright
    with dissolve
    h "Well why you decided to pick this idea even though it will be time-consuming for us to work on the web browser."
    m "I thought it was going to be easy because I love to go on the internet and I think making the web browser is a great idea."
    hide carla-unamused at slightleft
    with dissolve
    show carla-lookin-at-you at slightleft
    c "That's enough, both of you decided to pick on this project so we're going as it is."
    hide hana-angry at slightright
    with dissolve
    show hana at slightright
    h "Sorry about that"
    hide mei-worried
    with dissolve
    show mei
    with dissolve
    m "Me too."
    hide carla-lookin-at-you at slightleft
    with dissolve
    show carla-heroic at slightleft
    with dissolve
    c "We'll work hard on our web browser program."
    hide hana at slightright
    with dissolve
    show hana-heroic at slightright
    with dissolve
    h "Alright let's do this."
    hide mei
    with dissolve
    show mei-heroic
    with dissolve
    m "Oh yeah!!!!!!!!!!!!!!!"
    hide hana-heroic at slightright
    with dissolve
    show hana-smile at slightright
    with dissolve
    hide mei-heroic
    with dissolve
    show mei
    with dissolve
    hide carla-heroic at slightleft
    with dissolve
    show carla at slightleft
    with dissolve
    c "We'll use our computers that I brought which are running Ubuntu."
    c "I installed Atom on them so we can work on the project."
    c "Since we are going to program in C for the client-side of the web browser."
    c "We need to use the GNU GCC compilers to compile our web browser."
    c "Because in C we need to compile the program after we make it in code."
    h "This may be a little complicated but we can work on this project."
    m "Alright let's do this!!!!!!!!"
    c "Now let's start programming."

    jump programming2


label programming1:
    play music "wwwwub.mp3"

    hide carla at slightleft
    with dissolve
    hide carla-lookin-at-you at slightleft
    with dissolve
    show carla-heroic at slightleft
    with dissolve
    c "I already started the work on the peer-to-peer project so we're going to complete the program together."
    c "Hana you will work on the Python part because it's the easiest one and you can understand it better."
    show hana-heroic at slightright
    with dissolve
    h "Alright I'll do it."
    hide hana-heroic at slightright
    with dissolve
    show hana-smile at slightright
    with dissolve
    h "I should be able to work on this part on Python because I learned about programming in Python since middle school."
    c "And that's why I picked you to work on Python because I think you can work on this part of the program because Python is a simple programming language."
    c "As for you Mei you're going to work on the Java part of it because you tell me that you are very influent on Java and can write programs on that programming language."
    show mei-heroic
    with dissolve
    m "Yup I know everything I know about Java."
    m "So I should do everything I can to write this program in Java."
    c "That's what I love to hear."
    hide carla-heroic at slightleft
    with dissolve
    hide mei-heroic
    with dissolve
    show mei
    with dissolve
    show carla at slightleft
    with dissolve
    c "Well I'm going to share you girls my source code via Git so we can work on this project."
    c "I'm doing it right now."
    c "Here we go now you can see the project on GitHub."
    h "Alright so now we can work on the program."
    m "Git is very fast and we can work on the project with no worries."
    h "Alright I see the Python code for the peer-to-peer program."
    h "I'm working on it right now."
    m "I see the Java code for the peer-to-peer program."
    m "I'm working on it"

    "After seconds later"

    h "Alright I was able to finish the Python part of the project and it was very easy."
    m "I finished the Java part of the project and it was very simple everthing ran very well."
    c "Great work you too now let's test the program."
    c "Now you need to push the Git respository to me so I can see it."
    h "Alright"
    m "Yes ma'm"
    c "I see your changes in the code and now I'm going to test it."
    c "Yup looks like the program is working."
    c "Awesome work."
    c "Finally we need to add a license to our program"
    c "This shows other developers around the world that they can redistribute the code for any purpose."
    c "I'll put this program under GNU GPLv2."
    h "That is great so that means anyone can see our code."
    c "Exactly"
    m "Yup and this makes our program free software so the software can be distributed for free."
    c "Now let's present the peer-to-peer program to class."

    jump presentation1


label programming2:
    play music "wwwwub.mp3"

    hide carla at slightleft
    with dissolve
    hide carla-lookin-at-you at slightleft
    with dissolve
    show carla-heroic at slightleft
    with dissolve
    c "I already started the work on the web browser project so we're going to complete the program together."
    c "Hana you will work on the Python part because it's the easiest one and you can understand it better."
    show hana-heroic at slightright
    with dissolve
    h "Alright I'll do it."
    hide hana-heroic at slightright
    with dissolve
    show hana-smile at slightright
    with dissolve
    h "I should be able to work on this part on Python because I learned about programming in Python since middle school."
    c "And that's why I pick you to work on Python because I think you can work on this part of the program because Python is a simple programming language."
    c "As for you Mei, you are going to work on the C part of it because you tell me that you can program in C."
    show mei-worried
    with dissolve
    m "I maybe good in C but it's complicated for me and I literally messed up when I compile the code especially that's it's so hard."
    hide carla-heroic at slightleft
    with dissolve
    show carla-lookin-at-you at slightleft
    c "Well you decided that you wanted to work on the web browser program so you're going to be working on it."
    hide mei-worried
    with dissolve
    show mei
    with dissolve
    m "I might as well do it."
    hide mei
    with dissolve
    show mei-heroic
    with dissolve
    m "But I'll do my best work on this part of the project in C."
    hide carla-lookin-at-you at slightleft
    with dissolve
    show carla-heroic at slightleft
    with dissolve
    c "That's I want to hear."
    hide carla-heroic at slightleft
    with dissolve
    show carla at slightleft
    with dissolve
    hide mei-heroic
    with dissolve

    c "Well I'm going to share you girls my source code so we can work on this project."
    c "I'm doing it right now."
    c "Here we go now you can see the project on GitHub."
    h "Alright so now we can work on the program."
    m "Git is very fast and we can work on the project with no worries."
    h "Alright I see the Python code for the web browser."
    m "I see the C code for the web browser."
    hide mei
    with dissolve
    show mei-worried
    with dissolve
    m "But this is going to be very complicated for me because C can be hard sometimes."
    hide carla at slightleft
    with dissolve
    show carla-lookin-at-you at slightleft
    with dissolve
    c "Hang in there Mei, I know C can be complicated but you are going to do well."
    hide mei-worried
    with dissolve
    show mei
    with dissolve
    m "Alright I'll start working on the C part of the program."

    "Minutes later"

    h "Alright I was able to finish the Python part of the project and it was easy."
    m "I'm still working on the C part of the project and right now everything is good."
    hide met
    with dissolve
    show mei-worried
    with dissolve
    m "But I don't know if the program will run because I have to compile it."
    m "And I may run through errors."
    hide carla at slightleft
    with dissolve
    show carla-lookin-at-you at slightleft
    with dissolve
    c "Hang in there Mei, C can be complcated but you can make the program work, you can do it."
    hide mei-worried
    with dissolve
    show mei-heroic
    with dissolve
    m "I'll continue my best of writing this program in C"
    hide mei-heroic
    show mei
    with dissolve

    "An hour later"

    m "Well I finished the C part of the web browser."
    h "That's great to hear."
    m "Now I'm going to compile the program."
    hide mei
    with dissolve
    show mei-worried
    with dissolve
    m "Oh no, the web browser is running with errors so the compile failed."
    hide hana at slightright
    with dissolve
    show hana-worried at slightright
    with dissolve
    h "That's not good."
    hide carla at slightleft
    with dissolve
    show carla-lookin-at-you at slightleft
    with dissolve
    c "Looks like you need to check for errors on your code especially with debugging."
    hide mei-worried
    with dissolve
    show mei
    with dissolve
    m "Looks like I'm going to have to check for errors and fix them and I'll make sure to use debug."
    hide carla-lookin-at-you at slightleft
    with dissolve
    hide hana-worried at slightright
    with dissolve
    show carla at slightleft
    with dissolve
    show hana at slightright
    with dissolve

    "Minutes later"

    m "Alright I got the errors fixed and and now the program compiles."
    hide hana at slightright
    with dissolve
    show hana-happy at slightright
    with dissolve
    h "Awesome so now we have a working web browser."
    c "Awesome work you too now let's test the program."
    c "Now you need to push the Git respository to me so I can see it."
    hide hand-happy at slightright
    with dissolve
    show hana-smile at slightright
    with dissolve
    h "Alright"
    m "Yes m'am"
    c "Alright I see your changes in the code and now I'm going to compile the program and test it."
    c "Yup it works"
    c "Awesome work"
    c "Finally we need to add a license to our program."
    c "This shows other developers that they can share and redistribute the code for any purpose."
    c "I'll put the client-side of our web browser under the MIT License and the server-side of the browser under GNU GPLv2."
    h "That is great so anybody can see our code."
    c "Exactly"
    m "That means the program is going to be distributed as free-and-open-source software."
    c "Now let's present our web browser to class."

    jump presentation2


label presentation1:
    scene anime-classroom
    with fade
    play music "free-software-song.ogg"

    "Alright class today you will be presenting your project."
    "First up we have Carla, Mei, and Hana."
    "So please present your project."


    show carla at slightleft
    with dissolve
    show mei
    with dissolve
    show hana-smile at slightright
    with dissolve

    c "Hello class today we are going to present our project."
    m "It's a peer-to-peer program"
    h "And it allows computers to be shared to each other"
    c "We'll demonstrate this by using two computers running our program."

    "After demonstation of the program, the class applauses."
    "The class decided to give you girls questions."
    "One of the classmates answered"
    "What programming language is it programmed in and can we be able to use the program?"

    c "The program is written in Java and Python."
    c "And also our program is written in GNU GPLv2 meaning that you can see the source code and redistribute it that suits your needs."

    "The class applauses."

    "After class is over"

    hide hana-smile at slightright
    with dissolve
    show hana-happy at slightright
    with dissolve

    h "Well looks like we made a great team."
    c "We sure did"
    m "Well looks like we'll do more open source project in the future since we have made the club dedicated to open source."
    c "I'm hoping we can do more free-and-open-source projects in the future."
    h "I'll definitely continue working with you girls on writing programs dedicated to open source."
    h "Because of this, now I'm very confident in programming now."
    c "That's what I love to hear."
    c "Now we can work on more free-and-open-source projects in the future especially with our club."
    h "Looks like we'll be working collaborative on open source."
    m "Oh yeah"
    c "Now let's call this a day and let's go home."

    scene black
    with dissolve

    "Now Hana and their new friends Carla and Mei now work together on writing free-and-open-source projects"
    "{b}The End.{b}."

    return

label presentation2:
    scene anime-classroom
    with fade
    play music "free-software-song.ogg"

    "Alright class today you will be presenting your project."
    "First up we have Carla, Mei, and Hana."
    "So please present your project."


    show carla at slightleft
    with dissolve
    show mei
    with dissolve
    show hana-smile at slightright
    with dissolve

    c "Hello class today we are going to present our project."
    m "It's a web browser"
    h "It's built on Chromium so you can browse websites at fast speed."
    c "We'll demonstrate this by showing the web browser to everyone in the class."

    "After demonstation of the program, the class applauses."
    "The class decided to give you girls questions."
    "One of the classmates answered"
    "What programming language is it programmed in and can we be able to use the program?"

    c "The program is written in C and Python."
    c "And also our program is written in the MIT License for the client-side of the program meaning that it's simple and permissive and you can do anything you want with the code."
    c "As well as GNU GPLv2 for the server-side of the program meaning that you can see the source code and redistribute it that suits your needs."

    "The class applauses."

    "After class is over"

    hide hana-smile at slightright
    with dissolve
    show hana-happy at slightright
    with dissolve

    h "Well looks like we made a great team."
    c "We sure did"
    m "Well looks like we'll do more open source project in the future since we have made the club dedicated to open source."
    c "I'm hoping we can do more free-and-open-source projects in the future."
    h "I'll definitely continue working with you girls on writing programs dedicated to open source."
    h "Because of this, now I'm very confident in programming now."
    c "That's what I love to hear."
    c "Now we can work on more free-and-open-source projects in the future especially with our club."
    h "Looks like we'll be working collaborative on open source."
    m "Oh yeah"
    c "Now let's call this a day and let's go home."

    scene black
    with dissolve

    "Now Hana and their new friends Carla and Mei now work together on writing free-and-open-source projects"
    "{b}The End.{b}."

    return
