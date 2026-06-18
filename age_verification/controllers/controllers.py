# -*- coding: utf-8 -*-
# from odoo import http


# class AgeVerification(http.Controller):
#     @http.route('/age_verification/age_verification', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/age_verification/age_verification/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('age_verification.listing', {
#             'root': '/age_verification/age_verification',
#             'objects': http.request.env['age_verification.age_verification'].search([]),
#         })

#     @http.route('/age_verification/age_verification/objects/<model("age_verification.age_verification"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('age_verification.object', {
#             'object': obj
#         })

