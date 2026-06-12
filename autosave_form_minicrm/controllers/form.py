from odoo import http
from odoo.http import request

class AutoSaveForm(http.Controller):
    @http.route('/auto_form', type='http', auth='public', website=True)
    def auto_form(self):
        return request.render('autosave_form_minicrm.mini_crm')