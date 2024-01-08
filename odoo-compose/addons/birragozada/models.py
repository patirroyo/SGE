from odoo import api, models, fields

class Cerveza(models.Model):
    _name = 'birragozada.cerveza'
    _rec_name = 'nombre'
    tipo = fields.Char()
    nombre = fields.Char(required=True)
    descripcion = fields.Text()
    contenido_alcoholico = fields.Float(string='Contenido alcohólico (%)')
    precio_unidad = fields.Float()
    volumen_unidad = fields.Float(string='Volumen por unidad (ml)')
    disponible = fields.Boolean()
    lote = fields.One2many(comodel_name='birragozada.lote', inverse_name='cerveza')
    distribuidor = fields.Many2many(comodel_name='birragozada.distribuidor', string='Distribuidor(es)')
    ingrediente = fields.Many2many(comodel_name='birragozada.ingrediente', string='Ingrediente(s)')

class Lote_de_produccion(models.Model):
    _name = 'birragozada.lote'
    _rec_name = 'fecha_inicio_produccion'
    fecha_inicio_produccion = fields.Date(required=True)
    fecha_estimada_finalizacion = fields.Date()
    cantidad_producida = fields.Integer()
    estado = fields.Selection([('en_proceso', 'En proceso'), ('completo', 'Completo'), ('en_espera_de_empaquetado', 'En espera de empaquetado')], default='en_proceso')
    cerveza = fields.Many2one(comodel_name='birragozada.cerveza', string='Cerveza')

class Ingrediente(models.Model):
    _name = 'birragozada.ingrediente'
    _rec_name = 'nombre'
    nombre = fields.Char(required=True)
    tipo = fields.Selection([('malta', 'Malta'), ('lupulo', 'Lúpulo'), ('levadura', 'Levadura'), ('agua', 'Agua'), ('otro', 'Otro')])
    cantidad = fields.Float(string='Cantidad disponible(kg/l)')


class Empaquetado(models.Model):
    _name = 'birragozada.empaquetado'
    _rec_name = 'fecha_empaquetado'
    fecha_empaquetado = fields.Date(required=True)
    cantidad_empaquetada = fields.Integer()
    lote = fields.Many2one(comodel_name='birragozada.lote', string='Lote de producción')

class Distribuidor(models.Model):
    _name = 'birragozada.distribuidor'
    _rec_name = 'nombre'
    nombre = fields.Char(required=True)
    direccion = fields.Text()
    telefono = fields.Char()
    cerveza = fields.Many2many(comodel_name='birragozada.cerveza', string='Cervezas suministradas')
    