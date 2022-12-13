from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import sqlite3
# Use dot, I'm into the library, example ".forms"
from .forms import TherapistForm
from .models import Person

# Create your views here.

""" def greeting(request):
    return HttpResponse('Hello, this message is from server...') """

def greeting(request, template_name='entity/greeting.html'):
    data = {"name":"Carlos","degree": {"university":"UP", "area":"psychology"}, "years_to_graduate":7, "courses":["ABA", "TCC", "AT"]}
    # render() -> This function allows join different views to templates with request 
    return render(request, template_name, data)

def about(request):
    return HttpResponse('First class of Django...')

def get_all_therapists(request):
    conn = sqlite3.connect('providers.sqlite')
    therapist = conn.cursor()
    therapist.execute('SELECT name, profile, experience, address FROM therapists')
    html = """
            <html>
            <title> Therapists list </title>
            <h1>Note: without html template</h1>
            <table style="border: 1px solid">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Profile</th>
                        <th>Experience</th>
                        <th>Address</th>
                    </tr>
                </thead>
    """
    for (name, profile, experience, address) in therapist.fetchall():
        html += "<tr><td>" + name + "</td><td>" + profile + "</td><td>" + str(experience) + "</td><td>" + address + "</td><tr>"
    html += "</table></html>"
    conn.close()
    return HttpResponse(html)

def get_all_therapistsJSON(request):
    conn = sqlite3.connect('providers.sqlite')
    therapists = conn.cursor()
    therapists.execute('SELECT name, profile, experience, address FROM therapists')
    response = JsonResponse(therapists.fetchall(), safe=False)
    conn.close
    return response

def get_courses(request, template_name='entity/courses.html'):
    conn = sqlite3.connect('providers.sqlite')
    courses = conn.cursor()
    courses.execute('SELECT title, dept_name, entity, credits FROM courses')
    list_of_courses = courses.fetchall()
    data = {"courses": list_of_courses}
    conn.close()
    return render(request, template_name, data)

def get_courses_by_therapist_id(request, therapist_id, template_name='entity/courses.html'):
    conn = sqlite3.connect('providers.sqlite')
    therapist_courses = conn.cursor()
    therapist_courses.execute('SELECT title, dept_name, entity, credits FROM courses WHERE therapist_id=?', [therapist_id])
    list_of_courses = therapist_courses.fetchall()
    data = {"courses": list_of_courses}
    conn.close()
    return render(request, template_name, data)

def get_therapist_data(request, therapist_id, template_name='entity/therapist.html'):
    conn = sqlite3.connect('providers.sqlite')
    therapist = conn.cursor()
    therapist.execute('SELECT id, name, profile, experience, address FROM therapists WHERE id=?', [therapist_id])
    therapist = therapist.fetchone()
    # fetchone() return a tuple, have to use index for show data in html template
    data = {"therapist": therapist}    
    return render(request, template_name, data)

# Call function twice, first to show and second to send values
def add_therapist(request, template_name='entity/therapist_form.html'):
    # Cycle ->
    # First: to the view with blank fields
    # Second: to the view with data loaded and method="POST" setting
    if request.method == "POST":
        # Note: add "request.POST" in parent constructor
        # Note: cleaned_data method has all data from the form
        form = TherapistForm(request.POST)
        if form.is_valid():
            conn = sqlite3.connect('providers.sqlite')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO therapists VALUES (?, ?, ?, ?, ?)",
            (form.cleaned_data["id"],
            form.cleaned_data["name"],
            form.cleaned_data["profile"],
            form.cleaned_data["experience"],
            form.cleaned_data["address"]))
            conn.commit()
            conn.close()
            # Note: redirect method forward use the name attribute in path in urls.py
            return redirect('therapists')
    else:
        t_form = TherapistForm()
    data = {"t_form": t_form}
    return render(request, template_name, data)

def get_all_persons(request, template_name='entity/persons.html'):
    persons_list = Person.objects.all()
    data = {"persons": persons_list}
    return render(request, template_name, data)

# Get record from table Person
def get_person_by_phone(request, phone, template_name='entity/person.html'):
    # use the specific field for search in db, example: "phone_number"
    person_by_phone = Person.objects.get(phone_number=phone)
    data = {"person": person_by_phone}
    return render(request, template_name, data)
