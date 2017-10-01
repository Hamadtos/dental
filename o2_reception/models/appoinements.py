from odoo import models, fields , api

class appoinements(models.Model):
	 

	_name = "o2clinic.appoinements"
    
	patient_id = fields.Many2one('o2clinic.patients', string="Patient name" , required=True)
	open_reservation_id = fields.Many2one('o2clinic.open.reservations', string="open reservations")
	state = fields.Selection(selection=[('draft', 'draft'),('confirmed', 'confirmed'),('done', 'done')] , default='draft')
	sort = fields.Integer()
	comment = fields.Text()
	patient_name = fields.Char()
	patient_phone = fields.Integer()
	patient_gender = fields.Selection(selection=[('male', 'Male'),('female', 'Female')])
	notification = fields.Boolean(default=False)
	appointment_time = fields.Datetime()
	active = fields.Boolean(default=True)
	waiting_time = fields.Integer()
	doctor_id = fields.Many2one('o2clinic.doctors', string="Doctor name")

	@api.multi
	def action_draft(self):
		self.state = 'draft'
		return True
	@api.multi
	def action_confirm(self):
		self.state = 'confirmed'
		return True
	@api.multi
	def action_done(self):
		self.state = 'done'
		return True


class teeths(models.Model):
	
    _name = "o2clinic.teeths"
    

    name = fields.Char()
    code = fields.Char()
    image = fields.Binary()













