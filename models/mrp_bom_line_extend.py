from odoo import models, fields, api

class BomLinePriceExt(models.Model):
    _inherit = "mrp.bom.line"

    bom_line_cost = fields.Float(string="Total Cost")
    each_bom_line_cost = fields.Float(related="product_id.lst_price",string="Cost", store=True)
    total_amount = fields.Float(string="Total Amount",compute='total_amo',store=True)


    # This is the function which calculate (product cost x product qty)
    @api.depends('each_bom_line_cost','product_qty')
    def total_amo(self):
        for each in self:
            each.total_amount = each.product_qty * each.each_bom_line_cost


