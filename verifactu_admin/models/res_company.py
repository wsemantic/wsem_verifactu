from odoo import models, fields, api


class Company(models.Model):
    _inherit = 'res.company'

    client_server_address = fields.Char()
    client_server_api_key = fields.Char()
