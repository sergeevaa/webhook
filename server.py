from flask import Flask, request, jsonify, abort

app = Flask(__name__)


def create_status_dict():
    return {
        range(100, 200): {"status": "Informational", "message": "Working"},
        range(200, 300): {"status": "Success", "message": "Ok"},
        range(300, 400): {"status": "Redirection", "message": "Working"},
        range(400, 500): {"status": "Client Error", "message": "Error"},
        range(500, 600): {"status": "Server Error", "message": "Error"},
    }


def validate_code(mycode):
    return isinstance(mycode, int) and 100 <= mycode <= 599


error_messages = {
    400: "Bad Request",
    404: "Not Found",
    500: "Internal Server Error",
}

status_dict = create_status_dict()


@app.route('/')
def home():
    return '<h3>Start</h3>'


@app.route('/webhook/<int:mycode>', methods=['GET', 'POST'])
def handle_webhook(mycode):
    if not validate_code(mycode):
        abort(500)

    response_code = int(request.args.get('response_code', mycode))

    for k, v in status_dict.items():
        if mycode in k:
            return jsonify(v), response_code

    abort(500)


if __name__ == '__main__':
    app.run(debug=True)
