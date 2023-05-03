from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.POST:
        data = request.POST
        a = data['text']
        b = f'<h1>{a}</h1>'
        return JsonResponse(b, safe=False)

    return render(request, 'index.html', {'title': 'Text'})

def email(request):
    if request.POST:
        data = request.POST
        a = data['text']
        b = f'<h1>{a}</h1>'
        return JsonResponse(b, safe=False)
        
    return render(request, 'email.html', {'title': 'Email'})

def number(request):
    if request.POST:
        data = request.POST
        a = data['text']
        b = f'<h1>{a}</h1>'
        return JsonResponse(b, safe=False)
        
    return render(request, 'number.html', {'title': 'Number'})
