# -*- coding: utf-8 -*-
# from odoo import http


# class ThrottleDebounce(http.Controller):
#     @http.route('/throttle_debounce/throttle_debounce', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/throttle_debounce/throttle_debounce/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('throttle_debounce.listing', {
#             'root': '/throttle_debounce/throttle_debounce',
#             'objects': http.request.env['throttle_debounce.throttle_debounce'].search([]),
#         })

#     @http.route('/throttle_debounce/throttle_debounce/objects/<model("throttle_debounce.throttle_debounce"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('throttle_debounce.object', {
#             'object': obj
#         })

