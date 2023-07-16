# -*- coding: utf-8 -*-

from odoo import models, fields, api
import io
import base64
from PIL import Image

class hr_workplace(models.Model):
    _name = "hr.work.place"
    _description = "hr_work_place"
    _rec_name = 'work_place'

    active = fields.Boolean(default=True)
    work_place = fields.Char(string="Work Place",
                            required=True,
                            copy=True,
                            translate=True
                             )
    work_location = fields.Many2one('hr.work.location',
                            required=True,
                            copy=True,
                            )
    plan = fields.Binary()
    work_place_x = fields.Float(help='meters')
    work_place_y = fields.Float(help='meters')


    plan_x = fields.Integer()
    plan_y = fields.Integer()


    @api.onchange('plan')
    def model_image_size(self):
        for rec in self:
            try:
                if rec.plan[-2:] != '==':
                    padded_data = rec.plan + b'=='
                else:
                    padded_data = rec.plan
                image_file = base64.b64decode(padded_data)
                im = Image.open(io.BytesIO(image_file))
                rec.plan_x, rec.plan_y = im.size
                # print(f'\n IMAGE: {padded_data[-2:]}, im.size: {im.size} rec.plan_x: {rec.plan_x} type: {type(rec.plan_x)}')
            except Exception as e:
                rec.plan_x = 0
                rec.plan_y = 0
                # print(f'\n ERROR: {e}')