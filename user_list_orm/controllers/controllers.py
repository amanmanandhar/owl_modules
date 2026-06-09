# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeListOrm(http.Controller):
#     @http.route('/employee_list_orm/employee_list_orm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_list_orm/employee_list_orm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_list_orm.listing', {
#             'root': '/employee_list_orm/employee_list_orm',
#             'objects': http.request.env['employee_list_orm.employee_list_orm'].search([]),
#         })

#     @http.route('/employee_list_orm/employee_list_orm/objects/<model("employee_list_orm.employee_list_orm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_list_orm.object', {
#             'object': obj
#         })

