from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def delivery(request):
    return render(request, 'pages/delivery.html')

def faq(request):
    return render(request, 'pages/faq.html')

def contact(request):
    return render(request, 'pages/contact.html')



