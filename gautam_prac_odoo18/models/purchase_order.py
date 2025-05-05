# -*- coding: utf-8 -*-

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    product_category_id = fields.Many2one(
        'product.category',
        string="Product Category",
        help='store the product category during procurement generation'
    )

    def _make_po_get_domain(self, company_id, values, partner):
        domain = super(PurchaseOrder, self)._make_po_get_domain(company_id, values, partner)
        domain += (('product_category_id', '=', values.get('product_category_id', False)))
