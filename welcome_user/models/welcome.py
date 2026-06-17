from odoo import fields, models, api

class WelcomeUser(models.TransientModel):
    _name = 'welcome.user'

    message = fields.Char(
        default=lambda self: f"Welcome {self.env.user.name}", readonly=True,
    )

