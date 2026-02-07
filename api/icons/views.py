from django.http import FileResponse, Http404, HttpResponse
import os
from django.conf import settings
from django.shortcuts import render

ICON_PATH = os.path.abspath(os.path.join(settings.BASE_DIR, "..", "icons"))


def get_icon(request, theme, icon_name):
    if theme not in ["dark", "light"]:
        raise Http404(f"Invalid theme: {theme}")

    file_path = os.path.join(ICON_PATH, theme, f"{icon_name}.svg")

    if not os.path.exists(file_path):
        raise Http404("Icon not found")

    return FileResponse(open(file_path, "rb"), content_type="image/svg+xml")


# def server_error(request):
#     if settings.DEBUG:
#         raise TypeError("Error 500")
#     else:
#         return None


def index_page(request):
    return render(request, "index.html")


def icon_gallery_view(request):
    base_path = os.path.join(settings.BASE_DIR, "..", "icons")

    query = request.GET.get("query", "").lower().strip()

    def load_icons(theme):
        folder = os.path.join(base_path, theme)
        if not os.path.exists(folder):
            return []

        icons = sorted([f for f in os.listdir(folder) if f.endswith(".svg")])
        if query:
            icons = [
                icon for icon in icons if query in icon.removesuffix(".svg").lower()
            ]

        return icons

    dark_icons = load_icons("dark")
    light_icons = load_icons("light")

    return render(
        request,
        "icon_gallery.html",
        {
            "dark_icons": dark_icons,
            "light_icons": light_icons,
        },
    )
