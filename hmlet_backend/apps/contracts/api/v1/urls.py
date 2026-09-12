
from django.urls import path
from hmlet_backend.apps.contracts.views.contract_views import ContractView

urlpatterns = [
path(
    "",
    ContractView.as_view({"post": "create_contract", "get": "get_all_contracts"}),
),
]