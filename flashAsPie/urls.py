from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import include, path
from django.contrib import admin
from django.views.generic import RedirectView
from enviro import settings

from .views import employee, home, order

urlpatterns = [
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('staff/', employee, name='staff'),
    #path('admin/', admin.site.urls, name='admin'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
