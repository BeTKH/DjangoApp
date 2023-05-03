
#multiple var declaration
x,y,z = 1,2,3
print(x,y,z)


#unapcking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y)


#global

def myfunc():
  global x
  x = "fantastic"
  print("func is called")

myfunc()

print("Python is " + x)