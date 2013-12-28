import requests
import connection
from random import randint
	
def credits(s):
	connection.send_channel(s, "My creator is Cephon!")

def tips(s):
	connection.send_channel(s, "Please send your tips to:")
	connection.send_channel(s, "ELucyYgmNsEa12wrZYnhtvwuRPWcDomxsF.")

def list(s):
	connection.send_channel(s, "These are the main bot comamnds:")
	connection.send_channel(s, "\t!leetmeter: See how l33t you are.")
	connection.send_channel(s, "\t!hello: Say hello to me!")
	connection.send_channel(s, "\t!credits: Find out who made this bot!")
	connection.send_channel(s, "\t!tip: Show the address to tip me at!")

def greet(s, user):
	connection.send_channel(s, "Hello, " + user + "!")
	
def leet(s):
	connection.send_channel(s, "You are " + str(randint(1,100)) + "% leet!")
	
def myst(s):
	connection.send_channel(s, "Sawg - MystPhysX 2013")
