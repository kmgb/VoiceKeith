"""
This module is the only one because I'm lazy

Someday, this module will speak, and its name will be Keith.
It may not speak the best, but it will try, and damn you that's better than most of us do.

Tries to translate words to their IPA form, then (in the future) speaks them back.
"""

import urllib.request
from bs4 import BeautifulSoup

def get_pronunciations(word):
    """
    Tries its darndest to find the pronunciations of a word on wiktionary, no guarantees :)

    Basically, Google Translate probably needs a payment for long-time usage, and manages to be
    even more inconsistent than Wiktionary (because the webpage is dynamic, toggling maybe, etc.),
    also they happen to use NOAD respelling, which would be annoying to switch to IPA for
    consistency.

    In the future, maybe there will be a convenient, open, consistent API for getting
    pronunciations, but today is not that day.
    """
    try:
        urlrequest = urllib.request.urlopen("https://en.wiktionary.org/wiki/"+word)
        # TODO: Safety checks for url returned, URLError, etc.
        # Right now, I'm pretending errors can't happen, which is never a good thing to assume
        html = urlrequest.read()
        soup = BeautifulSoup(html, "html.parser")
        possible_ipas = soup.select("span.IPA")
        ipalist = []
        for item in possible_ipas:
            # TODO: More testing if valid IPA
            if item.text.startswith("/") and item.text.endswith("/"):
                ipalist.append(item.text)
        return ipalist

    except: # TODO: Specify different errors
        return None


# Just a test...
ipalist = get_pronunciations("test")

if ipalist is not None and ipalist:
    # TODO: Choose based on context
    ipa = ipalist[0] # Choose the first, because that's *usually* the most common one
    ipa = ipa.translate({ord(c): None for c in "()"}) # Remove parentheses with *flamboyance*
    print(ipa)
