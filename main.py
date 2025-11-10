from flask import Flask, render_template, request
import pandas as pd
import api
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today_str = datetime.now().strftime('%Y%m%d')
    dftoday = api.get_today_exchange_rates()

    query_date = request.args.get('date', today_str)
    day_str = query_date.replace("-", "")
    df = api.get_exchange_rates_by_date(day_str)

    rate_dict = dict(zip(dftoday['Currency_Name'], zip(dftoday['Exchange_Rate'], df['Exchange_Rate'])))

    return render_template("index.html", rate=rate_dict, today=today_str, selected_date=query_date)

if __name__ == '__main__':
    app.run(debug=True)