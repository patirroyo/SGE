# -*- coding: utf-8 -*-
from odoo import models,fields

class Empresa(models.Model):
    _name = 'basemodulo.empresa'
    nombreEmpresa = fields.Char(string="nombre empresa")

class Entidad(models.Model):
    _name = 'basemodulo.entidad'
    nombreEntidad = fields.Char(string="nombre persona")

