import socket 

def command(c,e,args,json):
	try:
		c.privmsg(e.target,'.:: '+ str(args[1]) +' ::.')
	except IndexError:
		c.privmsg(e.target,'Please Specify a Message to Say')