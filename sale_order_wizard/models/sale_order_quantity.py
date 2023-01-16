from odoo import fields, models, _


class SaleOrderQuantity(models.TransientModel):
    _name = "sale.order.quantity"

    quantity = fields.Integer("Quantity")
    order_id = fields.Many2one('sale.order', string='Sale Order', required=True, ondelete='cascade')

    def action_set_quantity(self):
        if self.order_id and self.quantity:
            for line in self.order_id.order_line:
                line.update({"product_uom_qty": self.quantity})
        return
