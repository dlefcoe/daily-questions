'''

have a raw github json file
want to read this into python

converting a file to raw looks like this:

git file:
    https://github.com/dlefcoe/daily-questions/blob/master/perform_backup/inputs.json

raw file:
    https://raw.githubusercontent.com/dlefcoe/daily-questions/master/perform_backup/inputs.json

notice how:
 - github.com -> raw.githubusercontent.com
 - blob is removed

'''

# builtin imports
import json

# external imports
import pandas as pd


def main():
    ''' the main module '''
    
    url = 'https://github.com/dlefcoe/daily-questions/blob/master/perform_backup/inputs.json'
    raw_url = rawify_git(url)
    read_git(raw_url)


def read_git(url):
    ''' read git from raw url '''
    df = pd.read_json(url, typ='series')
    print(df)


def rawify_git(url:str):
    ''' given a native git url, change it to raw '''
    url = url.replace('github.com', 'raw.githubusercontent.com')
    url = url.replace('/blob/','/')
    return url


if __name__ == '__main__':
    main()