from flask import Flask, request
import requests
import json
import sys
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    doc = request.args.get('doc')
    if len(doc) == 10:
        doc = '0' + doc
    if len(doc) == 9:
        doc = '00' + doc
    
    if len(doc) == 11:
        cpf = '{}.{}.{}-{}'.format(doc[:3], doc[3:6], doc[6:9], doc[9:])
        print(cpf)
        return cpf

    if len(doc) == 14:
        cnpj = '{}.{}.{}/{}-{}'.format(doc[:2], doc[2:5], doc[5:8], doc[8:12], doc[12:14])

        print(cnpj)
        return cnpj

    # Se vier vazio
    return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
