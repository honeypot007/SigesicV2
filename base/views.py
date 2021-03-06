"""
Sistema Integral de Gestión para la Industria y el Comercio (SIGESIC)

Copyleft (@) 2016 CENDITEL nodo Mérida - https://sigesic.cenditel.gob.ve/trac/wiki
"""
## @namespace base.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas del módulo base
# @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from unidad_economica.directorio.forms import DirectorioForm

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"


@login_required
def inicio(request):
    """!
    Función que permite cargar la pantalla de inicio del sistema

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 01-06-2016
    @param request <b>{object}</b> Objeto que obtiene la petición
    @return Devuelve el response con la página de inicio del sistema
    """
    return render_to_response('base.template.html', {}, context_instance=RequestContext(request))


@login_required
def contacto(request):
    """!
    Función que permite cargar los datos de los tipos comunales en una tupla

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 01-06-2016
    @param request <b>{object}</b> Objeto que obtiene la petición
    @return Devuelve el response con la página de información de contacto
    """
    return render_to_response('base.contacto.template.html', {}, context_instance=RequestContext(request))