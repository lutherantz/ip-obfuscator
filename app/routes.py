import random
from .app import app
from requests import Session
from flask import render_template, Response, jsonify, request

class Routes:
    def __init__(self) -> None:
        self.config = {
            "host": "127.0.0.1",
            "port": "1337",
            "debug": True
        }

        self.routes = {
            "/": {
                "function": self._index,
                "methods": ["GET",]
            },
        }

        self.error = {
            "NOTHING": 0,
            "ERROR_DATA": 1,
            "ERROR_PARAMS": 2,
            "ERROT_JSON_DATA": 3,
            "ERROR_NOT_FOUND": 4,
            "ERROR_ALGO": 5,
            "ERROR_METHOD": 6,
        }

    def _obf(self, ip):
        ip_split = ip.split('.')
        hex_ip = ''.join(['0' + format(int(e), 'x')[-2:] for e in ip_split])
        oct_ip = '.'.join(['{0:03o}'.format(int(e)) for e in ip_split])
        dec_ip = str(int(hex_ip, 16))

        return ip, hex_ip, dec_ip, oct_ip

    def _index(self):
        try:
            data = request.json

            ip = data.get("ip")

            if ip:
                ipx, hex_ip, dec_ip, oct_ip = self._obf(ip)

                return jsonify({
                    "errorCode": self.error["NOTHING"],
                    "content": {
                        "standart": ipx,
                        "hexadecimal": hex_ip,
                        "decimal": dec_ip,
                        "octogonal": oct_ip
                    }
                })
        except:
            return jsonify({
                "errorCode": self.error["ERROT_JSON_DATA"],
                "content": "You must send the request like this: https://reqbin.com/code/python/m2g4va4a/python-requests-post-json-example"
            })