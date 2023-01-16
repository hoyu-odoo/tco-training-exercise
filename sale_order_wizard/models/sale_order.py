from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"


    def action_set_quantity(self):
        return {
            'name': _('Set Sales Order Quantity'),
            'view_mode': 'form',
            'res_model': 'sale.order.quantity',
            'view_id': self.env.ref('sale_order_wizard.sale_order_quantity_view_form').id,
            'type': 'ir.actions.act_window',
            'context': {'default_order_id': self.id},
            'target': 'new'
        }
