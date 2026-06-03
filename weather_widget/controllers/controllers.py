from odoo import http


class WeatherPage(http.Controller):
    @http.route('/weather', type='http', auth='public', website=True)
    def weather(self):
        return http.request.render('weather_widget.weather_page')


