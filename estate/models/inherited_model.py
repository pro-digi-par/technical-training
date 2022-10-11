from odoo import models, api, fields

class ModifyingUserModel(models.Model):
    _name = "estate_user_modification"
    _description = "Modification to user model for estate app"
    _inherit = "res.user"
    
    property_ids = fields.One2many("estate_property", "salesman_id")
    
