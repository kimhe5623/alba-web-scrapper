import requests
from bs4 import BeautifulSoup

def getSoup(url):
  rsp = requests.get(url)
  soup = BeautifulSoup(rsp.text, "html.parser")
  return soup
