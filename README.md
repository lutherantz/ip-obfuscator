<h1 align="center">IP Obfuscator <3</h1>

<p align="center">
  <b>🖤 Follow me here:</b><br>
  <a href="https://github.com/lutherantz">Github</a>
  <br>
  <br>
  <img src="https://cdn.discordapp.com/attachments/1211337418473738242/1212033846048985088/arbreee-2.jpg?ex=65f05d7b&is=65dde87b&hm=eb580289609c2c992734fe3aac502adba36da67658bd9c22934a989f3d9c7d10&" width="671" height="671">
</p>

#

## Setup:
```cs
/*
  *- Download / install python 3.5+ (click to add path)
  *- Install "Requests, Flask"
*/
```

#

## Script:
```python
from requests import get

res = get(
    "http://127.0.0.1:1337/",
    json = {
        "ip": "127.0.0.1" # REPLACE WITH DE DESIRED IP
    }
)

print(res.text)
```

#

## Response:
```cs
{
  "content": {
    "decimal": "2130706433",
    "hexadecimal": "07f000001",
    "octogonal": "177.000.000.001",
    "standart": "127.0.0.1"
  },
  "errorCode": 0
}
```

## ✨ Thanks

Don't Forget to Star the project !
