# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
#                                                                             #
# Part of Odoo. See LICENSE file for full copyright and licensing details.    #
#                                                                             #
#                                                                             #
#                                                                             #
# Co-Authors    Odoo LoCo                                                     #
#               Localización funcional de Odoo para Colombia                  #
#                                                                             #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

{
    'name': 'Impuestos - Colombia',
    'category': 'Localization',
    'version': '12.0',
    'author': 'Odoo LoCo, Jorels SAS',
    'license': 'AGPL-3',
    'maintainer': 'Jorels SAS',
    'website': 'https://www.jorels.com',
    'summary': 'Impuestos de Colombia: Modulo de Facturacion - Odoo 12.0',
    'images': ['images/'],
    'description': """
Impuestos Colombia:
======================
    * Este módulo calcula algunos impuestos colombianos que deben aplicarse.
    * Primer impuesto: retención de impuestos, que se calcula en un 2,4% del monto no tributado y se calcula con el monto total
    """,
    'depends': [
        'account',
        'l10n_co'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/l10n_co_tax_extension.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
