from odoo import models, fields, api

class BomFieldCalculated(models.Model):
    _inherit = 'mrp.bom'

    bom_calculate = fields.Float(string="Bom Cost Tree", realated="bom_lines_ids.total_amount",store=True)
    bom_each_calc = fields.Float(string="Each cost")
    bom_calculate_total = fields.Float(string="Bom Cost added", compute="get_bom_cost", store=True)



    # Show the grand total into the From view
    @api.depends('bom_line_ids')
    def get_bom_cost(self):
        a = 0
        for rec in self.bom_line_ids:
            for r in rec:
                a += r.total_amount
            self.bom_calculate_total = a

    @api.model
    def create(self, vals):
        print("Create method in side the mrp Bom")
        print("vals in side the mrp bom ",vals)
        res = super(BomFieldCalculated, self).create(vals)
        return res


