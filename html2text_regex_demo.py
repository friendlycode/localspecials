#!/usr/bin/env python

import re

import requests
import html2text

class VenueParser(object):

    url = None
    consumers = []

    def __init__(self):
        self.text = None
        self.specials = []

    def run(self):
        response = requests.get(self.url)
        html = response.text
        self.text = html2text.html2text(html)
        #print(self.text)
        for consumer in self.consumers:
            consumer(self)
        print(self.specials)




class PeppinosParser(VenueParser):

    url = "http://www.peppinospizza.com/specials"

    #@appends(0)
    def clean_intro(self):
        # TODO: this doesn't actually match anything
        matches = re.findall(r'Your Location.*Happy Hour', self.text, re.MULTILINE)
        for match in matches:
            text = match.group()
            print(text)
            self.text = self.text.replace(text, '')


    def clean_location(self):
        pass

    #@appends(3)
    def consume_late_night(self):
        #re.search(None, self.text)
        #self.text.replace(match, '')
        #self.specials.append(special)
        pass



    def consume_burger_special(self):
        self.text = self.text.replace("""
### Saturday

##### 11AM - 5PM

$5.99 All-American Burger Baskets

$.50 Traditional/$.60 Boneless Wings

#####  **‘till 8PM**

$3.75 Coors Light, Miller Lite 22oz Talls""", '')
        special = {
            'item': 'burger',
            'date': 'saturday',
            'start': '11am'
        }
        self.specials.append(special)



    consumers = [
        clean_intro,
        clean_location,
        consume_late_night,
        consume_burger_special,
    ]


parser = PeppinosParser()
parser.run()


