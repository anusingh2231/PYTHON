# 1: .items()  method

marks = {
  "harry":100,
  "Shiv":99,
  "Rohan":90
}
print(marks.items()) # this can be iterate usinhg for loop


# 2: .keys() method -> this will  give keys i.e harry,shiv, Rohan
print(marks.keys()) 

# 3: .values() method ->this will give the values i.e 100,99,90
print(marks.values())

#4: .update() method-> this will update the value means change the value 
marks.update({"harry":99}) # this is for single entrity we can update multiple value by separeting with ,(comma)
marks.update({"Shiv":89,"Rohan":78, "Renuka":77}) # here renuka is new key value pair not in the dictionary it doesnot give error instead it will update the dictionary by adding Renuka in the dictionary
print(marks)

# 5: .get() method
print(marks.get("harry"))# this will give none if the keys value pair doesnot exist

print(marks["harry"])# if we use[] brackets to get the value it will give error if the name(keys value pair) doesn't exist.

# 6 dic.clear() method

# 7: .pop() 
marks.pop("harry")
print(marks)




