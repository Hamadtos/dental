# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'O2 Lap',
  
    'version': '1.0.2',
    'category': 'healthcare',
     'author': 'Oxygenict',
    'description': """
O2 Lap
==================================================
    O2 Lap is an exclusive mini ERP system which helps in the systematic management of a Hospital.
    System also helps in administering branches of hospitals having one integrated database. It Covers the complete work flow of a General Practitioner and Specialist Clinics.
    With this great tool, clinics can drastically reduce the administration and management hassle and dedicate their time to providing quality healthcare services.
    O2 Lap is a securely hosted web application for patient care information Management.
    It integrates acute and community care information into a single view of the patient, enabling health and service providers to optimize the quality of care for their patient at the time and Point of care.
    """,
    'summary': 'Appoinement  , Reception , EMR , Billing  ',
    'website': 'https://www.oxygenict.com/apps/O2_Clinic',
    # 'depends': ['hr'],
    'data': ['views/view.xml','views/menuitem.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'version' : '0.1',
    'sequence': 1,  
}
