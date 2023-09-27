from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

"""
A simple guestbook flask app.
    :param name: String
    :param email: String
    :param phone_number: string
    :param description: string
    :param street_address: string
    :param service_type: string
    :param hours_operation: string
    param reviews: string
"""

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['email'], request.form['phone_number'], request.form['description'], request.form['street_address'], request.form['service_type'], request.form['hours_operation'], request.form['reviews'])
        return redirect(url_for('index'))
