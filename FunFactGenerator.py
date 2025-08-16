#Fun fact Web App Generator using PyWebIO module
#Create a virtual environment
#pip install pywebio
#pip install pylance
#python version 3.12.7

import json                                                             #loads python's built-in library to parse data returned from APIs
import requests                                                         #to send HTTP requests like GET to fetch data from web API
from pywebio.input import *                                             #imports PyWebIO’s input text fields, checkboxes
from pywebio.output import *                                            #imports PyWebIO’s output put_text, put_html
from pywebio.session import *                                           #imports session utilities like clear() to reset UI, hold() to keep app running

def get_fun_fact(_):
    clear()                                                             #resetting the page

    put_html(                                                           #to render raw HTML in the app
        '<p align="left>'
        '<h2>Fun Fact Generator</h2>'
        '</p>'
    )

    url = "https://uselessfacts.jsph.pl/random.json?language=en"        #API endpoint from where we will fetch the data

    response = requests.get(url)                                        #sends a GET request to that API, returning a Response object containing JSON data

    data = json.loads(response.text)                                    #With response.text we can get the API’s reply as a string. json.loads(...) converts that string into a Python dictionary so we can access its keys

    useless_fact = data['text']                                         #From the JSON response it will extract the text field which contains the actual fun fact

    style(put_text(useless_fact), 'color:blue; font-size: 30px')        #displays the fact as text on the webpage

    put_buttons(                                                        #creates buttons on the page.
        [dict(label='Click me', value='outline-success', 
              color='outline-success')], onclick=get_fun_fact
    )

if __name__ == '__main__':                                              #this block only runs when executed the script directly (not when imported as a module)

    put_html(
        '<p align="left">'
        '<h2>Fun Fact Generator</h2>'
        '</p>'
    )

    put_buttons(
        [dict(label='click me', value='outline-success', 
              color='outline-success')], onclick=get_fun_fact
    )
    hold()                                                              #Keeps the PyWebIO app running and interactive.