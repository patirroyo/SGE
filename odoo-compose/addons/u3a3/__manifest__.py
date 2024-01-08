# -*- coding: utf-8 -*-
{
    'name': "u3a3",
    'summary': """Part 2""",
    'description': """
        Modulo para aprobar la tarea:
        Completa el módulo original con los siguientes aspectos:
1. Añade en una de las clases una función que calcule la media de una serie de valores enteros almacenados en los registros.
2. Cree una clase hija que herede funcionalidades y añada otras nuevas.
3. Añada un logotipo al módulo.

            
    """,
    'author': "Alberto Saz",
    'website': "http://www.dejadefusilarmeelrepositorio.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'modulo_simple-main', 'basemodulo'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
