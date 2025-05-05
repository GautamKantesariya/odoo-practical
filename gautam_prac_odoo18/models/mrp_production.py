# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    is_created_from_so = fields.Boolean(
        string="Is Created from Sale Order",
        readonly=True,
        help='Help identify whether the Manufacturing Order was created from a Sale Order.',
    )

    @api.model_create_multi
    def create(self, vals_list):
        is_created_from_so = self.env.context.get('is_created_from_so', False)
        if is_created_from_so:
            for val in vals_list:
                val['is_created_from_so'] = is_created_from_so
        return super(MrpProduction, self).create(vals_list)
