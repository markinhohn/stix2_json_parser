#! /usr/bin/env python3
from flask import Flask, Response

app = Flask(__name__)

@app.route("/cisa_domain_dnsb2.txt")
def serverfile():
    with open('cisa_domain_dnsb2.txt', 'r') as handle:
        content = handle.read()

    return Response(content, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)