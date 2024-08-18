

import os
import openai
import sys
from bs4 import BeautifulSoup
import requests

import time

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

subscription_key = os.environ['BING_SEARCH_API_KEY']

def scrape_text_from_url(url):
    # Step 1: Send a request to the website
    response = requests.get(url)
    response.raise_for_status()  # Check that the request was successful

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 3: Find and extract all useful text (body, paragraphs, etc.)
    paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    scraped_text = []
    for paragraph in paragraphs:
        text = paragraph.get_text().strip()
        if text:  # Only add non-empty text
            scraped_text.append(text)

    # Join the extracted text into a single string
    scraped_text = '\n\n'.join(scraped_text)

    # Step 4: Return the URL and the scraped text in a dictionary
    return {
        'url': url,
        'scraped_text': scraped_text
    }


def getUrlfromBing2(count=5, search_term="top 10 places to visit in dubai"):
    # Replace with your Bing Search API key
    search_url = "https://api.bing.microsoft.com/v7.0/search"

    # Define headers and parameters for the request
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML", "count": count}

    # Make the request to Bing API
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()

    # Extract the search results
    search_results = response.json()

    results = {}
    for result in search_results["webPages"]["value"]:
        url = result["url"]
        title = result["name"]

        time.sleep(3)
        # Attempt to make a request to the URL
        try:
            page_response = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            })
            page_response.raise_for_status()  # Will raise an error for a 403 Forbidden or other issues

            # If no exception, add to results
            results[title] = url
            print(f"Successfully accessed: {title} - {url}")

        except requests.exceptions.RequestException as e:
            # Skip the URL if any request-related error occurs, e.g., 403 Forbidden
            print(f"Skipping {title} - {url} due to error: {e}")
            continue  # Skip to the next URL

    return results

def getUrlfromBing(count = 5, search_term = "top 10 places to visit in dubai"):
    # Replace with your Bing Search API key
    search_url = "https://api.bing.microsoft.com/v7.0/search"

    # Define headers and parameters for the request
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML", "count": count}

    # Make the request
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()

    # Extract the search results
    search_results = response.json()

    # Print the titles and links of the first few results
    count = 1

    results = {}
    for result in search_results["webPages"]["value"]:
        results[result["name"]] = result["url"]
        # print(count)
        # print(result["name"])
        # print(result["url"])
        # count+=1
    return results

    # scrape these links
    
url_dict = getUrlfromBing2(count = 5, search_term = "top 10 places to visit in dubai")

count = 1
for key, v in url_dict.items():
    print(count)
    result = scrape_text_from_url(v)
    print(result['scraped_text'])
    count+=1

# url = "https://www.visitdubai.com/en/articles/top-things-to-do-in-dubai"
# result = scrape_text_from_url(url)
# print(result['scraped_text'])