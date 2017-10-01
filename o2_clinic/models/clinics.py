from odoo import models, fields

class clinics(models.Model):

   _name = "o2clinic.clinics"
   name = fields.Char(string="clinic name", required=True)
  