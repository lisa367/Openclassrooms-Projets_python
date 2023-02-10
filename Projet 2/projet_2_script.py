import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from pathlib import Path
import csv


todays_date = dt.today()
extraction_date = todays_date.strftime("%Y-%m-%d_%H%M%S")

data_directory = Path.cwd() / "Data"
images_directory = data_directory / "Images"

data_directory.mkdir(exist_ok=True)
images_directory.mkdir(exist_ok=True)

landing_page_url = "https://books.toscrape.com/"


###          PHASE 1            ###

def request_and_parse(url):
    response = rq.get(url)
    soup = bs(response.text, "html.parser") if response.ok else 'error'

    return soup

def create_image_file(image_url, book_url):
    image_file_name = f"{book_url.split('/')[-2]}.jpg"
    # print(image_file_name)
    image_file_path = images_directory / f"{image_file_name}"
    if not image_file_path.exists():
        with open(image_file_path, 'wb') as image_file:
            r = rq.get(image_url, stream=True)
            if r.ok:
                image_file.write(r.content)

def get_book_info(book_url):
    soup = request_and_parse(book_url)
    if soup != 'error':
        table_data = [td.contents[0] for td in soup.select("td")]
        summary = soup.select("#product_description ~ p")

        upc = table_data[0]
        title = soup.select("h1")[0].contents[0]
        category = soup.select(".breadcrumb li:nth-of-type(3) a")[0].contents[0]
        price_including_tax = table_data[2].strip("Â£")
        price_excluding_tax = table_data[3].strip("Â£")
        available_stock = table_data[5].strip("In stock (").strip(" available)")
        star_rating = soup.select(".star-rating")[0]['class']
        product_page_url = book_url
        image_url = f"{landing_page_url}{soup.select('.carousel-inner > div > img')[0]['src'].strip('../..')}"
        product_description = summary[0].contents[0].strip("...more") if summary else ''

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

        create_image_file(image_url, book_url)

        book_info = {"universal_ product_code": upc, "title": title, "category": category, "price_including_tax": price_including_tax, "price_excluding_tax": price_excluding_tax, "number_available": available_stock, "review_rating": review_rating, "product_page_url": product_page_url, "image_url": image_url, "product_description": product_description}

        return book_info

    else:
        return "La requête n'a pu aboutir."

print(extraction_date)
# print(request_and_parse("https://looks.toscrape.com/"))
# print(get_book_info("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"))


def create_book_file(book_url):
    book_info = get_book_info(book_url)
    book_info["extraction_date"] = extraction_date
    book_title = '_'.join(book_info["title"].lower().split(' '))
    book_file_path = data_directory / f"{book_title}.csv"

    mode = 'w' if not book_file_path.exists() else 'a'

    with open(book_file_path, mode=mode, newline='') as file:
        fieldnames = ["extraction_date", "universal_ product_code", "title", "category", "price_including_tax", "price_excluding_tax", "number_available", "review_rating", "product_page_url", "image_url", "product_description"]
        outputfile = csv.DictWriter(file , fieldnames=fieldnames, delimiter="\t")
        if mode == 'w':
            outputfile.writeheader()
        outputfile.writerow(book_info)

# create_book_file("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")

###          PHASE 2            ###

def create_csv_file(category_name, urls):
    category_file_path = data_directory / f"{category_name}_{extraction_date}.csv"

    with open(category_file_path, 'w', newline='') as file:
        fieldnames = ["universal_ product_code", "title", "category", "price_including_tax", "price_excluding_tax", "number_available", "review_rating", "product_page_url", "image_url", "product_description"]
        outputfile = csv.DictWriter(file , fieldnames=fieldnames, delimiter="\t")
        outputfile.writeheader()
        for url in urls:
            data = get_book_info(url)
            outputfile.writerow(data)

def parse_category(category_name):
    category_url = f"{landing_page_url}catalogue/category/books/{category_name}_{all_categories.index(category_name)+1}/index.html"
    category_page = request_and_parse(category_url)

    max_page = category_page.select(".current")
    total_pages = int(max_page[0].contents[0].strip("\n            \n                ").split(" ")[-1]) if max_page else 1
    books_urls = []

    for i in range(1, total_pages+1):
        url = category_url.replace('index', f'page-{i}') if total_pages > 1 else category_url
        # print(url)
        soup = request_and_parse(url)
        hyperlinks = [link['href'].strip("../../../") for link in soup.select(".image_container a")]
        books_on_page = [f"{landing_page_url}catalogue/{link}" for link in hyperlinks]
        # print(books_on_page)
        books_urls += books_on_page

        create_csv_file(category_name, books_urls)
    
    # print(total_pages)
    # print(books_on_page)
    # print(books_urls)
    return books_urls

###          PHASE 3            ###

landing_page_soup = request_and_parse(landing_page_url).select("aside a")
all_categories = ["-".join(category.contents[0].lower().strip("\n                            \n").split(" ")) for category in landing_page_soup]

for category in all_categories:
    if category == "books":
        continue
    parse_category(category)


###          PHASE 4            ###

# print(landing_page_soup)
# print(all_categories)
# parse_category("poetry")
