import requests
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

#REST API URL
api_key = 'z260j295e191p057c040j080o1'

def get_exchange_rates_by_date(date_str):
    url = f'https://unipass.customs.go.kr:38010/ext/rest/trifFxrtInfoQry/retrieveTrifFxrtInfo?crkyCn={api_key}&qryYymmDd={date_str}&imexTp=2'

    response = requests.get(url)
    root = ET.fromstring(response.text)
    data = []

    for item in root.findall('trifFxrtInfoQryRsltVo'):
        row = {
            'Country_Code': item.findtext('cntySgn'),
            'Currency_Name': item.findtext('mtryUtNm'),
            'Exchange_Rate': item.findtext('fxrt'),
            'Currency_Sign': item.findtext('currSgn'),
            'Apply_Begin_Date': item.findtext('aplyBgnDt'),
            'Import_Export_Type': item.findtext('imexTp')
        }
        data.append(row)

    df = pd.DataFrame(data)
    return df


def get_today_exchange_rates():
    today_str = datetime.now().strftime('%Y%m%d')

    urltoday = f'https://unipass.customs.go.kr:38010/ext/rest/trifFxrtInfoQry/retrieveTrifFxrtInfo?crkyCn={api_key}&qryYymmDd={today_str}&imexTp=2'

    responsetoday = requests.get(urltoday)
    roottoday = ET.fromstring(responsetoday.text)
    datatoday = []

    for item in roottoday.findall('trifFxrtInfoQryRsltVo'):
        row = {
            'Country_Code': item.findtext('cntySgn'),
            'Currency_Name': item.findtext('mtryUtNm'),
            'Exchange_Rate': item.findtext('fxrt'),
            'Currency_Sign': item.findtext('currSgn'),
            'Apply_Begin_Date': item.findtext('aplyBgnDt'),
            'Import_Export_Type': item.findtext('imexTp')
        }
        datatoday.append(row)
    dftoday = pd.DataFrame(datatoday)
    return dftoday