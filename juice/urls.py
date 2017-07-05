from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'juice'
urlpatterns = [
    url(r'^$', views.products, name='products'),
    url(r'^products$', views.products, name='products'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product, name='product'),
    url(r'^stores$', views.stores, name='stores'),
    url(r'^about$', views.about, name='about')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)