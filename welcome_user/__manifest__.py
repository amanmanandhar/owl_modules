# -*- coding: utf-8 -*-
{
    'name': 'Welcome After Login',
    'summary': 'Dialog learning, small module',
    'description': """
        A prototype to show the things or model dialog after login can make a different age verification or different dialog with same type of logic
    """,
    'author': 'Aman Manandhar',
    'category': 'Uncategorized',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'assets': {
        'web.assets_backend': [
            'welcome_user/static/src/js/welcome.js',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/welcome_wizard.xml',
    ],
    'installable': True,
}

