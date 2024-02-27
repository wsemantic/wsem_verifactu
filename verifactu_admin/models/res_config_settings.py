from odoo  import models, fields ,api


class ConfigSetting(models.TransientModel):
    _inherit='res.config.settings'

    subs_client_server_address = fields.Char(related='company_id.client_server_address', readonly=False)
    subs_client_server_api_key = fields.Char(related='company_id.client_server_api_key', readonly=False)

