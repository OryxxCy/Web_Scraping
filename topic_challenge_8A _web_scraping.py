"""
Description: Webscrapes https://www.colorhexa.com/color-names 
and print all color names and hex codes.
Author: Cyrusbien Sarceno
Section Number: 251409
Date Created: 03-13-2024
Updates: 03-17-2024
"""

from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
    """A class that inherits from HTMLParser to parse the HTML content 
    and extract the color names and hex values."""
    def __init__(self):
        super().__init__()
        self.td = False
        self.a = False
        self.color_name = ""
        self.color_hex_code = ""
        self.colors = {}

    def handle_starttag(self, tag, attrs):
        """ Get the start tags and its attributes."""
        if tag == 'td':
            self.td = True
        if self.td and tag == 'a':
            self.a = True

    def handle_data(self, data):
        """Get the data inside tags."""
        if self.td and self.a and self.color_name == "":
            self.color_name = data
        elif self.td and self.a:
            self.color_hex_code = data
            self.colors[self.color_name] = self.color_hex_code
            self.color_name = ""
        if self.td and self.a:
            self.td = False
            self.a = False

def get_colors():
    """Get the colors name and hex value form colorhexa."""
    myparser = MyHTMLParser()
    with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
        html = str(response.read())
    myparser.feed(html)
    return myparser.colors.items()

if __name__ == "__main__":
    for name, hex_value in get_colors():
        print(f"{name} {hex_value}")
    print(f"Total colors: {len(get_colors())}")
    input("Press the keyboard to exit.")
