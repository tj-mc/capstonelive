# capstone.live

Source code for an interactive audio-visual performance with Python and TouchDesigner. Audience members submit short messages via a web app, which is shown on screen using TouchDesigner and read aloud using MacOS using the command line program 'say'.

## Structure
There are 4 main components to the performance:

 - Touch Designer
	 - Displays user messages on the screen
	 - Provides a GUI for checking messages before displaying them and other features
	 - Broken in to 3 files for performance reasons. All 3 must run at once.
 - TTS Listener
	 - Written in Python
	 - Checks the web server for a message to read out
	 - Reads the message using the MacOS 'say' command (So it has to be run on a mac)
 - Flask web app
	 - Allows communication between all the components
	 - Is the interface for audience members to submit messages
 - Database
	 - Very simple MySQL database
	 - You'll need to set this up yourself and connect it to your flask app
   
More documentation and a video demonstration coming soon. The original implementation can be accessed at www.capstone.live, though you won't be able to enjoy the awesome live performance that accompanies it.
   
# Warning
I take no responsibility for damages caused by this software. Use at your own risk. Software is not guaranteed to be bug free.

Note that this implementation does not contain any protection for repeated submissions, making it very vulnerable to a simple denial of service attack.

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
