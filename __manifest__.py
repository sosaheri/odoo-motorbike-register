# -*- coding: utf-8 -*-
{
    'name': "curso 1 - Motorcycle Register",
    'summary': "Manage mortorcycle registers",
    'description': """Manage mortorcycle registers""",
    'license': 'OPL-1',
    'author': "Heriberto Sosa",
    'website': "https://www.humanssoftware.site",
    'category': 'Custom Modules/HS',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/hs_motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'application': True,
}

