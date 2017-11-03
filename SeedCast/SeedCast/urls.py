"""Jetpractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django.views.static
from django.conf.urls import url,include
from django.contrib import admin
from SeedCast import views
import Masters.views as some
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/mobile', some.MobileViewSet)
admin.autodiscover()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    url(r'^', admin.site.urls),
    #url(r'^admin/Dealer_reg/dealer_registration/import/', include('models.Dealer_')),
    url(r'^export/xls_users/$', views.export_users_xls, name='export_users_xls'),
    url(r'^xls/$', views.export_xls, name='export_xls'),
    url(r'^registrations/', include('Masters.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^graph/$', some.BarView.as_view()),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root', settings.STATIC_ROOT}),
    url(r'^feedback/$', some.Feedback.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
