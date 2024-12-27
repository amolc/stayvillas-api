from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa: F841


urlpatterns = [
    path('admin/', admin.site.urls),
    path("<int:org_id>/api/customer/", include("customers.urls")),
    path("<int:org_id>/api/property/", include("property.urls")),
    path("<int:org_id>/api/destination/", include('destination.urls')),
    path("<int:org_id>/api/investor/", include('investors.urls')),
    path("<int:org_id>/api/agent/", include('agent.urls')),
    path(
        "<int:org_id>/api/property_listing/",
        include('property_listing.urls')
    ),
    path("<int:org_id>/api/enquiry/", include('enquiry.urls')),
    path("<int:org_id>/api/cancellation/", include('cancellation.urls')),
    path(
        "<int:org_id>/api/property_manager/",
        include('property_manager.urls')
    ),
    path("<int:org_id>/api/booking/", include('booking.urls')),
    path("<int:org_id>/api/holidays/", include('holidays.urls')),
    path("<int:org_id>/api/event/", include('event.urls')),
    path('sentry-debug/', trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
