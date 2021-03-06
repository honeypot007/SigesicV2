"""
Sistema Integral de Gestión para la Industria y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/wiki
"""
## @namespace base.templatetags.base_filters
#
# Contiene filtros a utilizar en los templates
# @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import logging

from django.utils.safestring import mark_safe

logger = logging.getLogger("base")

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"

from django import template
register = template.Library()


@register.simple_tag
def menu_left_filter(user, url_path):
    """!
    Función que permite cargar las opciones del menú disponibles para el usuario autenticado

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-06-2016
    @param user <b>{string}</b> Cadena de texto que contiene el usuario autenticado
    @param url_path <b>{string}</b> Cadena de texto que contiene la url actual del sistema
    @return Devuelve una cadena de texto con las opciones del menú a mostrar
    """
    from unidad_economica.models import UnidadEconomica
    from unidad_economica.sub_unidad_economica.models import SubUnidadEconomica

    ## Contiene las opciones del menú lateral correspondiente al registro de datos
    menu_left = ''

    ## Contiene la opción a agregar al menú lateral
    opcion = '<li class="treeview">' \
             '   <a href="%s">' \
             '       <i class="label label-warning number-item-menu">%s</i><span>%s</span>' \
             '   </a>' \
             '</li>'

    ## Usuario que se encuentra actualmente autenticado en el sistema
    usuario = User.objects.get(username=user)

    # Si existen datos registrados en la opción de Información General, se habilitan las opciones asociadas a la
    # Unidad Economica
    if UnidadEconomica.objects.filter(user=usuario):

        ## Unidad Economica registrada por el usuario
        ue = UnidadEconomica.objects.get(user=usuario)

        # Opción para el registro de información mercantil
        menu_left += opcion % (reverse('informacion_mercantil'), _("2"), _("Información Mercantil"))

        #Opción para el registro de Sub Unidad Economica
        menu_left += opcion % (reverse('sub_unidad_create'), _("3"), _("Sub Unidad Económica"))

        # Si existe al menos una sub unidad económica del tipo planta registrada
        if SubUnidadEconomica.objects.filter(unidad_economica=ue, tipo_sub_unidad='Pl'):
            menu_left += opcion % (reverse('maquinaria_equipos'), _("4"), _("Maquinaria y Equipos"))

    return mark_safe(menu_left)
