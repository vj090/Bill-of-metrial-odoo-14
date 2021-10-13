from odoo import models, fields, api

class BomPriceExt(models.Model):
    _name = "bom.cost"
    _inherit = "mrp.bom"

    bom_cost_test = fields.Float(string="Bom Cost")

