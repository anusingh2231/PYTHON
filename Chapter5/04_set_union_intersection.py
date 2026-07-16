s1 = {1,45,60,78}
s2 ={7,8,1,78}
print("Union of the set is: " ,s1.union(s2))

print("Intersection of the set is: ",s1.intersection(s2))

# we can do multiple set to union
a = {2, 4, 5, 6}
b = {4, 6, 7, 8}
c = {7, 8, 9, 10}

print(a.union(b).union(c))
print(a.union(b, c))