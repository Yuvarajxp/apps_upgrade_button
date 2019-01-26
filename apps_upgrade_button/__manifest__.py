{
    'name': 'App Upgrade button in kanban view',
    'version': '1.0',
    'category': 'Extra Tools',
    'sequence': 6,
    'summary': 'Upgrade installed module in Kanban view without going in form view',
    'description': '''
        If an app is installed. It shows "Upgrade" Button in kanban view.
    ''',
    'author': "Tintumon .M",
    'website': "http://www.tintumon.co.in",
    'depends': [
        'base',
        'web'
    ],
    'data': [
        'views/upgrade_button_views.xml',
    ],
    'installable': True,
}
