from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.conf import settings

from rest_framework import routers

from .site import SiteAssets
from .views.uploads import serve_upload
from .views import api

from django.contrib import admin
admin.site = SiteAssets()
admin.autodiscover()

private_url = settings.PROTECTED_MEDIA_URL.strip("/")

# Api
router = routers.DefaultRouter()
router.register(r'earnings', api.EarningViewSet)
router.register(r'spendings', api.SpendingViewSet)
router.register(r'earning-types', api.EarningTypeViewSet)
router.register(r'spending-types', api.SpendingTypeViewSet)
router.register(r'students', api.StudentViewSet)
router.register(r'staffs', api.StaffViewSet)
router.register(r'invoices', api.InvoiceViewSet)

urlpatterns = patterns(
    'association.views',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index')),
        name='home'),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Uploads
    url(r'^' + private_url + '/invoices/(?P<invoice_path>.+)', serve_upload),

    # REST API
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
)
