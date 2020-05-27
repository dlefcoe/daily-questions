'''

web scrape using the requests and Beautiful soup modules

BeautifulSoup lets users pull tags from the HTML which is pulled from requests.


'''


# imports
import requests
import bs4

url = 'https://www.bbc.co.uk'





def myExample(url):
    ''' example code '''

    # get the data
    result = requests.get(url)

    if result.status_code == 200:
        print('code 200: all good')
        # print all the things in the code that we might want
        #print(result.content)
        #print(result.headers)
        #print(result.text)
        #print(result.json)

        # create soup object
        soup = bs4.BeautifulSoup(result.content, 'lxml')
        links = soup.find_all('a')
        h2 = soup.find_all('h2')
        #print(links)
        print(h2)
        
        # list for the urls
        urls = []


        return True
    else:
        print('some kind of error')
        return False



# execute code
if __name__ == "__main__":
    myExample(url)