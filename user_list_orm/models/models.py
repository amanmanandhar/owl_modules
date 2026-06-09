# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class employee_list_orm(models.Model):
#     _name = 'employee_list_orm.employee_list_orm'
#     _description = 'employee_list_orm.employee_list_orm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

