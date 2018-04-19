import random
import re
import time
import server
import client

# riddles courtesy of The LOTR and The Hobbit:
riddles = [("A box without hinges, key, or lid, yet golden treasures inside is hid", re.compile('.*egg *.*', re.IGNORECASE)),
           ("What has roots as nobody sees, Is taller than trees, Up, up it goes, And yet never grows?", re.compile(".*mountain*.*", re.IGNORECASE)),
           ("Voicelss it cries, Wingless flutters, Toothless bites, Mouthless mutters", re.compile(".* wind *.*", re.IGNORECASE)),
           ("Speak Friend, and enter", re.compile(".*friend *.*", re.IGNORECASE)),
           # now for one I found off of the internet:
           ("I have keys but no locks. I have a space but no room. You can enter, but can't go outside. What am I?", re.compile(".*keyboard *.*", re.IGNORECASE))]

# random.shuffle(riddles)


def say_stuff(message, ipAddr, portNum):
    c = client.Client(ipAddr, portNum, message,
                      False)
    c.start()
    time.sleep(2)

def get_riddle():
    global riddles
    return random.choice(riddles)

def get_riddle_part(riddle):
    return riddle[0]

def check_riddle(guess):
    global riddles
    for riddle, regex in riddles:
        if regex.match(guess):
            return True
    return False

denials = ["No! You shall never leave!", "Mwahaha! Thats not it!"]

def play_riddle(ip, port, riddle):
    again_command = re.compile(".*say *.* again *.*", re.IGNORECASE)
    give_up = re.compile("I give up", re.IGNORECASE)
    say_stuff("You find yourself in a dark room. There are two creepy eyes staring out at you from the darkness. A voice says \"I will let you leave if you answer me a riddle.\"", ip, port)
    correct = False
    say_stuff(riddle[0], ip, port)
    while not correct:
        command = server.get_command(ip, port)
        if again_command.match(command):
            say_stuff(riddle[0], ip, port)
        elif give_up.match(command):
            say_stuff("You are doomed! I will exact my price in blood!", ip, port)
        elif riddle[1].match(command):
            say_stuff("The creepy voice says \"How did you know? I guess I will keep my promise\"", ip, port)
            say_stuff("The room becomes bright, and you can see your way out", ip, port)
            correct = True
        else:
            to_say = random.choice(denials)
            say_stuff(to_say, ip, port)

if __name__ == "__main__":
    import sys
    play_riddle(sys.argv[1], sys.argv[2], get_riddle())
