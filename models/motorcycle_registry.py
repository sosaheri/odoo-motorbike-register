from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _name = "hs_motorcicle_registry.motorcycle_registry"
    _description = "Course Motorcicle Registry"
    _rec_name = "registry_number"
    
    certificate_title = fields.Binary(string='Certificate Title', attachment=True, help='Certificate')
    current_mileage = fields.Float(string='Current Mileage')
    date_registry  = fields.Date(string='Fecha de Nacimiento')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    license_plate = fields.Char(string='License Plate')
    registry_number = fields.Char(string='Register Number', required=True)
    vin = fields.Char(string='Vin', required=True)