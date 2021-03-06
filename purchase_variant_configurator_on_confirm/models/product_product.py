# Copyright 2016 ACSONE SA/NV
# Copyright 2017 Tecnativa - David Vidal
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _select_seller(
        self, partner_id=False, quantity=0.0, date=None, uom_id=False, params=False
    ):
        """Don't fail on empty products for allowing to copy purchase order lines."""
        if not self:
            return False
        return super()._select_seller(
            partner_id=partner_id,
            quantity=quantity,
            date=date,
            uom_id=uom_id,
            params=params,
        )
