"""
Sistema Integral de Gestión para la Industria y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/wiki
"""
## @namespace base.constant
#
# Contiene constantes de uso general en la aplicación
# @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"

## Nacionalidades
NACIONALIDAD = (
    ("V", _("Venezolano")),
    ("E", _("Extranjero"))
)

## TIPOS DE PERSONALIDAD
TIPO_PERSONA = (
    ("V", _("Natural")),
    ("J", _("Jurídica")),
    ("E", _("Extranjera")),
    ("P", _("Pasaporte"))
)

## TIPOS DE PERSONALIDAD (ABREVIADO)
SHORT_TIPO_PERSONA = (
    ("V", "V"), ("J", "J"), ("E", "E"), ("P", "P")
)

## PERIODO DE VERIFICACION DE LA CADUCIDAD DE LA CONTRASEÑA EN DIAS
ACTUALIZACION_PASSWORD = 90