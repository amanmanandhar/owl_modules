from odoo import http
from odoo.http import request

class UserList(http.Controller):
    @http.route('/user-list',type='http', auth="user", website=True)
    def user_list(self):
        return request.render('user_list_orm.list_view')