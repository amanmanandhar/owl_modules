from odoo import http
from odoo.http import request

class CounterApp(http.Controller):
    @http.route('/counter', type='http', auth="public", website=True)
    def counter(self):
        return request.render('website_counter_owl.counter_page')