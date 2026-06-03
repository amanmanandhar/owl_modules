# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class digital_clock(models.Model):
#     _name = 'digital_clock.digital_clock'
#     _description = 'digital_clock.digital_clock'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

