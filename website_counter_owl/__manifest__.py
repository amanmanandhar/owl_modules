# -*- coding: utf-8 -*-
{
    'name': "website_counter_owl",
    'summary': "Website counter made from owl",
    'description': """
      Handled the counter from owl to show website 
    """,
    'author': "Aman Manandhar",
    'category': 'website',
    'version': '18.0.1.0.0',
    'depends': ['website'],
    'assets': {
        'web.assets_frontend': [
            'website_counter_owl/static/src/portal_component/js/component.js',
            'website_counter_owl/static/src/xml/component.xml',
        ],
    },
    'data': [
        'views/website_view.xml',
    ],
    'installable': True,
    'application': True,
}

