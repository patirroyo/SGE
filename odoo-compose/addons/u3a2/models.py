from odoo import api, models, fields

class Bicicleta(models.Model):
    _name = 'u3a2.bicicleta'
    _rec_name = 'nombre'
    codigo = fields.Integer()
    nombre = fields.Char(required=True)
    talla = fields.Selection(selection=[('50', 'XS'), ('52', 'S'), ('54', 'M'), ('56', 'L'), ('58', 'XL')], required=True, string='Talla')
    tipo = fields.Selection(selection=[('0', 'Montaña'), ('1', 'Carretera'), ('2', 'Gravel'), ('3', 'Enduro'), ('4', 'Descenso')], required=True, string='Tipo')
    marca = fields.Many2one(comodel_name='u3a2.marca', string='Marca')
    precio = fields.Float()
    fecha_recepcion = fields.Date()
    fecha_venta = fields.Date()
    vendida = fields.Boolean(compute='_compute_venta', store=True)
    @api.depends('fecha_venta', 'vendida')
    def _compute_venta(self):
        for record in self:
            if record.fecha_venta:
                record.vendida = True
            else:
                record.vendida = False
    cliente = fields.Many2one(comodel_name='u3a2.cliente', string='Cliente')

class Marca(models.Model):
    _name = 'u3a2.marca'
    _rec_name = 'nombre'
    codigo = fields.Integer()
    nombre = fields.Char(required=True)
    ano_creacion = fields.Date(string='Año de creación')
    descripcion = fields.Char()
    bicicleta = fields.One2many(comodel_name='u3a2.bicicleta', inverse_name='marca')

class Tienda(models.Model):
    _inherit = 'salesianos.proveedor'
    _name = 'u3a2.tienda'
    direccion = fields.Char()

class Cliente(models.Model):
    _inherit = 'basemodulo.entidad'
    _name = 'u3a2.cliente'
    _rec_name = 'nombreEntidad'
    bicicleta = fields.One2many(comodel_name='u3a2.bicicleta', inverse_name='cliente')
    edad = fields.Integer()
    
    @api.constrains('edad', 'nombreEntidad') 
    def _check_edad(self):
        for record in self:
            if record.edad < 18:
                raise models.ValidationError('El cliente "{}" debe ser mayor de edad.'.format(record.nombreEntidad))
            elif record.edad > 100:
                raise models.ValidationError('El cliente "{}" no puede tener más de 100 años.'.format(record.nombreEntidad))
