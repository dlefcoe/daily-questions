'''
How do I specify new lines on Python, when writing on files?


'''

import os

def main():
    ''' everything is is this main function 
    this forces all functions to be read before they are executed
    '''

    # example 1
    print('First line \n Second line')


    # example 2
    line1 = "hello how are you"
    line2 = "I am testing the new line escape sequence"
    line3 = "this seems to work"

    # create full path
    pathname = os.path.dirname(os.path.realpath(__file__))
    filename =  'demofile01.txt'
    fullname = os.path.join(pathname, filename)

    # write to file
    writeToFile(fullname)

    # write to file
    def writeToFile(fullname):
        ''' write to file '''

        file = open(fullname, "a")

        file.write(line1)
        file.write("\n")
        file.write(line2)
        file.write("\n")
        file.write(line3)
        file.write("\n")

        file.close()


