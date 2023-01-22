import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from pathlib import Path


todays_date = dt.today()
extraction_date = todays_date.strftime("%Y-%m-%d_%H%M%S")

data_directory = Path.cwd() / "data"
images_directory = data_directory / "images"

#data_directory.mkdir(exist_ok=True)
#images_directory.mkdir(exist_ok=True)


###          PHASE 1            ###

def request_and_parse(url):
    response = rq.get(url).text
    soup = bs(response, "html.parser")

    return soup


def get_book_info(book_url):
    soup = request_and_parse(book_url)
    # table_data = [bs(str(td), "html.parser").get_text() for td in soup.select("td")]
    table_data = [td.contents[0] for td in soup.select("td")]

    upc = table_data[0]
    title = soup.select("h1")[0].contents[0]
    category = soup.select(".breadcrumb li:nth-of-type(3) a")[0].contents[0]
    price_including_tax = table_data[2].strip("Â£")
    price_excluding_tax = table_data[3].strip("Â£")
    available_stock = table_data[5].strip("In stock (").strip(" available)")
    star_rating = bs(str(soup.select(".star-rating")), "html.parser").get_text()
    product_page_url = book_url
    image_url = soup.select(".carousel-inner > div > img")[0]['src']
    product_description = soup.select("#product_description ~ p")[0].contents[0]

    '''
    if "One" in star_rating:
        review_rating = 1
    elif "Two" in star_rating:
        review_rating = 2
    elif "Three" in star_rating:
        review_rating = 3
    elif "Four" in star_rating:
        review_rating = 4
    elif "Five" in star_rating:
        review_rating = 5
    '''

    book_info = {"upc": upc, "title": title, "category": category, "price_including_tax": price_including_tax, "price_excluding_tax": price_excluding_tax, "available_stock": available_stock, "review_rating": 'review_rating', "product_page_url": product_page_url, "image_url": image_url, "product_description": product_description}

    return book_info
    #return table_data


# print(extraction_date)
print(get_book_info("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"))