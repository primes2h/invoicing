from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    name = fields.Char(copy=True)
