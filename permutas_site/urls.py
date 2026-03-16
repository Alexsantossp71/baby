"""
URL configuration for permutas_site project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='sobre'),
    path('ajuda/', TemplateView.as_view(template_name='ajuda_e_faq_desktop.html'), name='ajuda'),
    path('rastreio/', TemplateView.as_view(template_name='rastreio.html'), name='rastreio'),
    path('cadastro/', RedirectView.as_view(url='/accounts/register/', permanent=False), name='cadastro'),
    path('admin/', admin.site.urls),
    path('baby/', include('baby.urls', namespace='baby')),
    path('accounts/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)