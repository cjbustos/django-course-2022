from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sqlite3

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
            <h1>Without html template</h1>
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
    print(data)
    conn.close()
    return render(request, template_name, data)

def get_therapist_data(request, therapist_id, template_name='entity/therapist.html'):
    conn = sqlite3.connect('providers.sqlite')
    therapist = conn.cursor()
    therapist.execute('SELECT id, name, profile, experience, address FROM therapists WHERE id=?', [therapist_id])
    therapist = therapist.fetchone()
    # fetchone() return a tuple, use index for show data in html template
    data = {"therapist":therapist}    
    return render(request, template_name, data)