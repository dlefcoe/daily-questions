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
import requests


def main():
    ''' the main module '''
    
    url = 'https://github.com/dlefcoe/daily-questions/blob/master/perform_backup/inputs.json'
    raw_url = rawify_git(url)
    x = read_git_pandas(raw_url)
    y = read_git_request(raw_url)

    print('dataframe:', '\n', x, '\n')
    print('dict:', '\n', y)


def read_git_pandas(url:str)->pd.DataFrame:
    ''' read git from raw url into a pandas dataframe '''
    df = pd.read_json(url, typ='series')

    return df


def read_git_request(url:str) -> dict:
    ''' read git from raw url into a python dict '''
    response = requests.get(url)
    data = json.loads(response.text)

    return data
    


def rawify_git(url:str):
    ''' given a native git url, change it to raw '''
    url = url.replace('github.com', 'raw.githubusercontent.com')
    url = url.replace('/blob/','/')
    return url


if __name__ == '__main__':
    main()
