from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _get_computed_reference(self):
        result = super(AccountInvoice,self)._get_computed_reference()
        if self.company_id.invoice_reference_type == False:
            return ''
        else:
            return result
