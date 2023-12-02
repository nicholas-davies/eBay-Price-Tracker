eBay Price Scraper
Overview
This Python script enables users to scrape eBay product information, focusing on sold items, based on a provided URL with desired filters. It utilizes the requests library for web scraping and BeautifulSoup for HTML parsing. Extracted data, including product title, sold price, and product link, is then stored in a Pandas DataFrame and saved to a CSV file for further analysis.

Features
User Interaction: The script prompts users to input a URL with specific filters, ensuring the retrieval of sold items.

Data Extraction: The program extracts relevant information from eBay product pages, including title, sold price, and product link.

Data Processing: It skips items with certain conditions, such as a price range or promotional messages, to provide more accurate results.

Output: Extracted data is presented in the console and saved to a CSV file named 'iPhonePriceAverage.csv' in the same directory as the script.

How to Use
Run the script and input the eBay URL with the desired filters (ensure the 'sold' filter is selected).
The script will retrieve and process the data, displaying product information in the console.
The extracted data is saved to a CSV file for further analysis.
Dependencies
requests
BeautifulSoup
Pandas
