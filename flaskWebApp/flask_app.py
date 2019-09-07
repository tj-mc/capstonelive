
from flask import Flask, request, render_template
import MySQLdb
from bs4 import BeautifulSoup
from random import randint

app = Flask(__name__)

# Make sure templates are reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Connects to the database
def dbConnect():
    db = MySQLdb.connect("") #You'll need to put your own details in here
    db.set_character_set('utf8')
    return db

#Error
def error(error, exception):
    return render_template("error.html", error = error, exception = exception)




#Main route for submitting mesages
@app.route('/', methods = ['GET', 'POST'])
def index():

    #%%%%%%%%%%%%%%%%%%%%%%% Lockout code to prevent pre performance submissions %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #return render_template('lockout.html')

    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':

        #If data was empty
        textData = request.values.get('textData')
        if not textData:
            return error("You submitted an empty form.", None)

        soup = BeautifulSoup(textData)
        textData = soup.get_text()

        #If entry was too long
        if len(textData) > 100:
            return error("Your entry was too long.", None)

        #Prevent illegal characters in the string
        bannedCharacters = ["#", "@", "&"]
        print(textData)
        if any(c in textData for c in bannedCharacters):
            return error("You used an illegal character. Please avoid using #, @ or &", None)

        #Break the input text into words
        textList = textData.split()

        #Open the banned words list
        file = open("/home/tommcintosh/qcgu/static/banned.txt", "r")
        bannedWords = file.read().splitlines()


        #Boolean for keeping track of naughty words
        wasNaughty = False

        #A list of friendly words
        happyWords = ["obsidian", "diamonds", "the nether", "notch", "mojang", "chicken", "the ender dragon", "steve", "minecraft", "creeper", "herobrine", "skeleton", "baby zombie", "zombie", "enderman", "gold", "redstone", "mine", "enchanted pickaxe", "diamond sword", "pewdiepie"]

        # Iterate through the user input to check for banned words
        for index, word in enumerate(textList):
            #If this word matches a banned word.
            if word.lower() in bannedWords:
                wasNaughty = True
                #Replace the word at the current index with a safe word
                textList[index] = happyWords[randint(0, 20)]

        #Join the textList into a string
        if wasNaughty == True:
            textData = " ".join(textList)

        #Ensure message is in the right format for the database
        textData = textData.encode('utf-8')

        #Create a cursor and query the databse
        try:
            db = dbConnect()
            cursor = db.cursor()
            cursor.execute('SET NAMES utf8;')
            cursor.execute('SET CHARACTER SET utf8;')
            cursor.execute('SET character_set_connection=utf8;')
            cursor.execute("""INSERT INTO posts (postid, datetime, contents) VALUES (NULL, NOW(), %s)""", (textData, ))
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            return error("Error inserting submission into database. This is due to an incompetent developer.", e)

        if wasNaughty == True:
            return error("Looks like you used an innapropriate word. Obviously this was a mistake, so I replaced it with something more PG &#x1f60e;", "")

        #If no errors have been returned yet
        return render_template('thankyou.html')

    else:
        return error("Method not supported.", None)


#Display all entries in the database as plain text
#Used by TouchDesigner to get messages and ID's
@app.route('/plainTextData', methods = ['GET'])
def plainText():

    if request.method == 'GET':

        try:
            db = dbConnect()
            cursor = db.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("""SELECT postid, datetime, contents FROM posts""")
            results = cursor.fetchall()
            cursor.close()
            db.close()
        except:
            return 'Could not return results from the database.'

        return render_template('admin.html', results = results)

    else:
        return error('Method banned.', None)


#Delete posts using ID
#Used by TouchDesigner to delete posts
#If we didn't run this, then we would keep downloading the same posts again and again
@app.route('/deletePostByID', methods = ['GET'])
def deletePostByID():

    #Only method supported for this
    if request.method == 'GET':

        #If no values supplied
        if not request.args:
            return 'Nothing to do'

        #Get the number of arguments
        numOfArguments = len(request.args)

        print(numOfArguments)

        sql = "DELETE FROM posts WHERE "

        #To count the iterations of this for loop
        counter = 1

        #Iterate across the request values to create a the sql query
        for id in request.args.values():

            #Append to the sql command
            sql = sql + "postid = " + str(id)

            #If this is not the last item in the list
            if counter != numOfArguments:
                sql = sql + ' or '

            counter = counter + 1



        #Delete the results using the sql string
        #Create a cursor and query the databse
        try:
            db = dbConnect()
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            return error("Error deleting submission from database.", e)

        print(sql)
        return 'ok'

    else:
        return error('Method banned.', None)

#Used to send a single message to the TTSListener
#Inserts a single string into the database. 
#The ID of this string is always 0
@app.route('/TTShold', methods = ['POST'])
def TTShold():

    textData = request.values.get('textData')

    textData = textData.encode('utf-8')

    #Create a cursor and query the databse
    try:
        db = dbConnect()
        cursor = db.cursor()
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute("""UPDATE ttshold SET text = %s WHERE id = 0""", (textData, ))
        db.commit()
        cursor.close()
        db.close()
    except:
        return "Error inserting submission into databse."

    return "OK! Web server has sent message \n>>>{}".format(textData)


#Used by the TTS Listener to get the latest message, then delete it
@app.route('/TTSGet', methods = ['GET'])
def TTSGet():

    #Get data
    try:
        db = dbConnect()
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("""SELECT text FROM ttshold WHERE id = 0""")
        results = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        return 'Could not return results from the database.'


    #Delete data
    #Create a cursor and query the databse
    try:
        textData = ""
        db = dbConnect()
        cursor = db.cursor()
        cursor.execute("""UPDATE ttshold SET text = %s WHERE id = 0""", (textData, ))
        db.commit()
        cursor.close()
        db.close()
    except:
        return "Error inserting submission into database. This is due to an incompetent developer."


    return render_template('tts.html', results = results)

#Because the TTSGet route automatically deletes a message as soon as it is retrieved,
# we need another route to just check the message.
# This is used by TouchDesigner to see if the TTS Listener has grabbed the latest message
# This gives me visual feedback that confirms the TTS Listener is working
@app.route('/TTSPeek', methods = ['GET'])
def TTSPeek():
    #Get data
    try:
        db = dbConnect()
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("""SELECT text FROM ttshold WHERE id = 0""")
        results = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        return 'ERROR: Could not return results from the database.'

    if not results:
        return ''

    else:
        return render_template('tts.html', results = results)

















