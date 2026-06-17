from odoo import http
from odoo.http import request

class WelcomeCheck(http.Controller):
    @http.route('/welcome_user/check', type='json', auth='user')
    def check_user(self):
        if request.session.get('welcome_shown'):
            return False

        request.session['welcome_shown'] = True
        return True
