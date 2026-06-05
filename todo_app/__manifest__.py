# -*- coding: utf-8 -*-
{
    'name': 'Todo App from Owl for website',
    'summary': 'Making todo for website using owl and making public component',
    'description': """
        Used useState, registry to extract as public component as use as owl-component in website views
    """,
    'author': 'Aman Manandhar',
    'category': 'website',
    'version': '18.0.1.0.0',
    'depends': ['website'],
    'assets': {
        'web.assets_frontend': [
            'todo_app/static/src/js/todo.js',
            'todo_app/static/src/css/todo.css',
            'todo_app/static/src/xml/todo.xml',
        ],
    },
    'data': [
        'views/todo_views.xml',
    ],
    'installable': True,
    'application': True,
}


