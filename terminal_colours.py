
'''

class with basic terminal colours in python.
and an example 

'''


class Colours:
    '''  ANSI escape codes used for defining a color. '''

    # colours
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'

    # decoariton
    bold = '\033[1m'
    underline = '\033[4m'

    # end
    end = '\033[0m'


def main():
    """ example usage """
    c = Colours()
    print(f'{c.magenta}hi there{c.end}')
    print(f'{c.blue}hi there{c.end}')
    print(f'{c.cyan}hi there{c.end}')
    print(f'{c.yellow}hi there{c.end}')
    print(f'{c.red}hi there{c.end}')
    print(f'{c.white}hi there{c.end}')
    print(f'{c.bold}hi there{c.end}')
    print(f'{c.underline}hi there{c.end}')
    print('the end...')


if __name__ == '__main__':
    main()
