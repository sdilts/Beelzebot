#!/usr/bin/python3

from character import Character
import server1 as server
import client
import sys
import board

def run_game(ipAddr, portNum):
    b = board.Board()
    bot = Character(ipAddr, portNum, b)
    try:
        while (not b.at_end(bot.position)) and bot.isAlive():
            bot.take_turn()
            b.print_stats()
        if not bot.isAlive():
            print("Done!")
            client.say_phrase(ipAddr, portNum, "Better luck next time!", False)
        else:
            client.say_phrase(ipAddr, portNum, "We are victorious!", False)

        if server.wait_for_command.server:
            server.wait_for_command.server.stop()
    except Exception as e:
        print(str(e))
        if server.wait_for_command.server:
            server.wait_for_command.server.stop()

run_game(sys.argv[1], sys.argv[2])
