'''

This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?

25 aug 2019
This was solved by D Ross. Tested by dlefcoe.

'''


import random

urls = {}  # keys are long urls - values are short urls
chars = "abcdefghijklmnopqrstuvwxyz"
chars += chars.upper()
chars += "0123456789"


def gen_url():
    """Generate a unique 6 character short URL code."""
    short = [random.choice(chars) for i in range(6)]
    short = "".join(short)
    # ensure short url is unique
    while short in urls.values():
        return gen_url()
    return short

def shorten(url):
    """Shorten a url."""
    if url in urls:
        # this url has already been shortened
        return urls[url]
    else:
        # this url has not been shortened so generate a new short url and add it to our dict
        short = gen_url()
        urls[url] = short
        return short

def restore(short):
    """Restore a shortened url."""
    for longurl, shorturl in urls.items():
        if shorturl == short:
            return longurl
    # not found
    return None

def test():
    """Shorten some urls, test duplicate input, re-expand urls."""

    testurls = (
        "http://www.aol.com",
        "http://www.cnn.com",
        "http://www.poo.com",
        "http://www.cnn.com",
        "http://www.bbc.com",
    )

    for testurl in testurls:

        shortened = shorten(testurl)
        print(testurl, shortened, restore(shortened))

test()