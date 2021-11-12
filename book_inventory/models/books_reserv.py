from odoo import api, fields, models


class ReservationBooks(models.Model):
    _name = "reservation.books"

    _description = "Books Reservation"

    _rec_name = "name_seq1"

    name_reservation = fields.Char(string='Name of Reservation', required=True)
    customer = fields.Many2one('res.partner', string="Customer")
    product_lines = fields.One2many('product.reservation.lines',
                                    'customer_id', string='Add Product')

    expiry_date = fields.Date(string="Expiry Date")
    note = fields.Text(string='Description')
    name_seq1 = fields.Char('Order Reference', required=True, index=True,
                           copy=False, default='New')
    field_related = fields.Many2one('res.users', string='Responsible User',
                                    default=lambda self: self.env.user)

    @api.model
    def create(self, vals):
        vals['name_seq1'] = self.env['ir.sequence'].next_by_code(
            'reservation.books')
        return super(ReservationBooks, self).create(vals)
