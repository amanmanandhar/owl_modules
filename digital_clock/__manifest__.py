# -*- coding: utf-8 -*-
{
    'name': "digital_clock",
    'summary': "To show digital clock using owl js",
    'description': """ 
      Long description of module's purpose
    """,
    'author': "Aman Manandhar",
    'category': 'website',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'assets':{
        'web.assets_frontend':[
            'digital_clock/static/src/js/clock.js',
            'digital_clock/static/src/js/mount.js',
            'digital_clock/static/src/xml/clock.xml',
        ]
    },
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/clock_page.xml',
    ],
    'installable': True,
    'application': True,
}

