# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tag_ids = fields.Many2many(
        'crm.tag',
        string="Tags",
        help="Tags for deliveries"
    )

    @api.model_create_multi
    def create(self, vals_list):
        so_tag_ids = self.env.context.get('so_tag_ids')
        if so_tag_ids:
            picking_type_ids = {vals.get('picking_type_id') for vals in vals_list if vals.get('picking_type_id')}
            picking_types = self.env['stock.picking.type'].sudo().browse(picking_type_ids).read(['code'])
            type_code_map = {pt['id']: pt['code'] for pt in picking_types}

            for vals in vals_list:
                picking_type_id = vals.get('picking_type_id')
                if picking_type_id and type_code_map.get(picking_type_id) == 'outgoing':
                    vals['tag_ids'] = [(6, 0, so_tag_ids)]

        return super(StockPicking, self).create(vals_list)
