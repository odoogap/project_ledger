# -*- coding: utf-8 -*-
{
    'name' : 'Project Ledger',
    'version' : '1.1',
    'summary': 'Third Party Ledger Management',
    'sequence': 15,
    'description': """
Third Party Ledger Management
=============================
    """,
    'category': 'Project Management',
    'website': 'https://www.odoogap.com/',
    'images' : [],
    'depends' : ['project', 'hr_timesheet', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'data/ledger_data.xml',
        'views/project_view.xml',
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
