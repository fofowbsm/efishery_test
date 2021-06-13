# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Efishery Test',
    'version': '1.1',
    'category': 'Sales/Sales',
    'summary': 'Sales internal machinery',
    'description': """
    Goals
    1.Interceptor service bisa dinyalakan di port berbeda
    2.Static token bisa dikonfigurasi di Odoo
    3.Semua endpoint berfungsi dengan semestinya
    4.Dokumentasi endpoint Odoo dengan Module Open API
    5.Dokumentasi system diagram-nya dalam format C4 Model(Context dan Deployment)
    6.Dockerfile untuk masing-masing app
    7.Petunjuk penggunaan dan instalasi di README.md yang memudahkan
    
    Additional Goals (Nice to Have)
    1.Menggunakan mono repo (interceptor service & Odoodalam satu repo)
    2.Deployed ke Host/Penyedia Layanan (semacam surge,heroku, vercel, firebase, glitch,host anda pribadi)
    3.Docker Compose4.Unit Testing
    """,
    'depends': ['sale'],
    'data': [
        # 'security/sale_security.xml',
        # 'security/ir.model.access.csv',
        # 'report/sale_report.xml',
        # 'report/sale_report_views.xml',
        # 'report/sale_report_templates.xml',
        # 'report/invoice_report_templates.xml',
        # 'report/report_all_channels_sales_views.xml',
        # 'data/ir_sequence_data.xml',
        # 'data/mail_data.xml',
        # 'data/sale_data.xml',
        # 'wizard/sale_make_invoice_advance_views.xml',
        # 'views/sale_views.xml',
        # 'views/sales_team_views.xml',
        # 'views/res_partner_views.xml',
        # 'views/mail_activity_views.xml',
        # 'views/assets.xml',
        # 'views/variant_templates.xml',
        # 'views/sale_portal_templates.xml',
        # 'views/sale_onboarding_views.xml',
        # 'views/res_config_settings_views.xml',
        # 'views/payment_views.xml',
        # 'views/product_views.xml',
        # 'views/utm_campaign_views.xml',
        # 'wizard/sale_order_cancel_views.xml',
        # 'wizard/sale_payment_link_views.xml',
    ],
    'demo': [
        # 'data/product_product_demo.xml',
        # 'data/sale_demo.xml',
    ],
    'installable': True,
    'auto_install': False
}
