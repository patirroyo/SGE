from odoo import models, fields, api

class ventas(models.Model):
    _name = 'ventas_cole.ventas' # nombre del modelo y crea la tabla ventas_cole.ventas
    _description = 'ventas_cole.ventas'
    name = fields.Char()
    descripcion = fields.Char()#la api de fields es para crear los campos, asi de facil
    precio = fields.Integer()
    cantidad = fields.Integer()
    total = fields.Integer()
    cliente = fields.Char()
    vendedor = fields.Many2one(comodel_name='ventas_cole.vendedores')#un vendedor puede tener muchas ventas, para ello se usa el many2one
    factura = fields.Char()
    fecha = fields.Date()
    total_con_decimales = fields.Float()

class vendedores(models.Model):
    _name = 'ventas_cole.vendedores'
    _description = 'ventas_cole.vendedores'
    _rec_name = 'nombre' # Para que se muestre el nombre en lugar del id
    nombre = fields.Char()
    apellido = fields.Char()
    dni = fields.Char()
    ventas = fields.One2many(comodel_name='ventas_cole.ventas', inverse_name='vendedor')#un vendedor puede tener muchas ventas, para ello se usa el one2many
class lugares(models.Model):
    _name = 'ventas_cole.lugares'
    _description = 'ventas_cole.lugares'
    _rec_name = 'nombre'
    nombre = fields.Char()
    direccion = fields.Char()
    telefono = fields.Char()
    ventas = fields.Many2many(comodel_name='ventas_cole.ventas', relation='ventas_lugares_rel', column1='lugar_id', column2='venta_id')#un lugar puede tener muchas ventas, 