import requests
import urllib.parse

user_agent = {'User-agent': 'Mozilla/5.0'}
keywords = "renault clio"  # producto a buscar
keywords = urllib.parse.quote(keywords)
url = f"https://api.wallapop.com/api/v3/general/search?filters_source=search_box&keywords={keywords}&longitude=-3.69196&latitude=40.41956"
r = requests.get(url, headers=user_agent)

##print(r.json())
search_results = r.json()["search_objects"]
price_sum = 0
elements = len(search_results)
for r in search_results:
    print(r['title'])
    print(r['description'])
    print(r['price'])
    print("---------------------------------")
    price_sum = price_sum + r['price']

print(elements, "elementos encontrados")
print("precio promedio: ", price_sum/elements)


