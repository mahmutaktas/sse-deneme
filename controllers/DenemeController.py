import flask
from flask_cors import cross_origin
from flask import request, Blueprint
from apscheduler.schedulers.background import BackgroundScheduler
from services import DenemeServices
from services.DenemeServices import publisher

deneme_page = Blueprint('deneme_page', __name__, template_folder= "templates")

@deneme_page.route('/deneme_sse', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin()
def get_raw_price_from_external_api():


    sched = BackgroundScheduler(daemon=True)

    sched.add_job(DenemeServices.deneme_function, 'interval', seconds=60)

    sched.start()

    return flask.Response(publisher.subscribe(), content_type='text/event-stream')


@deneme_page.route('/deneme', methods=['GET', 'POST', 'OPTIONS'])
def get_raw_price_from_external_apii():

    return {"success": True, "message": "deneme"}


