from django.urls import path

from . import views
#

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersonas.as_view(),
        name="personas"
    ),
    path(
        'api/personas/',
        views.PersonaListApi.as_view(),
        name="personas"
    ),
    path(
        'api/personas/add/',
        views.PersonaCreateApi.as_view(),
        name="personas"
    ),
    path(
        'api/personas/get/<pk>/',
        views.PersonaGetApi.as_view(),
        name="personas"
    ),
    path(
        'api/personas/update/<pk>/',
        views.PersonaUpdateApi.as_view(),
        name="personas"
    ),
    path(
        'api/personas/getupdate/<pk>/',
        views.PersonaGetUpdateApi.as_view(),
        name="personas"
    ),
    path(
        'api/personas/delete/<pk>/',
        views.PersonaDeleteApi.as_view(),
        name="personas"
    ),
]