'''



'''
import urllib.request
import requests

urlForBBC = 'https://www.bbc.co.uk/news'
r = requests.get(urlForBBC)

bbcText = r.text
print(bbcText)
print('----done-----')

from xml.etree.ElementTree import parse

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')

data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()



def gray(n):
    """Generate gray code."""
    result = ["0", "1"]

    while n > 1:
        new = reversed(result)
        result = ["0" + x for x in result] + ["1" + x for x in new]
        n -= 1

    return result

def runCode():
    for line in gray(5):
        print(line)


def setTest():
    y = set(["hello","baby", "zaza"])
    print(y)

    y = set({"hello":5})
    print(y)

setTest()


print('the first modules name: ' + __name__)



def tryGet():
    ages = {
        'mary': 5,
        'john': 10,
        'dick': 20
    }

    a = ages.get('john')
    b = ages.get('blah', 'dont know age')
    print(a, b)

tryGet()



def testFun(a, b):
    """This adds a and b and returns the sum.
    
    Arguments:
        a {integer} -- first value
        b {integer} -- second value
    
    Returns:
        integer -- sum of the inpits
    """

    return a + b

x = testFun(5, 3)



def foobar():
    foo = 'hello'
    bar = 'world'
    print(foo, bar)


foobar()

print(x)
print('hello')



import inspect

print(inspect.getmembers(foobar()))
print('------ the source code:')
print(inspect.getsource(foobar))






