# -*- coding: utf-8 -*-
#from odoo import models, api, fields
import logging

from openerp import api, fields, models, _ 
from openerp.exceptions import UserError, ValidationError
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF


# Este lo usamos para realizar las pruebas
_logger = logging.getLogger(__name__)

class saleOrder(models.Model):
	_name = 'sale.order'
	_inherit = 'sale.order'

	#campo = fields.Char(string='nuevo_campo')
	campo = fields.Char(
		string='campo',
		compute='_compute_campo')

	@api.depends('company_id')
	def _compute_campo(self):
		self.campo = self.company_id
