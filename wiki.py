import requests
import wikipediaapi

def getwikiurl(title):
    lang = wikipediaapi.Wikipedia('en')
    page_py = lang.page(title)
    wikipages = page_py.fullurl
    print(wikipages)
    return{
        'wiki' : wikipages
    } 
