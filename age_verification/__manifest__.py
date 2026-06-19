# -*- coding: utf-8 -*-
{
    'name': "age_verification",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['website'],
    'assets': {
        'web.assets_frontend': [
            'age_verification/static/src/js/verification.js',
            'age_verification/static/src/css/verification.css',
            'age_verification/static/src/xml/verification.xml',
        ],
    },
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
}

