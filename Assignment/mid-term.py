import requests
import json
import pandas as pd


api_key = "76484a4c647275643636684d55686f"
root_path = "Assignment/json_datas/df"

def save_api_data(year, month):
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/energyUseDataSummaryInfo/1/10/{year}/{month:02d}"
    try:
        res = requests.get(url)
        res.raise_for_status()

        data = res.json()['energyUseDataSummaryInfo']['row']
        print(f"{year}년 {month}월 API 응답:", res.status_code)

        for row in data:
            if (row['MM_TYPE']=='개인'):
                print(row)
                df = pd.DataFrame([row])
                df.to_json(f'{root_path}/energy_analysis_{year}_{month:02d}.json', orient='records', indent=4, force_ascii=False)

    except requests.exceptions.RequestException as e:
        print(f"API 호출 실패: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON 파싱 실패: {e}")

def save_all_data():
    for year in range(2015, 2025):
        for month in range(1, 13):
            save_api_data(year, month)

save_all_data()