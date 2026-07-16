# Question 1: Write a program to create a Dictionary of Hindi words with value as their English translation provide a user with an option to look it up
words = {
  "madad": "help",
  "kurshi": "chair",
  "billi":"cat"
}
word = input("Enter the word you want meaning of: ")
print(words[word])


#question 2: Write a program to input a 8 number from the user and display all the unique number once 
s = set()
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
print(s)


#Question 3: Can we have a set with 18(int)integer and 18(str) string as a value in it-> yes we can have 
s1 = set()
s1.add(18)
s1.add("18")
print(s1)

#Question 4:what will be the length of following s:
# s2= set()
# s2.add(20)
# s2.add(20.0)
# s2.add('20') This will only give 2 value i.e {'20',20} because python read 20,20.0 will be treated as equal as it compare values not their type

s2= set()
s2.add(20)
s2.add(20.0)
s2.add('20')
print(len(s2))

#Question 5: s = {}   what is the type of 's3'?
s3 = {}
print(type(s3)) # o/p : dictionary


#Question 6: Create an empty dictionary allow four friends to enter their favorite language as the value and use key as their name assume that the name are unique
k = {}

name = input("Enter friends name:")
lang = input("Enter language name: ")
k.update({name: lang})

name = input("Enter friends name:")
lang = input("Enter language name: ")
k.update({name: lang})

name = input("Enter friends name:")
lang = input("Enter language name: ")
k.update({name: lang})

name = input("Enter friends name:")
lang = input("Enter language name: ")
k.update({name: lang})

name = input("Enter friends name:")
lang = input("Enter language name: ")
k.update({name: lang})

print(k)

# Question 7: If the name of two friends are same what will happen to the program in the problem 6 -> then it will only show 3  key value pair and it will print last value because it will update the value


# Question 8 : if the language  is same ? value can be same but key must not be same

#Question 9: Can you change the value inside a list which is contained in set S ? s3 = { 8, 7 ,12, "Harry",[1,2]}
# the value later enter will be updated 
s3 = { 8, 7 ,12, "Harry",[1,2]} # list cannot be in the set

s3 #must not be
