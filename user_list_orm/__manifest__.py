# -*- coding: utf-8 -*-
{
    'name': "user_list_orm",
    'summary': "ORM hook practice module",
    'description': """
        Made normal user fetching adding editing an deleting using owl hooks
    """,
    'author': "Aman Manandhar",
    'category': 'website',
    'version': '18.0.1.0.0',
    'depends': ['web,website'],
    'assets': {
        'web.assets_frontend': [
            'user_list_orm/static/src/js/user.js',
            'user_list_orm/static/src/xml/user.xml',
            'user_list_orm/static/src/css/user.css',
        ],
    },
    'data': [
        'views/list_view.xml',
    ],
    'installable': True,
    'application': True,
}

