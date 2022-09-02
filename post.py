from flask import Flask, request
import requests
import json
import sys
import os

app = Flask(__name__)

# @app.route('/', methods=['POST'])
@app.route('/', methods=['GET'])
def index():
    doc = request.args.get('doc')
    # doc = json.loads(request.data)['doc']
    print('DOC :', doc)
    if len(doc) == 10:
        doc = '0' + doc
    if len(doc) == 9:
        doc = '00' + doc

    if len(doc) == 11:
        cpf = '{}.{}.{}-{}'.format(doc[:3], doc[3:6], doc[6:9], doc[9:])
        print(cpf)
        return json.dumps({'data': cpf})

    if len(doc) == 14:
        cnpj = '{}.{}.{}/{}-{}'.format(doc[:2], doc[2:5], doc[5:8], doc[8:12], doc[12:14])

        print(cnpj)
        return json.dumps({'data': cnpj})

    # Se vier vazio
    return None

@app.route('/ddd', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
