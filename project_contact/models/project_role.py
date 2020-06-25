# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProjectRole(models.Model):
    _name = 'project.role'
    _description = 'Ledger Tag'

    name = fields.Char('Role', required=True)
    project_id = fields.Many2one('project.project', 'Project', help="In case this type is specific")
    partner_id = fields.Many2one('res.partner', string='Partner', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")


class ResPartner(models.Model):
    _inherit = 'res.partner'

    role_ids = fields.One2many('project.role', 'partner_id', 'Roles')


class ProjectProject(models.Model):
    _inherit = 'project.project'

    role_ids = fields.One2many('project.role', 'project_id', 'Roles')