'''

convert a string to a date
then
convert a date to a string

the format is always: yyyy-mm-dd
the date is a datetime (or date) class

'''


from datetime import datetime

# the format is yyyy-mm-dd
start_date = '2018-09-19'

# convert string to date
date_obj = datetime.strptime(start_date,'%Y-%m-%d').date()
print('date object:', date_obj)

# convert date to string
date_str = date_obj.strftime('%Y-%m-%d')
print('date string:', date_str)
