from django.shortcuts import render
# from django.http import HttpResponse
from listings.models import Listing

# Create your views here.
def index(request):
    # print(request, request.path)
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request,'pages/index.html', context)

def about(request):
    print(request, request.path)
    return render(request, 'pages/about.html')
