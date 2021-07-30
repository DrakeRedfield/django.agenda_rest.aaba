from django.urls import path

from . import views
#

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersonas.as_view(),
    ),
    path(
        'api/personas/',
        views.PersonaListApi.as_view(),
    ),
    path(
        'api/personas/add/',
        views.PersonaCreateApi.as_view(),
    ),
    path(
        'api/personas/get/<pk>/',
        views.PersonaGetApi.as_view(),
        name = "get_person_api1"
    ),
    path(
        'api/personas/update/<pk>/',
        views.PersonaUpdateApi.as_view(),
    ),
    path(
        'api/personas/getupdate/<pk>/',
        views.PersonaGetUpdateApi.as_view(),
    ),
    path(
        'api/personas/delete/<pk>/',
        views.PersonaDeleteApi.as_view(),
    ),
    path(
        'api/v2/personas/',
        views.PersonaListApiCustom.as_view(),
    ),
    path(
        'api/v3/personas/',
        views.PersonaListApiCustom2.as_view(),
    ),
    path(
        'api/reunion/',
        views.MeetingListApiCustom.as_view(),
    ),
    path(
        'api/reunion/job/',
        views.MeetingByPersonJobListApiCustom.as_view(),
    ),
    path(
        'api/v2/reunion/',
        views.MeetingListApiCustom2.as_view(),
    ),
]