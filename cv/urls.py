from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),  # add
    url(r'^uimage/$', views.uimage, name='uimage'),
    url(r'^dface/$', views.dface, name='dface'),  # add
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
