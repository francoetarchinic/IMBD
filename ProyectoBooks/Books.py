import requests
from lxml import html 
import pandas as pd
'''
url = "https://books.toscrape.com/"

response = requests.get(url)

print(response.text[:500])
print(response.status_code)
print(response.headers)
'''
data = []

for page in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:
        response = requests.get(url)
        tree = html.fromstring(response.text)
        full_catalog = tree.xpath(".//ol/li")

        print("Página", page, "items:", len(full_catalog))

        for item in full_catalog:

            #Nombre del libro
            try:
                name = item.xpath(".//h3/a/@title")[0]
                print(name)
            except Exception as e:
                name = ""
                print("error",e)
            
            #Precio del libro
            try:
                price = item.xpath(".//div/p[@class='price_color']")[0].text
                price = price.replace("Â£", "").strip()
                print(price)
            except Exception as e:
                price = ""
                print("error",e)

            #Rating
            try:
                rating =item.xpath(".//p[contains(@class,'star-rating')]/@class")[0]
                rating_raw = rating.split(" ")[-1]
                print(rating_raw)
            except Exception as e:
                price = ""
                print("error",e)    

            book =  {
                'title' : name,
                'price' : price,
                'rating' : rating_raw
            }

            data.append(book)

    except Exception as e:
        print(e)

print(len(data))


df = pd.DataFrame(data)

df.to_csv("books.csv", index=False, encoding="utf-8.sig")

print("Proceso terminado")
print("Total libros", len(df))