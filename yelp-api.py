# -*- coding: utf-8 -*-
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#**params, is a way to get the dictionary into the search

def get_businesses(location, term):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ['TOKEN_SECRET']
    )
    client = Client(auth)

    params = {
        'term': term,
        'lang': 'en',
        'limit': 3
    }

    response = client.search(location, **params)
    businesses = []
#     for business in response.businesses:
#         # print(business.name, business.rating, business.phone)
#         businesses.append(business.name)
#     return businesses
# businesses = get_businesses('Danville', 'golf')
# print(businesses)

# question: what if i want to print out a list of each business as a dictionary
    for business in response.businesses:
        # print(business.name, business.rating, business.phone)
        businesses.append({"name": business.name,
        "rating": business.rating,
        "phone": business.phone
        })
    return businesses

address = input("what city do you want to search  ")
terms = input("What search term do you want to use  ")
print(address, terms)
businesses = get_businesses(address, terms)
