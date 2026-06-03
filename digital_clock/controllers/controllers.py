# -*- coding: utf-8 -*-
# from odoo import http


# class DigitalClock(http.Controller):
#     @http.route('/digital_clock/digital_clock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/digital_clock/digital_clock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('digital_clock.listing', {
#             'root': '/digital_clock/digital_clock',
#             'objects': http.request.env['digital_clock.digital_clock'].search([]),
#         })

#     @http.route('/digital_clock/digital_clock/objects/<model("digital_clock.digital_clock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('digital_clock.object', {
#             'object': obj
#         })

