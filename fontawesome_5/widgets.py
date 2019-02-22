from __future__ import absolute_import

from django import forms

from .app_settings import get_css_admin


class IconWidget(forms.Select):
    template_name = 'fontawesome_5/select.html'

    def __init__(self, attrs=None):
        super(IconWidget, self).__init__(attrs)

    class Media:

        js = (
            'django-fontawesome.js',
        )

        css = {
            'all': get_css_admin()
        }
