# -*- coding: utf-8 -*-
{
    'name': "bom_cost_price",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/get_product_data.xml',
        'views/add_bom_field.xml',
        'views/add_bom_cost_tree_View.xml',
        'views/mrp_bom_line_extend_view.xml',


    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
