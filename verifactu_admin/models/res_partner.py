from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    remote_username = fields.Char()
    remote_password = fields.Char()
