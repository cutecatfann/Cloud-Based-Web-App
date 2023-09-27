#:param name: String
#:param email: String
#:param phone_number: string
#:param description: string
#:param street_address: string
#:param service_type: string
#:param hours_operation: string
# param reviews: string

from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(name=row[0], email=row[1], phone_number = row[2],signed_on=row[3], description=row[4],street_address=row[5],service_type=row[6],hours_operation=row[7],reivews=row[8] ) for row in model.select()]
        return render_template('index.html',entries=entries)
