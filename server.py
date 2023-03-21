from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return '<h3>Start</h3>'


@app.route('/webhook/<int:mycode>', methods=['POST'])
def handle_webhook_post(mycode):
    if 99 < mycode < 600:
        response_code = int(request.args.get('response_code', mycode))
        response_data = {"status": "success", "message": "Webhook received."}
        return jsonify(response_data), response_code
    else:
        return 'Response code incorrect', 500


@app.route('/webhook/<int:mycode>', methods=['GET'])
def handle_webhook_get(mycode):
    if 99 < mycode < 600:
        response_code = int(request.args.get('response_code', mycode))
        response_data = {"status": "success", "message": "Webhook received."}
        return jsonify(response_data), response_code
    else:
        return 'Response code incorrect', 500


if __name__ == '__main__':
    app.run(debug=True)
