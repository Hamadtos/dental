from odoo import models, fields

class patients(models.Model):

   _name = "o2clinic.patients"
   name = fields.Char(string="name", required=True)
   en_name = fields.Char(string="EN name")
   birth_date = fields.Date()
   image = fields.Binary()
   gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')])
   nationality_id = fields.Many2one('o2clinic.nationality', string="Patient nationality")


   Social_status = fields.Selection(selection=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed')] , string="Social status")
   passport_No = fields.Char(string="passport No")
   blood_type = fields.Char(string="blood type")
   ID_Number = fields.Char(string="ID Number")
   Religion = fields.Char(string="Religion")
   Date_of_Birth = fields.Char(string="Date of Birth")
   telephone_number = fields.Char(string="telephone number")
   address = fields.Char(string="address")
   patient_job = fields.Char(string="patient-job")
   sponsor_name = fields.Char(string="sponsor_name")
   sponsor_mobile_No = fields.Char(string="sponsor mobile  No")
