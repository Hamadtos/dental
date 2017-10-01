from odoo import models, fields


    
class nationality(models.Model):
	"""docstring for nationality"""

	_name = "o2clinic.nationality"
	name = fields.Char(string="name", required=True)

class workdays(models.Model):
	"""docstring for workdays"""

	_name = "o2clinic.workdays"
	name = fields.Char(string="name", required=True)








