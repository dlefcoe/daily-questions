'''
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

requires the "helloWorldSample.txt" file in the same folder.

date: sep 2019
author: darren


'''




def read7(filename, startPos):
    ''' 
    reads file
    filename: string containing the name of the file to be read (ie. helloWorld.txt)
    startPos: integer for starting position to read from
    returns 7 characters from file and file pointer number

    
    '''
    s = ' start blank'

    # open the file for reading
    filehandle = open(filename, 'r')
    filehandle.seek(startPos)
    contents = filehandle.read(7)
    print(contents)

    # while True:
    #     contents = filehandle.read(7)
    #     if not contents:
    #         print('end of file')
    #         break
    #     print(contents)

    last_pos = filehandle.tell()

    # close the pointer to that file
    filehandle.close()

    
    return s, last_pos




def readN(filename, numRead7):
    '''
    reads file using the read7 function above.
    inputs: 
        filename: string for file to read
        numRead7: integer for number of read7 functions to use 
    '''

    for i in range(1, numRead7):
        read7(filename, i*7)


    s = 'return N string'
    return s


# define the name of the file to read from
filename = "helloWorldSample.txt"
read7(filename, 0)

readN(filename, 3)

