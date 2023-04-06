import requests

payload =  {'page': 2, 'count': 25}

r =  requests.get("https://httpbin.org/get", params=payload)

#print(f"url: {r.url} \n\ntext: \n {r.text}")
json_dict = r.json()
keys = json_dict.keys()

for k in keys:
    print(f"{k} : ")
    v = json_dict[k]
    if type(v) == dict:
        for e in v.keys():
            print(f"\t {e} : {v[e]}")
    else:
        print(f"\t {json_dict[k]}")