
'''
how to use the new match statement in python with a dict
'''


# %% standard match statement

def process_input(input):
    ''' function which uses the match statement '''

    match input:
        case "start":
            print("Starting...")
        case "stop":
            print("Stopping...")
        case value if isinstance(value, int) and value > 0:
            print(f"Processing {value} items...")
        case _:
            print("Unknown command")


# some examples
process_input('start')
process_input('stop')
process_input(10)
process_input('blah blah')






# %%


d1 = {'a':100, 'b':10, 'c':99}
d2 = {'a':1, 'b':2, 'c':3}

def process_input_dict(input:dict):
    ''' function which uses the match statement '''


    match input:
        case {'a':100, 'b':10, 'c':99}:
            print("Starting...")
        case {'a':1, 'b':2, 'c':3}:
            print("Stopping...")
        case value if isinstance(value, int) and value > 0:
            print(f"Processing {value} items...")
        case _:
            print("Unknown command")

process_input_dict(d1)
process_input_dict({'a':1, 'b':2, 'c':3})
process_input_dict(10)
process_input_dict('blah blah')


