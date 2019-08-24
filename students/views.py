from django.shortcuts import render

def listStudents(request):
    return render(request, "students/students.html")
