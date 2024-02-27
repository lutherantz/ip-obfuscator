from requests import get

res = get(
    "http://127.0.0.1:1337/",
    json = {
        "ip": "127.0.0.1"
    }
)

print(res.text)