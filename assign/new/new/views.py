from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def about(request):
    data = request.GET
    math = int(data['math'])
    social = int(data['social'])
    hindi = int(data['hindi'])
    english = int(data['english'])
    science = int(data['science'])
    total = math + social + hindi + english +science 
    percentage = total/5
    return HttpResponse(f'Total : {total} and Percentage:{percentage}')

