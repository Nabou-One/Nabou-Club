from django.shortcuts import render

def hello_club(request):
    return render(request, 'club/hello.html')
