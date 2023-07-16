# -*- coding: utf-8 -*-
{
    'name': "hr_work_place",

    'summary': """
        It let you to add work place related to work location in HR app""",

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://karvazendegi.com/odoo",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': True,
    'version': '0.1.6',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/hr_employee_views.xml',

    ],
    'assets': {
    },
    'license': 'LGPL-3',

}
