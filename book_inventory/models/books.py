from odoo import api, fields, models


class InventoryBooks(models.Model):
    _name = "inventory.books"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Inventory Books"

    name = fields.Char(string='Name of Book', required=True)
    image = fields.Binary()
    book_price = fields.Float(string='Book Price')
    isbn_number = fields.Char(string='ISBN Number', required=True)
    avail = fields.Boolean('Book is Available?')
    book_category = fields.Selection([
        ('novel', 'Novel'),
        ('short stories', 'Short Stories'),
        ('poems', 'Poems'),
        ('crime thriller', 'Crime Thriller'),
        ('others', 'Others'),
    ], required=True)
    date_publish = fields.Date(string='Published Date')
    author_name = fields.Many2many('res.partner', string='Authors Name',
                                   required=True)
    publisher_name = fields.Many2one('res.partner', string='Publisher Name')
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda
        self: self.env.user)
    serial_number = fields.Integer(string='Serial Number', required=True)
    _sql_constraints = [('serial_number_unique', 'unique(serial_number)',
                         'Cant be duplicate value for this field!')]
    note = fields.Text(string='Description')
    invoice_ref = fields.Many2one('account.move', string='Invoice Reference',
                                  required=True)

    @api.onchange('publisher_name')
    def onchange_publisher_name(self):
        for rec in self:
            return {'domain': {
                'invoice_ref': [('partner_id', '=', rec.publisher_name.id)]}}

    # print(self)
    # inv_ref = self.env['account.move'].search([('partner_id',
    #                                            '=', self.publisher_name)])
    # print(inv_ref)
    # print(inv_ref.payment_reference)
