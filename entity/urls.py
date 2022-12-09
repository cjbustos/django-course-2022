from django.urls import path
from . import views

urlpatterns = [
    path("", views.greeting, name='greeting' ),
    path("about", views.about, name='about'),
    path("therapists", views.get_all_therapists, name='therapists'),
    path("therapists-json", views.get_all_therapistsJSON, name='therapists-json'),
    path("therapist/<int:therapist_id>", views.get_therapist_data, name='therapist'),
    path("courses", views.get_courses, name='courses'),
    path("courses/<int:therapist_id>", views.get_courses_by_therapist_id, name='therapist-courses'),
    path("add_therapist", views.add_therapist, name='add-therapist'),
]

""" For example, name='greeting' - this prop handle internal control to serve """