from django.contrib import admin

from devpro.encurtador.models import UrlRedirect


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destino', 'slug', 'criado_em', 'atualizado_em',)
