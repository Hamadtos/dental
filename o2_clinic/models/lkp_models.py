from odoo import models, fields


class open_reservations(models.Model):
	"""docstring for open_reservations"""

	_name = "o2clinic.open.reservations"
	doctor_id = fields.Many2one('o2clinic.doctors' , string="Doctor Name")
	start_time = fields.Float(string='Start Time')
	end_time =  fields.Float(string='End Time')


class employees(models.Model):

   _name = "o2clinic.employees"
   _inherit = 'hr.employee'
   _description = 'Doctor Information'







