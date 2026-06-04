# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteCounterOwl(http.Controller):
#     @http.route('/website_counter_owl/website_counter_owl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_counter_owl/website_counter_owl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_counter_owl.listing', {
#             'root': '/website_counter_owl/website_counter_owl',
#             'objects': http.request.env['website_counter_owl.website_counter_owl'].search([]),
#         })

#     @http.route('/website_counter_owl/website_counter_owl/objects/<model("website_counter_owl.website_counter_owl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_counter_owl.object', {
#             'object': obj
#         })

