

"""
Lists are

- ordered
- mutable
- allow duplicates and dt data types

"""

hyb_list = [1,2,3,3, "str", True, False, False, 3.14]

for i in hyb_list:
    print('list item', i, "has data type:", type(i))

print()
#list operations

#check if item exists

list_Fruit = ["apple", "banana", "cherry"]
if "apple" in list_Fruit:
  print("Yes, 'apple' is in the fruits list")
print()

#mutate / modify list at a given index
list_Fruit[0] = "Mango"
print(list_Fruit)

list_Fruit[0:2] = ["Kiwi", "Avocado"]
print(list_Fruit)


#insert into list
list_Fruit = ["apple", "banana", "cherry"]
list_Fruit.insert(0, "Mangooo")
print(list_Fruit, )


#append into list
list_Fruit = ["apple", "banana", "cherry"]
list_Fruit.append("Mangooo")
print(list_Fruit, "\n")

#extend list

list1 = ["A", "B", "C"]
list2 = ["D", "E"]

list1.extend(list2)
print(list1)


list1 = ["A", "B"]
list2 = ["D", "E"]
list_3 = list1 + list2
print(list_3)


# remove
list_3.remove("A")
print(list_3)


#loop on lists-for loops
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i], "the index is:", i)


#loop on lists-while loops
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


thislist_ = ["d", "sd", "dwa"]
[print(x) for x in thislist_]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


# list comprehension with condition  [expression for item in iterable if condition == True]
new_fruits = [x for x in fruits if "a" in x]

print(new_fruits)



newlist_ap = [x for x in fruits if x != "apple"]
print(newlist_ap)