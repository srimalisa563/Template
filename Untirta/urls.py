from django.contrib import admin
from django.urls import path
from faperta.views import index
from feb.views import index
from fh.views import index
from fisip.views import index
from fk.views import index
from fkip.views import index
from ft.views import index
from pascasarjana.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', index ),
    path('feb/', index ),
    path('fh/', index ),
    path('fisip/', index ),
    path('fk/', index ),
    path('fkip/', index ),
    path('ft/', index ),
    path('pascasarjana/', index ),
]
