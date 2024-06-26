# The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services

# Once you have installed the Requests module, you can start using it to send HTTP requests. Here is a simple example that sends a GET request to the Google homepage


# import requests
# response = requests.get("https://www.google.com")
# print(response.text)

import requests 
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)