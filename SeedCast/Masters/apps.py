from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MastersConfig(AppConfig):
    name = 'states'
    verbose_name = _('States')


#from django.apps import AppConfig


#class MenuConfig(AppConfig):
 #   name = 'menu'
 #   verbose_name = _('Menu')
