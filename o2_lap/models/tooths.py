from odoo import models, fields

class tooths(models.Model):

   _name = "o2clinic.tooths"
   name = fields.Char(string="tooth name", required=True)
   image = fields.Binary()
  