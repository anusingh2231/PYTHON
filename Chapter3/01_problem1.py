#question 1: WAP to display a user entered name followed by good afternoon using input() function.
name = input("Enter your name: ")

print(f"Good afternoon,{name}")# using f string to access the value in the name



#question 2: WAP to fill in a letter template given below with name and date.
# letter='''
#       Dear <|Name|>,
#       You are selected!
#       <|Date|> 
#        ''' 
letter='''
      Dear <|Name|>,
       You are selected!
       <|Date|> 
        ''' 
print(letter.replace( " <|Name|>","Harry").replace("<|Date|> ", "24 september 2026"))



#Question 3: WAP to detect the double space in a string
name1 = "Harry is a good     boy and"
print(name1.find("  ")) # return the index where the space detected


#Question 4: Replace the double space from problem 3 with single space
name2 = "Harry is a good     boy and"
print(name2.replace("  ", " ")) 
print(name2)


#Question 5: WAP to formate the following letter using escape sequence characters.   Letter ="Dear Harry, This python course is nice. Thanks!"
Letter ="Dear Harry,\n \tThis python course is nice.\n Thanks!"
print(Letter)






