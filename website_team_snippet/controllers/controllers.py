# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteTeamSnippet(http.Controller):
#     @http.route('/website_team_snippet/website_team_snippet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_team_snippet/website_team_snippet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_team_snippet.listing', {
#             'root': '/website_team_snippet/website_team_snippet',
#             'objects': http.request.env['website_team_snippet.website_team_snippet'].search([]),
#         })

#     @http.route('/website_team_snippet/website_team_snippet/objects/<model("website_team_snippet.website_team_snippet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_team_snippet.object', {
#             'object': obj
#         })

