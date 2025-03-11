from odoo import models,fields

class HmsDoctor(models.Model):
    _name = "hms.doctor"
    _description = "Doctor Information"

    FirstName = fields.Char()
    LastName = fields.Char()
    image = fields.Binary()

