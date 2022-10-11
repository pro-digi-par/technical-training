from odoo import models, fields

class TestModel(models.Model):
    _name = "estate_property"
    _description = "My Estate property description"
    
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=fields.Date.add(fields.Date.today(), months=3))
    expected_price= fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Used to choose your orientation")
    
    Active=fields.Boolean(default=False)
    State=fields.Selection(string='State',
                          selection=[('new','New'),('Offer_Received','Offer_Received'),('Offer_Accepted','Offer_Accepted'),('sold','Sold'),('canceled','canceled')],
                           required=True,
                           copy=False,
                           default='new')
    property_type_it = fields.Many2One("estate_property_type", string="Property Type")
    

class EstatePropertyTypeModel(models.Model):
    _name = "estate_property_type"
    _description = "Demo property type"
    name = fields.Chart(required = True)
 
