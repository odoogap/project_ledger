# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountAnalyticLine(models.Model):
    _inherit = 'project.project'

    def action_open_ledger(self):
        self.ensure_one()
        ledger_id = self.env.ref('project_ledger.project_ledger_default').id
        return {
            'name': 'Ledger Lines - %s' % self.display_name,
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref('project_ledger.ledger_lines_tree').id,
            'view_mode': 'tree',
            'res_model': 'project.ledger.line',
            'context': {'default_project_id': self.id, 'default_ledger_id': ledger_id},
            'domain': [('project_id', '=', self.id), ('ledger_id', '=', ledger_id)],
        }


class ProjectLedger(models.Model):
    _name = 'project.ledger'
    _description = 'Ledger Type'

    name = fields.Char('Name', required=True)


class ProjectLedgerLine(models.Model):
    _name = 'project.ledger.line'
    _description = 'Ledger Line'
    _order = 'date desc, id desc'

    def write(self, vals):
        if not vals.get('ledger_id'):
            vals.update({'ledger_id': self._default_ledger})
        res = super(ProjectLedgerLine, self).write(vals)
        return res

    @api.model
    def _default_ledger(self):
        return self.env.context.get('ledger_id', self.env.ref('project_ledger.project_ledger_default').id)

    @api.model
    def _default_user(self):
        return self.env.context.get('user_id', self.env.user.id)

    code = fields.Char(size=8)
    ref = fields.Char(string='Ref.')
    name = fields.Char('Description', required=True)
    date = fields.Date('Date', required=True, index=True, default=fields.Date.context_today)
    amount = fields.Monetary('Amount', required=True, default=0.0)
    product_id = fields.Many2one('product.product', string='Product', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    ledger_id = fields.Many2one('project.ledger', string='Ledger Type', required=True, default=_default_ledger)
    unit_amount = fields.Float('Quantity', default=0.0)
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_uom_id.category_id', readonly=True)
    project_id = fields.Many2one('project.project', 'Project', required=True, ondelete='restrict', index=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    partner_id = fields.Many2one('res.partner', string='Partner', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    user_id = fields.Many2one('res.users', string='User', default=_default_user)
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one(related="company_id.currency_id", string="Currency", readonly=True, store=True, compute_sudo=True)
