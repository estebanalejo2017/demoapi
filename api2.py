#creacion de api con Flask importando query
from flask import Flask,request
from query import get_company_information
from query_wallapop import get_wallapop


app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/api/yahoo")
def get_company():
    symbol = "AAPL"
    return get_company_information(symbol)

@app.route("/api/wallapop")
def get_product_and_price_average():
    query = request.args.get('search_text')
    if query is None:
        return "empty query"
    return get_wallapop(query)

if __name__ == '__main__':
    app.run()