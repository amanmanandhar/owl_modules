# -*- coding: utf-8 -*-
# from odoo import http


# class WelcomeUser(http.Controller):
#     @http.route('/welcome_user/welcome_user', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/welcome_user/welcome_user/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('welcome_user.listing', {
#             'root': '/welcome_user/welcome_user',
#             'objects': http.request.env['welcome_user.welcome_user'].search([]),
#         })

#     @http.route('/welcome_user/welcome_user/objects/<model("welcome_user.welcome_user"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('welcome_user.object', {
#             'object': obj
#         })

