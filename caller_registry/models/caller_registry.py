from odoo import models, fields, api

class CallerRegistry(models.Model):
    _name = 'caller.registry'
    _description = 'Caller Registry'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')