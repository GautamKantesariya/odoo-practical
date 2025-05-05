# -*- coding: utf-8 -*-
{
    'name': 'gautam_prac_odoo18',

    'summary': 'Gautam Odoo 18 Practical',

    'description': """
Gautam Kantesariya Odoo Practical
    """,

    'author': 'Gautam Kantesariya',
    'website': 'https://github.com/GautamKantesariya',
    'category': 'Uncategorized',
    'version': '18.0.0.0.1',
    'depends':['base', 'base_automation', 'contacts', 'mrp', 'purchase', 'sale_management', 'stock'],
    'assets': {
            'web.assets_backend': [
                'gautam_prac_odoo18/static/src/widget/**/*',
            ],
        },
    'data': [
        'data/base_automation_data.xml',
        'data/mail_template_data.xml',
        'views/mrp_production.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}

