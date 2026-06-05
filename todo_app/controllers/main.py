from odoo import http
from odoo.http import request

class TodoController(http.Controller):
    @http.route('/todo', type='http', auth="public", website=True)
    def todo_show(self):
        return request.render('todo_app.todo_page')