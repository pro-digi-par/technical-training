from odoo import models, api, fields

class ModifyingUserModel(models.Model):
    _name = "res.user"
    _description = "Modification to user model for estate app"
    _inherit = "res.user"
    
    property_ids = fields.One2many("estate_property", "salesman_id")
    
