import os

from flask import Flask, request, render_template, send_from_directory, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return f'<h3>Start</h3>'


@app.route('/webhook/<int:mycode>', methods=['POST'])
def handle_webhook_get(mycode):
    if 99 < mycode < 600:
        data = request.get_json()
        response_code = int(request.args.get('response_code', mycode))
        return jsonify({'request': request.remote_addr, 'code': response_code, 'data': str(data)}), response_code
    else:
        return 'Response code incorrect', 500


@app.route('/webhook/<int:mycode>', methods=['GET'])
def handle_webhook_get(mycode):
    if 99 < mycode < 600:
        data = request.args.get('data')
        response_code = int(request.args.get('response_code', mycode))
        return jsonify({'request': request.remote_addr, 'code': response_code, 'data': str(data)}), response_code
    else:
        return 'Response code incorrect', 500


if __name__ == '__main__':
    app.run(port=5001)
    app.debug = True
