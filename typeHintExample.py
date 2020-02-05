'''

example of type hinting (for documenting and commenting code)
it tells you wat it is expecting, but does not throw an error

'''



def helloWorld(myName: str) -> str:

    return(f'hello {myName}')


x = helloWorld('darren')

print(x)




import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(x)
print(type(x))

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))


