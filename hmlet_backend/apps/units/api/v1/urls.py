from django.urls import path
from hmlet_backend.apps.units.unit_views import UnitView

urlpatterns = [
    path(
        "",
        UnitView.as_view({"get": "get_all_units"}),
        name="units",
    ),
]
