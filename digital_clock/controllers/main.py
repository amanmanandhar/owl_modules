from odoo import http
import logging

_logger = logging.getLogger(__name__)

class DigitalClockWebsite(http.Controller):
    @http.route('/digital-clock', type='http', auth='public',website=True)
    def clock_page(self, **kw):
        return http.request.render('digital_clock.clock_page')