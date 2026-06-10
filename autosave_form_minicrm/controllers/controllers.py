# -*- coding: utf-8 -*-
# from odoo import http


# class AutosaveFormMinicrm(http.Controller):
#     @http.route('/autosave_form_minicrm/autosave_form_minicrm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autosave_form_minicrm/autosave_form_minicrm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('autosave_form_minicrm.listing', {
#             'root': '/autosave_form_minicrm/autosave_form_minicrm',
#             'objects': http.request.env['autosave_form_minicrm.autosave_form_minicrm'].search([]),
#         })

#     @http.route('/autosave_form_minicrm/autosave_form_minicrm/objects/<model("autosave_form_minicrm.autosave_form_minicrm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('autosave_form_minicrm.object', {
#             'object': obj
#         })

