# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################
from osv import osv
from osv import fields


class OeMedicalEthnicity(osv.osv):
    _name = 'oemedical.ethnicity'

    _columns = {
        'notes': fields.char(size=256, string='Notes', required=True),
        'code': fields.char(size=256, string='Code', required=True),
        'name': fields.char(size=256, string='Name', required=True),
    }

OeMedicalEthnicity()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
