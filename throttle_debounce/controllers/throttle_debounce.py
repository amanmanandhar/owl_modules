from odoo import http
from odoo.http import request

class ThrottleDebounce(http.Controller):
    @http.route('/throttle_debounce', auth="public", website=True)
    def throttle_debounce(self):
        return request.render('throttle_debounce.throttle_debounce_view')