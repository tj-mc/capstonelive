#!/usr/bin/python



import os
import random
import time
import datetime
import urllib2
import ssl

os.system("clear") 

#add your own web server here
webServer = "http://www.google.com"

voices = ['Fred', 'Daniel', 'Alex', 'Karen', 'Fiona', 'Victoria', 'Tessa', 'Samantha',]

counter = 1
timeout = 5 #seconds

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("***************************************")
print("* CapstoneTTS Version4 for Python2.7  *")
print("***************************************")


print("+-----------------------------------------+")
for i in range(5):
	open(os.path.expanduser('~/desktop/{}.wav'.format(i + 1)), 'a').close()
	print("| Wrote initial file {}.wav to ~/desktop/  |".format(i + 1))
print("+-----------------------------------------+")


while True:

	try:
		startTime = time.time()
		phrase = (urllib2.urlopen(webServer + "/TTSGet", context=ctx, timeout=timeout).read()).decode()
		endTime = time.time()
		responseTime = round((endTime - startTime), 2)
	except Exception:
		print("***** CONNECTION FAILED @ {} *****".format(time.asctime(time.localtime(time.time()))))
		time.sleep(1)
		print("Retrying...")
		continue


	outputMessage = "Server reponded on {} after {} seconds: ".format(time.asctime(time.localtime(time.time())), responseTime)


	if not phrase:
		print(outputMessage + "Nothing new.")
		continue


	else:

		voice = voices[random.randint(0, 7)]

		path = os.path.expanduser('~/desktop/{}.wav'.format(counter))

		cmd = 'say -v {} -o {} --data-format=LEF32@44100 "{}"'.format(voice, path, phrase)
		
		#Handle unexpected errors from the system call
		try:
			os.system(cmd)
		except:
			print("Unexpected error on system call.")
			continue

		print(outputMessage + 'New message recieved: "{}"'.format(phrase))
		print('Overwrote file {}.wav with voice "{}"'.format(counter, voice))

		counter += 1

		if counter == 6:
			counter = 1
