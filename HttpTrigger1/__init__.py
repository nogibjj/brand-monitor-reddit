import logging

import azure.functions as func
from flask import Flask, redirect

app = Flask(__name__)

# code for azure function
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the WSGI handler.
    """
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)

# flask app
@app.route('/')
def index():
    logging.info("flask app - about to do a redirect")
    return redirect("https://www.google.com", code=302)