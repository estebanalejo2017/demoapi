#primer ejemplo completo, aca se usa Flask, se hace la consulta y se publica en localhost
#aca esta el codigo, no se importa de otro archivo como en api2
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/company")
def  get_company_data():
    user_agent = {'User-agent': 'Mozilla/5.0'}
    symbol = "INTC"  # Ticker de INTEL
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    r = requests.get(url, headers=user_agent)

    print(r.json())
    my_data_selection = {
        "nombre": r.json()["quoteSummary"]["result"][0]["price"]["shortName"],
        "ticker": r.json()["quoteSummary"]["result"][0]["price"]["symbol"],
        "precio": r.json()["quoteSummary"]["result"][0]["summaryDetail"]["previousClose"]["raw"]
    }

    #print(my_data_selection)
    return my_data_selection

if __name__ == '__main__':
    app.run()