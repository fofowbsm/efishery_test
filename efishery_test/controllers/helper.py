# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

headers_json = {"Content-Type": "application/json"}


def error(error, message, code):
    return Response(
        json.dumps({"data": None, "error": error, "code": code, "message": message}),
        headers=headers_json,
        status=code,
    )


def ok(data):
    return Response(
        json.dumps({"data": data, "error": "", "code": 200, "message": "success"}),
        headers=headers_json,
        status=200,
    )


def not_found(message):
    return error("Not Found", message, 404)


def unauthorized(message):
    return error("Unauthorized", message, 403)


def internal_error(message):
    return error("Internal Error", message, 500)


def bad_request(message):
    return error("Bad request", message, 400)


def get_json_body():
    return json.loads(http.request.httprequest.data.decode("utf-8"))
