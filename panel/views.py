from django.shortcuts import render

# Create your views here.
def bookTicketPanel(request):
    return render(request, 'panel/UI.html')
