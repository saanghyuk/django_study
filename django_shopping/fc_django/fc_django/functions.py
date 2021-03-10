import requests
import datetime


def get_exchange():
    today = datetime.datetime.now()
    if today.weekday() >= 5:
        diff = today.weekday() - 4
        today = today - datetime.timedelta(days=diff)

    today = today.strftime('%Y%m%d')

    auth = 'elRygCw18408LKjNX6WWzPbXbhhFOsEP'
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data=AP01'
    url = url.format(auth, today)
    res = requests.get(url)
    print(res)
    data = res.json()
    print(data)
    for d in data:
        if d['cur_unit'] == 'USD':
            return d['tts']
    return
