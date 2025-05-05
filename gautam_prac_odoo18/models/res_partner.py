# -*- coding: utf-8 -*-

from odoo import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('name', 'ref')
    def _compute_display_name(self):
        for record in self:
            ref = record.ref or ''
            record.display_name = f"{record.name} [{ref}]" if ref else record.name
