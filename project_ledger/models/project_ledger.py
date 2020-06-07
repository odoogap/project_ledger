# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountAnalyticLine(models.Model):
    _name = 'project.ledger.line'
    _description = 'Ledger Line'
    _order = 'date desc, id desc'

    @api.model
    def _default_user(self):
        return self.env.context.get('user_id', self.env.user.id)

    code = fields.Char(size=8)
    ref = fields.Char(string='Ref.')
    name = fields.Char('Description', required=True)
    date = fields.Date('Date', required=True, index=True, default=fields.Date.context_today)
    amount = fields.Monetary('Amount', required=True, default=0.0)
    product_id = fields.Many2one('product.product', string='Product', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    unit_amount = fields.Float('Quantity', default=0.0)
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_uom_id.category_id', readonly=True)
    project_id = fields.Many2one('project.project', 'Project', required=True, ondelete='restrict', index=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    partner_id = fields.Many2one('res.partner', string='Partner', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    user_id = fields.Many2one('res.users', string='User', default=_default_user)
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one(related="company_id.currency_id", string="Currency", readonly=True, store=True, compute_sudo=True)
