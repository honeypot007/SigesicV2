"""
Sistema Integral de Gestión para la Industria y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/wiki
"""
## @namespace base.admin
#
# Contiene las clases, atributos y métodos básicos del sistema a implementar en el panel administrativo
# @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
from __future__ import unicode_literals

from django.contrib import admin

from base.models import DatosSistema, TelefonoSistema, HorarioSistema, ImagenCarousel

import logging

logger = logging.getLogger("base")

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"


class DatosSistemaAdmin(admin.ModelAdmin):
    list_display = ("institucion",)
    list_filter = ("institucion",)
    ordering = ("institucion",)
    search_fields = ("institucion",)


admin.site.register(DatosSistema, DatosSistemaAdmin)
admin.site.register(TelefonoSistema)
admin.site.register(HorarioSistema)
admin.site.register(ImagenCarousel)