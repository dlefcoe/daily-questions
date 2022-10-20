
'''
python coding book:
https://www.lulu.com/shop/darren-lefcoe/python-programming/ebook/product-5pgqrd.html
'''


options = {
    'a':'liz Truss', 
    'b':'Jeremy Hunt',
    'c':'Kwasi Kwarteng'
    }

print('list of options:')
for k, v in options.items():
    print(k, v)

# ask the question
prime_minister = input('who is the prime minister?')

if prime_minister in options:
    print('try again')
else:
    print('correct: anyone but these')
