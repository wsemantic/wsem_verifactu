from odoo import models, fields, api


class SubscriptionPackageProductLine(models.Model):
    """Subscription Plan Product Line Model"""
    _name = 'subscription.plan.product.line'
    _description = 'Subscription Plan Lines'

    plan_id = fields.Many2one('subscription.package.plan', store=True,
                              string='Subscription Plan')
    company_id = fields.Many2one('res.company', string='Company', store=True,
                                 related='plan_id.company_id')
    product_id = fields.Many2one('product.product', string='Product',
                                 store=True, ondelete='restrict',
                                 domain=[('is_subscription', '=', True)])
    product_qty = fields.Float(string='Quantity', store=True, default=1.0)
    product_uom_id = fields.Many2one('uom.uom', string='UoM', store=True,
                                     related='product_id.uom_id',
                                     ondelete='restrict')
    uom_catg_id = fields.Many2one('uom.category', string='UoM Category',
                                  store=True,
                                  related='product_id.uom_id.category_id')
    unit_price = fields.Float(string='Unit Price', store=True, readonly=False,
                              related='product_id.list_price')
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  store=True,
                                  related='plan_id.currency_id')
    total_amount = fields.Monetary(string='Subtotal', store=True,
                                   compute='_compute_total_amount')
    sequence = fields.Integer('Sequence', help="Determine the display order",
                              index=True)

    @api.depends('product_qty', 'unit_price')
    def _compute_total_amount(self):
        """ Calculate subtotal amount of product line """
        for rec in self:
            if rec.product_id:
                rec.total_amount = rec.unit_price * rec.product_qty
                if rec.discount != 0:
                    rec.total_amount -= rec.total_amount * (rec.discount / 100)


class SaaSPlan(models.Model):
    _inherit = 'subscription.package.plan'

    number_of_users = fields.Integer()
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', store=True)
    content_ids=fields.One2many('subscription.plan.product.line', 'plan_id','Plan Content')
