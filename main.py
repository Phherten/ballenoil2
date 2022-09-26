from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import lxml


def ballenoil_scraping(web):
    resultado = requests.get(web)
    sopa = BeautifulSoup(resultado.text, 'lxml')
    valor = sopa.select('.small-12 tbody tr td')[1]
    precio = valor.getText()
    return precio
