# capstone.live

Source code for an interactive audio-visual performance with Python and TouchDesigner. Audience members submit short messages via a web app, which is shown on screen using TouchDesigner and read aloud using MacOS using the command line program 'say'.

The performance originally took place on September 2, 2019 at the Griffith University Queensland Convservatorium in Brisbane, Australia.  
Completed for the *Music Technology Live Capstone* class in 3rd year.

Performed and concieved in collaboration with Lachlan Parker and Lachlan Grant.

## Structure
There are 4 main components to the performance:

 - Touch Designer
	 - Displays user messages on the screen
	 - Provides GUI Interface
	 	- Check messages before going to screen
		- Clear all current messages
		- Send a message to the TTS Listener
		- Skip a message
	 - Broken in to 3 files for performance reasons. All 3 must run at once.
	 - Contains Python files written for 2.7, as this is the version that runs inside TouchDesigner
 - TTS Listener
	 - Written in Python 2.7
	 - Checks the web server for a message to read out
	 - Reads the message using the MacOS 'say' command (So it has to be run on a mac)
 - Flask web app
	 - Allows communication between all the components
	 - Is the interface for audience members to submit messages
 - Database
	 - Very simple MySQL database.
	 - You'll need to set this up yourself and connect it to your flask app
   
More documentation and a video demonstration coming soon. The original implementation can be accessed at www.capstone.live, though you won't be able to enjoy the awesome live performance that accompanies it.
   
# Warning
I take no responsibility for damages caused by this software. Use at your own risk. Software is not guaranteed to be bug free.

Note that this implementation does not contain any back-end protection for repeated submissions, making it very vulnerable to a simple denial of service attack.

# Software used
Bootswatch v4.3.1  
Homepage: https://bootswatch.com  
Copyright 2012-2019 Thomas Park  
Licensed under MIT  
Based on Bootstrap  

Bootstrap v4.3.1 (https://getbootstrap.com/)  
Copyright 2011-2019 The Bootstrap Authors  
Copyright 2011-2019 Twitter, Inc.  
Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)  

Trumbowyg v2.18.0 - A lightweight WYSIWYG editor  
http://alex-d.github.io/Trumbowyg  
license MIT  
Alexandre Demode (Alex-D)  
Twitter : @AlexandreDemode  
Website : alex-d.fr  

TouchDesigner 099
www.derivative.ca

Python 2.x

Flask for Python

MySQL
