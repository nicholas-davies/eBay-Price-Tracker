# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Prompt user to enter the URL with the desired filters
url = input("\nEnter the url (with the desired filters) for your item make sure you check the 'sold' filter: ")

# Function to get data from the provided URL
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# Function to parse the HTML and extract relevant information
def parse(soup):
    productslist = []  # List to store product information
    results = soup.find_all('div', {'class': 's-item__info clearfix'})  # Find all items in the HTML with the specified class
    print(len(results))
    print('\n')

    numberOfResults = len(results)
    averagePrice = 0

    for item in results:
    	
        # Skip items with specific conditions
        if 'to' in item.find('span', {'class': 's-item__price'}).text:
            continue
        if 'Shop on eBay' in item.find('div', {'class': 's-item__title'}).text:
            continue

        # Extract information from each item
        products = {
            'title': item.find('div', {'class': 's-item__title'}).text,
            'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('$', '').replace(',', '').strip()),
            'link': item.find('a', {'class': 's-item__link'})['href'],
        }

        averagePrice += products['soldprice']
        print(products)
        print('\n')
        productslist.append(products)

    averagePrice /= numberOfResults
    print(averagePrice)
    print('\n')

    return productslist

# Function to output the extracted information to a CSV file
def output(productslist):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv('iPhonePriceAverage.csv', index=False)
    print('Saved to CSV (will save to whatever directory your terminal is in)\n')
    return

# Main program
soup = get_data(url)
productslist = parse(soup)
output(productslist)
