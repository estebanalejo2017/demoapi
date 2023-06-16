import requests
import urllib.parse

def get_wallapop(search_text: str):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    keywords = search_text  # producto a buscar
    keywords = urllib.parse.quote(keywords)
    url = f"https://api.wallapop.com/api/v3/general/search?filters_source=search_box&keywords={keywords}&longitude=-3.69196&latitude=40.41956"
    r = requests.get(url, headers=user_agent)

    ##print(r.json())
    search_results = r.json()["search_objects"]
    price_sum = 0
    elements = len(search_results)

    if elements == 0:
        return {
        "num_results": 0,
        "price_avg": None,
        "results": []
        }


    results = []
    for r in search_results:
        articulo = {
            "title": r['title'],
            "description": r['description'],
            "price": r['price']
        }


        results.append(articulo)
        #print("---------------------------------")
        price_sum = price_sum + r['price']

    print(elements, "elementos encontrados")
    print("precio promedio: ", price_sum / elements)
    price_avg = price_sum / elements

    return {
        "num_results": elements,
        "price_avg": price_avg,
        "results": results
    }


