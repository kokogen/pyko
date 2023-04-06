import requests

payload =  {'website': 'heihei.ru', 'established': 2018}

r =  requests.post("https://httpbin.org/post", data=payload)

print(f"url: {r.url} \n\ntext: \n {r.text}")

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