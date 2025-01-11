import pyupbit
from openai import OpenAI
import json
import time



def ai_trading():
    coin_data = {}

    all_coins = pyupbit.get_tickers(fiat="KRW")
    
    cnt = 1

    for ticker in all_coins:
        df = pyupbit.get_ohlcv(ticker, interval="day", count=1)

        if df is not None and not df.empty:
            volume = df['volume'].iloc[-1]
            print(f"{ticker}의 최근 24시간 거래량: {volume}")
            coin_data[ticker] = volume
        else:
            print("데이터를 가져오는 데 실패했습니다.")

        time.sleep(0.1)


    sorted_coin_data = sorted(coin_data.items(), key=lambda item: item[1], reverse=True)

    top5_coins = sorted_coin_data[:5]
    top5_coins_list = [coin[0] for coin in top5_coins]

    print(f'5개: {top5_coins_list}')
    print()

    for ticker in top5_coins_list:
        df = pyupbit.get_ohlcv(ticker, count=30, interval="day")

        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                        "type": "text",
                        "text": "You are an expert in Bitcoin investing. Tell me whether to buy, sell, or hold at the moment based on the chart data provided. response in json format. reaeon is answer in KOREAN.\n\nResponse Example:\n{\"decision\": \"buy\", \"reason\": \"some technical reason\"}\n{\"decision\": \"sell\", \"reason\": \"some technical reason\"}\n{\"decision\": \"hold\", \"reason\": \"some technical reason\"}"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": df.to_json()
                        }
                    ]
                }
            ],
            response_format={
                "type": "json_object"
            }
        )

        result = response.choices[0].message.content
        result = json.loads(result)
    
        print(f'종목 : {ticker}')
        print("### AI Decision: ", result["decision"].upper(), "###")
        print(f"### Reason: {result['reason']} ###")
        print()
        print(df.tail())
        print()



        if result["decision"] == "buy":
            pass
        elif result["decision"] == "sell":
            pass
        elif result["decision"] == "hold":
            pass





ai_trading()