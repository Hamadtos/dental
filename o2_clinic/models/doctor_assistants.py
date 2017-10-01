from odoo import models, fields

class doctor_assistants(models.Model):

   _name = "o2clinic.doctor.assistants"
   doctor_id = fields.Many2one('o2clinic.doctors' , string="Doctor Name")
   clinic_id = fields.Many2one('o2clinic.clinics' , string="Clinic Name")
   emp_id = fields.Many2one('res.partner', string='Employee  Name')
