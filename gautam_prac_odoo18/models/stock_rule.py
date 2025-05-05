# -*- coding: utf-8 -*-

from odoo import api, models


class StockRule(models.Model):
    _inherit = 'stock.rule'

    @api.model
    def _run_buy(self, procurements):
        for procurement, rule in procurements:
            procurement.values['product_category_id'] = procurement.product_id.categ_id.id
        return super(StockRule, self)._run_buy(procurements)

    def _make_po_get_domain(self, company_id, values, partner):
        domain = super(StockRule, self)._make_po_get_domain(company_id, values, partner)
        domain += (('product_category_id', '=',  values.get('product_category_id', False)),)
        return domain

    def _prepare_purchase_order(self, company_id, origins, values):
        res = super(StockRule, self)._prepare_purchase_order(company_id=company_id, origins=origins, values=values)
        values = values[0]
        res['product_category_id'] = values.get('product_category_id', False)
        return res
