from odoo import models, fields, api


class SubscriptionLine(models.Model):
    _inherit = 'subscription.package.product.line'

    plan_id = fields.Many2one('subscription.package.plan')


class SaaSSubscription(models.Model):
    _inherit = 'subscription.package'

    remote_companyid = fields.Integer()

    @api.onchange('plan_id')
    def _onchange_number_of_users(self):
        if self.plan_id:
            if self.product_line_ids:
                self.product_line_ids.filtered(lambda x: x.plan_id).unlink()
                self.product_line_ids = [(0, 0, {
                    'plan_id': x.plan_id.id,
                    'product_id': x.product_id.id,
                    'product_qty': x.product_qty,
                    'product_uom_id': x.product_uom_id.id,
                    'uom_catg_id': x.uom_catg_id.id,
                    'unit_price': x.unit_price,

                }
                ) for x in self.plan_id.content_ids]

    def saas_deploy(self):
        pass
