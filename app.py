"""
A business flask app
    :param name: String
    :param email: String
    :param phone_number: string
    :param description: string
    :param street_address: string
    :param service_type: string
    :param hours_operation: string
    param reviews: string
"""
import flask
from flask.views import MethodView
from index import Index
from sign import Sign

app = flask.Flask(__name__)       # Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/sign/',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
