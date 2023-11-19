from odoo import api, models, fields

class Moneda(models.Model):
    _name = 'durhos.moneda'
    codigo = fields.Integer()
    es_variante = fields.Boolean()
    desc_error = fields.Char()
    molde = fields.Many2one(comodel_name='durhos.molde')

class Modelo(models.Model):
    _name = 'durhos.modelo'
    cod = fields.Integer()
    valor_facial = fields.Char()
    unidad_monetaria = fields.Char()
    diametro = fields.Float()
    peso = fields.Integer()
    descripcion = fields.Char()
    molde = fields.One2many(comodel_name='durhos.molde', inverse_name='modelo')
    metal = fields.Many2many(comodel_name='durhos.metal', relation='durhos_modelo_rel', column1='modelo', column2='metal', string='Related instances')

class ModeloRelations(models.Model):
    _name = 'durhos.modelo.rel'
    modelo = fields.Integer(string='Modelo', required=True)
    metal = fields.Integer(string='Metal', required=True)
    proporcion = fields.Integer()
    ley = fields.Integer()
    relationship = fields.Selection(string='Modelo to Metal Relationship', selection='_get_relationship', required=True)
    def _get_relationship(self):
        return [
            ('01','relationship1'),
            ('02','relationship2')]
    

class Molde(models.Model):
    _name = 'durhos.molde'
    _description = 'durhos.molde'
    codigo = fields.Integer()
    ano_acunacion = fields.Date()
    descripcion = fields.Char()
    fecha_estrellas = fields.Date()
    moneda = fields.One2many(comodel_name='durhos.moneda', inverse_name='molde')
    modelo = fields.Many2one(comodel_name='durhos.modelo')

class Metal(models.Model):
    _name = 'durhos.metal'
    _rec_name = 'nombre'
    nombre = fields.Char()
    #modelo = fields.Many2many(comodel_name='durhos.modelo', relation='modmet', column1='modelo', column2='metal' )





