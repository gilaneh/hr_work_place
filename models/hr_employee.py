# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class hr_work_location_place(models.Model):
    _inherit = "hr.employee"
    # _rec_name = 'work_place_id'

    work_place_id = fields.Many2one('hr.work.place', string='Work Place',)

    @api.onchange('work_location_id')
    def _onchange_work_location_id(self):
        domain = {'work_place_id': [('work_location', '=', self.work_location_id.id)]}
        self.work_place_id = ""
        return {'domain': domain}

class HrWorkPlaceEmployeePublic(models.Model):
    _inherit = "hr.employee.public"
    # _rec_name = 'approvers_id'

    work_place_id = fields.Many2one('hr.work.place', string='Work Place',)