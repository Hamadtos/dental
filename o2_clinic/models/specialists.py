from odoo import models, fields

class specialists(models.Model):

   _name = "o2clinic.specialists"
   name = fields.Char(string="specialist name", required=True)
  