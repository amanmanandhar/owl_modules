from odoo import fields, models, api

class WelcomeUser(models.TransientModel):
    _name = 'welcome.user'

    message  = fields.Char(string="Message", compute="_compute_message")

    def _compute_message(self):
        for rec in self:
            rec.message = f"Welcome {self.env.user.name}"