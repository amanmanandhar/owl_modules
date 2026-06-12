# -*- coding: utf-8 -*-
{
    'name': "Mini CRM",
    'summary': "Saving form after user releases writing",
    'description': """
        Auto save form after stopping writing for certain time and hit crm and creates the details
    """,
    'author': "Aman Manandhar",
    'category': 'website',
    'version': '18.0.1.0.0',
    'depends': ['web','website'],
    'assets': {
        'web.assets_frontend': [
            'autosave_form_minicrm/static/src/js/auto_save.js',
            'autosave_form_minicrm/static/src/xml/auto_save.xml',
            'autosave_form_minicrm/static/src/css/auto_save.css',
        ],
    },
    'data': [
        'views/form_view.xml',
    ],
    'installable': True,
}

