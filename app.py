from flask import Flask, jsonify
from pylgate import generate_token
from pylgate.types import TokenType
import requests

app = Flask(__name__)

SESSION_TOKEN = bytes.fromhex("149e9b790f31c6f68a7122bf2416b697")
PHONE         = 33600000000
DEVICE        = "4G300208179"

@app.route('/open')
def open_gate():
    token = generate_token(SESSION_TOKEN, PHONE, TokenType.PRIMARY)
    r = requests.get(
        f'https://api1.pal-es.com/v1/bt/device/{DEVICE}/open-gate?outputNum=1',
        headers={'User-Agent': 'okhttp/4.9.3', 'X-Bt-Token': token}
    )
    return jsonify(r.json())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
