'''



'''
import urllib.request

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

try:

    pass
except expression as identifier:
    
    pass
else:
    pass
finally:
    pass
