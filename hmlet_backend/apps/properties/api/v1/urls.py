from django.urls import path
from hmlet_backend.apps.properties.property_views import PropertyView

urlpatterns = [
    path(
        "",
        PropertyView.as_view(
            {"post": "create_property", "get": "get_all_properties"}
        ),
        name="properties",
    ),
    path(
        "<int:property_id>/",
        PropertyView.as_view({"get": "get_property"}),
        name="property_detail",
    ),
]