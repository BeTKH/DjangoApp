

#string type

x = "hello"
print(x, "is type of: ", type(x) ,"\n")


#number types
i, f, c = 1, 1.2, 1+2j
print(i,f,c, "are types of :", type(i), type(f), type(c), "\n")


#sequnece types

lst_ = [1,2,3, "Hi", ["another", "lsit"]]
tup = (1,2,3, "Hi", ["another", "lsit"])
range_ = range(2, 10, 1)

print(lst_, "type is : ", type(lst_))
print(tup, "type is : ", type(tup))
print(range_, "type is : ", type(range_))

#set types - set and frozenset (special seqence - no duplicates)
set_ = {1,2,3,4,4, "yes", "yes"}
print(set_, "type is : ", type(set_))


vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet, type(fSet))
print('The empty frozen set is:', frozenset())

# frozensets are immutable
#fSet.add('v')


#mapping types

dict_ = {"key_1" : [1,2,3, "val2"], "key_2" : "val2"}
print(dict_, "type is : ", type(dict_), "\n")


#boolean types
t = True
print(t, "type is : ", type(t))


#bytes, bytearray, memoryview
b = bytes(True)
b2 = bytes(3)
print(b, "type is : ", type(b))
print(b2, "type is : ", type(b2))

ba = bytearray(True)
ba2 = bytearray(3)
print(ba, "type is : ", type(ba))
print(ba2, "type is : ", type(ba2), '\n')

#accepts by
mv = memoryview(ba)
mv2 = memoryview(ba2)

print(mv, "type is : ", type(mv))
print(mv2, "type is : ", type(mv2), '\n')


#none type
nn = None
print(nn, "type is : ", type(nn))


