# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request , Response
import json
from .jsonmixin import JsonControllerMixin
from . import helper


class saleController(http.Controller):
    JsonControllerMixin.patch_for_json("/order")
    @http.route("/order", auth="public", csrf=False,methods=["POST"])
    def sale_quotation_create(self,**kw):
        kw = helper.get_json_body()
        data = {}

        partner = http.request.env["res.partner"].sudo().search([('id', '=', kw.get('partner_id'))])
        print (partner.id)
        o = 1
        if not kw.get('order_line'):
            data.update({"order_line": "Is not array"})
            return Response(json.dumps(data,indent=4),status=400)
        else:
            for ol in kw.get('order_line'):
                if not kw.get('name') or not partner or not kw.get('company_id') or \
                        type(kw.get('order_line')) is not list or type(ol['product_id']) is not int\
                        or type(ol['price_unit']) is not int or type(ol['product_uom_qty']) is not int\
                        or type(ol['product_uom']) is not int:

                    if not kw.get('name'):
                        data.update({"name": "Required"})
                    if not partner:
                        data.update({"partner_id": "Not Found"})
                    if not kw.get('company_id'):
                        data.update({"company_id": "Required"})
                    if type(kw.get('order_line')) is not list:
                        data.update({"order_line": "Is not array"})
                    data.update({'succses':False})
                    if type(ol['product_id']) is not int:
                        data.update({"order_line." + str(o) + ".product_id": "Is not Integer"})
                    if type(ol['product_uom_qty']) is not int:
                        data.update({"order_line." + str(o) + ".product_uom_qty": "Is not integer"})
                    if type(ol['product_uom']) is not int:
                        data.update({"order_line." + str(o) + ".product_uom": "Is not interger"})
                    if type(ol['price_unit']) is not int:
                        data.update({"order_line." + str(o) + ".price_unit": "Is not interger"})

                    return Response(json.dumps(data,indent=4),status=400)
                else:
                    order = {
                        "name": kw.get('name'),
                        "partner_id": partner.id,
                        "date_order": kw.get('date_order'),
                        "company_id": kw.get('company_id'),
                    }
                    sale_order = http.request.env["sale.order"].sudo().create(order)
                    product =  http.request.env["product.product"].sudo().search([('id', '=', ol.get('product_id'))])
                    # product_tmpl = http.request.env["product.template"].sudo().search([('id', '=', product.product_tmpl_id.id)])
                    order_line = {
                        "order_id":sale_order.id,
                        'name': '['+str(product.default_code)+']'+ str(product.product_tmpl_id.name),
                        "product_id": ol.get('product_id'),
                        "product_uom": ol.get('product_uom'),
                        "product_uom_qty": ol.get('product_uom_qty'),
                        "price_unit": ol.get('price_unit'),
                    }
                    print (order_line)

                    sale_order_line = http.request.env["sale.order.line"].sudo().create(order_line)

                    data = {
                        'succses': True,
                        'message': 'Success'
                    }

                    return json.dumps(data,indent=4)

    @http.route("/order/<int:id>", auth="public", csrf=False,methods=["GET"])
    def sale_quotation_get_by_id(self,id,**kw):

        company = request.env.company
        sale = http.request.env["sale.order"].sudo().search([('id','=',id)])
        print (sale)
        # sale = self.env['sale.order'].browse(kw.get('id'))

        if not sale:
            data = {
                'succses': False,
                'message': "order id not found"
            }
            return Response(json.dumps(data,indent=4),status=400)
            # return Response(
            #     json.dumps({"data": data, "error": "", "code": 400, "message": "order id not found"}),
            #     headers=headers_json,
            #     status=400,
            # )

        else:
            order_line = []
            p = []
            for ol in sale.order_line:
                order_line.append({
                    "price_unit":ol.price_unit,
                    "product_id":ol.product_id.id,
                    "product_uom_qty":ol.product_uom_qty,
                    "product_uom": ol.product_uom.id
                })
                p.append({
                    "product_id":ol.product_id.id,
                    "name":ol.product_id.product_tmpl_id.name,
                    "description":ol.product_id.default_code,
                    "price": ol.product_id.product_tmpl_id.list_price
                })

            order = {
                "name":sale.name,
                "partner_id":sale.partner_id.id,
                "date_order":str(sale.date_order),
                "relationship":{
                    "partner":{
                        "partner_id":sale.partner_id.id,
                        "name":sale.partner_id.name,
                        "address":sale.partner_id.street
                    }
                },
                "product":p,
                "company": {
                    "id":sale.company_id.id,
                    "name":sale.company_id.name,
                    "description":sale.company_id.report_header
                },
                "order_line":order_line

            }
            data = {
                'success': True,
                'message': "Data Found",
                'data': order
            }

            return json.dumps(data,indent=4)