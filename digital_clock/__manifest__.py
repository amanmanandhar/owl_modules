# -*- coding: utf-8 -*-
{
    'name': "digital_clock",
    'summary': "To show digital clock using owl js",
    'description': """ 
      Digital Clock using proper owl and public components
    """,
    'author': "Aman Manandhar",
    'category': 'website',
    'version': '18.0.1.0.0',
    'depends': ['website'],
    'assets':{
        'web.assets_frontend':[
            'digital_clock/static/src/js/clock.js',
            'digital_clock/static/src/xml/clock.xml',
            'digital_clock/static/src/css/clock.css',
        ]
    },
    'data': [
        'views/clock_page.xml',
    ],
    'installable': True,
    'application': True,
}

