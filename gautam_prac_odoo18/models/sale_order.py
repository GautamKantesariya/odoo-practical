# -*- coding: utf-8 -*-

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self.with_context(so_tag_ids=self.tag_ids.ids, is_created_from_so=True)).action_confirm()
        return res

    def action_view_delivery(self):
        action = super(SaleOrder, self).action_view_delivery()
        if action:
            action.setdefault('context', {})
            action['context']['open_from_so'] = True
        return action

