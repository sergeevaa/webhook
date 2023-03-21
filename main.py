from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    print(data)
    response_code = int(request.args.get('response_code', '200'))
    return '', response_code


@app.route('/webhook', methods=['GET'])
def handle_webhook_get():
    data = request.args.get('data')
    response_code = int(request.args.get('response_code', '200'))
    print(data)
    return '', response_code


if __name__ == '__main__':
    app.run(port=443)
