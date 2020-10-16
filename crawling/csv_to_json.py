import csv
import json
import pandas as pd
'''
[
    {
        "year":"2020",
        "publications":[
            {
                "title":"bl;dufl",
                "writer":"writer x",
                "academy":"acm 2020",
                "pdf":"www.naver.com",
                "section":"1"
            },
            {
                "title":"bl;dufldfs",
                "writer":"writer x, writer xy",
                "academy":"kdd 2020",
                "poster":"www.naver.com",
                "ppt":"www.daum.net",
                "section":"2"
               
            }
        ]
    },
    {
        "year":"2019",
        "publications":[
            {
                "title":"bl;dufl",
                "writer":"writer x",
                "academy":"acm 2019",
                "section":"2"
            },
            {
                "title":"bl;dufldfs",
                "writer":"writer x, writer xy",
                "academy":"kdd 2019",
                "section":"1"
            }
        ]
    }
]
'''

data = pd.read_csv('crawled_data.csv')


years = data['year'].unique().tolist()
years.sort(key= lambda x: -int(x))

arr = {}
for year in years:
    arr[year] = {"year": str(year), 'publications':[]}

for i, row in data.iterrows():
    arr[row['year']]['publications'].append(
        {
            "title": row.title,
            "writer": row.writer,
            "academy": row.ws,
            "section": "1"
        }
    )

final = list(arr.values())
#print(final)

json_val = json.dumps(final)
#print(json_val)

with open('real_publications.json', 'w') as f:
    json.dump(json_val,f)