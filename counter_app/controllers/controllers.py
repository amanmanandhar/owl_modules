# -*- coding: utf-8 -*-
# from odoo import http


# class CounterApp(http.Controller):
#     @http.route('/counter_app/counter_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/counter_app/counter_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('counter_app.listing', {
#             'root': '/counter_app/counter_app',
#             'objects': http.request.env['counter_app.counter_app'].search([]),
#         })

#     @http.route('/counter_app/counter_app/objects/<model("counter_app.counter_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('counter_app.object', {
#             'object': obj
#         })

