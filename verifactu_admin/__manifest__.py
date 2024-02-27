{
    'name': 'Odoo Server Subscription Manager',
    'version': '1.0',
    'description': 'Odoo Server Subscription Manager',
    'summary': 'Odoo server Subscription Manager',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'subscription_package'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/subscription_plan_views.xml',
        'views/res_config_settigns.xml'
    ],
    'auto_install': False,
    'application': False,
}