# -*- coding: utf-8 -*-
# from odoo import http


# class Todo-app(http.Controller):
#     @http.route('/todo-app/todo-app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo-app/todo-app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo-app.listing', {
#             'root': '/todo-app/todo-app',
#             'objects': http.request.env['todo-app.todo-app'].search([]),
#         })

#     @http.route('/todo-app/todo-app/objects/<model("todo-app.todo-app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo-app.object', {
#             'object': obj
#         })

