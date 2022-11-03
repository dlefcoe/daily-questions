# %%  - test a double context manager

# some files
f1 = 'tests/test_csv.csv'
f2 = 'tests/some_file.txt'
f3 = ''


with open(f1) as a, open(f2) as b:
    contents_1 = a.readlines()
    contents_2 = b.readlines()

print('this is contents 1:')
print(contents_1)

print('this is contents 2:')
print(contents_2)


