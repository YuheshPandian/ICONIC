from django.urls import path
from . import views

urlpatterns = [
    path("<str:theme>/<str:icon_name>", views.get_icon),
    path("", views.index_page),
    path("gallery/", views.icon_gallery_view, name="icon-gallery"),
    # path("500/", views.server_error, name="error_500"),
]
