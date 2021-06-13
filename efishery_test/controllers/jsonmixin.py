# -*- coding: utf-8 -*-
from odoo import http
import re

class JsonControllerMixin(object):
    @staticmethod
    def patch_for_json(path_re):
        # this is to avoid Odoo, which assumes json always means json+rpc,
        # complaining about "function declared as capable of handling request
        # of type 'http' but called with a request of type 'json'"
        path_re = re.compile(path_re)
        orig_get_request = http.Root.get_request

        def get_request(self, httprequest):
            if path_re.match(httprequest.path):
                return http.HttpRequest(httprequest)
            return orig_get_request(self, httprequest)

        http.Root.get_request = get_request