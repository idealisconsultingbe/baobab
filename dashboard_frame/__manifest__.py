{
    'name': "Dashboard Frame",
    'summary': """
        Dashboards for Smart Analytics
    """,
    'description': """
        This module allows the seamless integration of external dashboards in Odoo
    """,
    'author': "Idealis Solutions",
    'website': "https://www.idealisconsulting.com/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'mail'],
    # always loaded
    'data': [
        #security
        'security/dashboard_smart_analytics_group.xml',
        'security/ir.model.access.csv',
        #views
        'views/board_views.xml',
        # data
        'data/config_parameter.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
