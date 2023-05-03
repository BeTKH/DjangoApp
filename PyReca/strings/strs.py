
#strs are like array
str_ = "Hello, World!"

#1.we can subset them
print("the word at index 0 is:", str_[0])

#2. we can loop through them

for w in str_:
    print(w)

    if w == "l":
        break

#3. we can get the length
print("the lenth of the str_ is: ", len(str_), '\n')


#4. check for the precence/absence of a string
str_ = "Hello, World!"

if ("Hell" in str_):
    print("yes there is Hell in Hello!")

if("love" not in str_ ):
    print("Love is not present in Hell!")



# string operations

#slising
str2 = "Mask"


slic_ = str_[1:5]
slic_2 = str2[0:1]
print("The sliced string is: ", slic_+slic_2)


#negative indexing
str_ = "Hello, World!"
print("The -ve indexed string is: ", str_[-5:-1], "\n")


#modify string: .upper(), .lower(), .strip(), replace(), split()

str_x = "  Hello World _"

print("upper", str_x.upper())
print("lower", str_x.lower())
print("strip", str_x.strip())
print("replace", str_x.replace("H", "F"))
print("split by _", str_x.split("_"))
print("split by space", str_x.split(" "))
print("split by space after strip", str_x.strip().split(" "))
print()

#join
CreateUserName = ("John", "Peter", "Vicky")
un_ = "_".join(CreateUserName)
print("joined text is: ",un_, '\n')

#partition()
print("the partition is:", un_.partition("_"), "\n")


newStr = un_.zfill(5)
print("zfill to text is", newStr )



#format strings
age = 36
txt = "May age is : {}"
print(txt.format(age))



wine = 23
beer = 15
txt2 = "    I want to get {} bottles of wine and {} bottles of beer"

print(txt2.strip().format(wine, beer))



