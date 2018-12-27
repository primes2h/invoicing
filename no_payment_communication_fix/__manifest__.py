# Copyright 2018 Sergio Zanchetta (Associazione PNLUG - Gruppo Odoo)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': "No payment communication fix",
    'version': '12.0.1.0.0',
    'category': 'Uncategorized',
    'summary': 'Fix Odoo issue #29735',
    'author': 'Sergio Zanchetta',
    'website': "https://www.github.com/primes2h",
    'license': 'AGPL-3',

    'depends': ['account'],

    # always loaded
#    'data': [
#        # 'security/ir.model.access.csv',
#        'views/views.xml',
#        'views/templates.xml',
#    ],
    # only loaded in demonstration mode
#    'demo': [
#        'demo/demo.xml',
#    ],
}
