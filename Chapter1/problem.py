# question1 : WAP to print twinkle twinkle little star poem
# using '''  triple single quote to print the multiline 
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.
''')
#question 2: use REPL  and print the table of 5 using it 
# manually print in terminal lile this 5*1 

#question3:install an external module and use it to perform an operation of your interest
import pyttsx3
engine = pyttsx3.init()
engine.say("you are awesome anushka. And you are so beautful with a beautfiul heart. you deserve the bestest in life . you will also get what you want")
engine.runAndWait()# this will convert the text into voice(speech)


# question4: WAP  to print the content of a directory using the OS module. Search online for the function which does that.
import os

# Enter the path of directory
path = "/"

# Get the list of files and folders
contents = os.listdir(path)

# Print directory contents
print("Contents of the directory:")

for item in contents:
    print(item)


#question5:label the code with comment 
# answer in above (qus4)    