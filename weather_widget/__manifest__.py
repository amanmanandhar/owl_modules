# -*- coding: utf-8 -*-
{
    'name': "weather_widget",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['web','website'],
    'assets': {
            'web.assets_frontend': [
                'weather_widget/static/src/js/weather.js',
                'weather_widget/static/src/js/mount.js',
                'weather_widget/static/src/css/weather.css',
                'weather_widget/static/src/xml/weather.xml',
            ],
        },
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/website_page.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

