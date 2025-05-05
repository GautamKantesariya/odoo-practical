# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductCategory(models.Model):
    _inherit = 'product.category'

    @api.constrains('name')
    def _validate_unique_name(self):
        names = self.mapped('name')
        duplicates = self.env['product.category'].search([
            ('name', 'in', names),
            ('id', 'not in', self.ids)
        ])
        if duplicates:
            raise ValidationError(_("Each category name must be unique. Found duplicate: %s") % ', '.join(set(duplicates.mapped('name'))))
