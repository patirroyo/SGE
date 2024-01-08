from odoo import api, models, fields

class Bicicleta(models.Model):
    _name = 'u3a2.bicicleta'
    _rec_name = 'nombre'
    codigo = fields.Integer()
    nombre = fields.Char()
    vendida = fields.Boolean()
    talla = fields.Selection(selection=[('50', 'XS'), ('52', 'S'), ('54', 'M'), ('56', 'L'), ('58', 'XL')], required=True, string='Talla')
    tipo = fields.Selection(selection=[('0', 'Montaña'), ('1', 'Carretera'), ('2', 'Gravel'), ('3', 'Enduro'), ('4', 'Descenso')], required=True, string='Tipo')
    marca = fields.Many2one(comodel_name='u3a2.marca')
    precio = fields.Float()
    fecha_venta = fields.Date()

class Marca(models.Model):
    _name = 'u3a2.marca'
    _rec_name = 'nombre'
    codigo = fields.Integer()
    nombre = fields.Char()
    ano_creacion = fields.Date(string='Año de creación')
    descripcion = fields.Char()
    bicicleta = fields.One2many(comodel_name='u3a2.bicicleta', inverse_name='marca')







