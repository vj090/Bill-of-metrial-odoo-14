from odoo import models, fields, api

class BomField(models.Model):
    _inherit = 'product.template'

    bom_cost_price = fields.Monetary(string="Total Bom Cost added", compute="bom_count_total",store=True)

    # this will give the total compute amount all mrp bom
    @api.depends('bom_ids')
    def bom_count_total(self):
        z = self.env['mrp.bom'].search([('product_tmpl_id', '=', self.id)])
        a = 0
        for each in z:
            # print("each bom overall cost....",each.bom_calculate_total)
            a += each.bom_calculate_total
        self.bom_cost_price = a

        print("All from mrp bom", z)
        print("Current product id", self.id)



