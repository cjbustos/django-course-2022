from django.urls import path
from . import views
# Preguntar por el login
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.greeting, name='greeting' ),
    path("about", views.about, name='about'),
    path("therapists", views.get_all_therapists, name='therapists'),
    path("therapists-json", views.get_all_therapistsJSON, name='therapists-json'),
    path("therapist/<int:therapist_id>", views.get_therapist_data, name='therapist'),
    path("courses", views.get_courses, name='courses'),
    path("courses/<int:therapist_id>", views.get_courses_by_therapist_id, name='therapist-courses'),
    path("add_therapist", views.add_therapist, name='add-therapist'),
    path("persons", views.get_all_persons, name='persons'),
    path("person/<int:phone>", views.get_person_by_phone, name='person-by-phone'),
    path("diagnostics", views.get_all_diagnostics, name='diagnostics'),
    path("add_diagnostic", views.add_diagnostic, name='add-diagnostic'),
    path("clients", views.get_all_clients, name='clients'),
    path("add_client", views.add_client, name='add-client'),
    path("update_client/<int:pk>", views.update_client, name='update-client'),
    path("client/<str:initial>", views.get_client_by_param, name='client-by-initial'),
    path("delete_client/<int:pk>", views.delete_client, name='delete-client'),
]

""" For example, name='greeting' - this prop handle internal control to serve """