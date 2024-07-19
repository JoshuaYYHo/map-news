import requests
from datetime import date
import pycountry
# Need to convert the country name first
def get_iso_country_code(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        return country.alpha_2.lower()
    except LookupError:
        return None

#https://worldnewsapi.com/docs/top-news/
def get_news(country_iso_code):
    if not country_iso_code:
        return None

    today_date = str(date.today())
    #top news
    
    # Later Feature - Maybe do different endpoints

    url = "https://api.worldnewsapi.com/top-news?source-country={}&language=en&date={}".format(country_iso_code, today_date) # Date: 2024-05-29
    api_key = "1d7fe406813549108a2d7a9cee330451"

    headers = {
        'x-api-key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return  response.json()
    else:
        return f"Error: {response.status_code}"


def get_items(country_name):
    country_iso = get_iso_country_code(country_name)
    news_of_country = get_news(country_iso)

    output_list = []
    #only getting the title and id
    for cluster in news_of_country["top_news"]:
        for news_item in cluster["news"]:
            title = news_item["title"]
            author = news_item["author"]
            # cutting the first 100 characters
            text = news_item["text"][:100] + "..."
            url = news_item["url"]
            image = news_item["image"]
            output_list.append((title, author, text, url, image))

    return output_list

# New Idea, instead continously calling the API, store the raw list into a database