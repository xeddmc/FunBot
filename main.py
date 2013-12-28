import sys
import socket
import string
import time
from random import randint
import pprint
import connection
import functions

def main():
        f = open('log.txt', 'w') #Opening the log txt file

        s = connection.get_connection()
        connection.announce(s)

        # Loop
        while 1:
                text = s.recv(2040)
                print text # This is the consoles output
                user = text.split('!')[0][1:] # User is the name of the person who sent the last message
                f.write(text) # Write the text to file
                if text.find('PING') !=-1: # This is to respond to the server when pinged, otherwise the bot will get kicked.
                        s.send("PONG %s\r\n")
                if text.find('!help') !=-1:
                        functions.list(s)
                if text.find('!credits') !=-1:
						functions.credits(s)
                if text.find('!tip') !=-1:
                        functions.tips(s)
                if text.find('!hello') !=-1:
                        functions.greet(s, user)
                if text.find('!leetmeter') !=-1:
                        functions.leet(s)
                if text.find('!MystPhysX') !=-1:
                        functions.myst(s)
main()