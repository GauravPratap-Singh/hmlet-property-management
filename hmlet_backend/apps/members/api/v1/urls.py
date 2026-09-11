from django.urls import path
from hmlet_backend.apps.members.member_views import MemberView

urlpatterns = [
path(
  "",
  MemberView.as_view({"post": "create_member", "get": "get_all_members"}),
  name="members",
),
]