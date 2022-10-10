from odoo import models, fields

class EstatePropertyModel(models.Model):
    _name = "estate.property.model"
    _description = "(whatever)"
    
    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Availability Date')
    expected_price = fields.Float('Expected Price')   
    selling_price = fields.Float('Selling Price')     
    bedrooms = fields.Integer('# of bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')           
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')