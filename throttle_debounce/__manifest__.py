# -*- coding: utf-8 -*-
{
    'name': "throttle_debounce",
    'summary': "Module to see difference between throttle and debounce",
    'description': """
        Module to see difference between throttle and debounce using the fakeAPI call
    """,
    'author': "Aman Manandhar",
    'category': 'Website',
    'version': '18.0.1.0.0',
    'depends': ['website'],
    'assets': {
        'web.assets_frontend': [
            'throttle_debounce/static/src/js/throttle_debounce_demo.js',
            'throttle_debounce/static/src/xml/throttle_debounce_demo.xml',
            'throttle_debounce/static/src/scss/throttle_debounce.scss',
        ],
    },
    'data': [
        'views/throttle_debounce_views.xml',
    ],
    'installable': True,
}

