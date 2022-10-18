# %% - example of SQLite database (DB)

# all python distributions since 2.5

import sqlite3

# create a connection to a database.
# conn = sqlite3.connect(':memory:')  # in memory DB
conn = sqlite3.connect('employee.db')  # makes a database file

# allows us to execue sql commants
c = conn.cursor()  # make a cursor

# start running sql commands
# c.execute(""" CREATE TABLE employees (
#     first text,
#     last text,
#     pay integer
#     ) """)

# c.execute('insert into employees VALUES ("alice", "apple", 50000)')
# c.execute('insert into employees VALUES ("bob", "banana", 75000)')

# employee_3 = {'first':'clive', 'last':'banana', 'pay':60000}

# c.execute('insert into employees VALUES (:first, :last, :pay)',
#     employee_3)

def insert_emp(emp:dict):
    with conn:
        c.execute('insert into employees VALUES (:first, :last, :pay)',
        emp)


def get_emps_by_name(lastname):
    c.execute('SELECT * FROM employees WHERE last=:last', 
                                    {'last':lastname})    
    return c.fetchall()


def update_pay(emp:dict, new_pay:int):
    with conn:
        c.execute('''UPDATE employees SET pay = :pay
            WHERE first = :first AND last = :last''', 
            {'first':emp['first'], 'last':emp['last'], 'pay':new_pay})


def remove_emp(emp:dict):
    with conn:
        c.execute('''DELETE from employees 
        WHERE first = :first AND last = :last''',
        {'first':emp['first'], 'last':emp['last']})


# c.execute('SELECT * FROM employees WHERE last=?', ('banana',))
# result = c.fetchall()
# print(result)

# c.execute('SELECT * FROM employees WHERE last=:last', 
#                                     {'last':'banana'})
# result = c.fetchall()
# print(result)

employee_01 = {'first':'dave', 'last':'cucumber', 'pay':100000}
employee_02 = {'first':'elle', 'last':'Dates', 'pay':125000}

insert_emp(employee_01)  # add employee
insert_emp(employee_02)  # add employee

update_pay(employee_02, 95000)  # update pay
remove_emp(employee_01)  # remove employee

emps = get_emps_by_name('banana')  # get data
print(emps)

# comit data to the database & close
conn.commit()
conn.close()


# %%
import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()  # make a cursor

remove_emp(employee_02)
remove_emp(employee_02)

conn.commit()
conn.close()


# %%
import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()  # make a cursor

emps = get_emps_by_name('banana')
print(emps)

conn.commit()
conn.close()
