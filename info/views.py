from django.shortcuts import render

# Create your views here.
def index(request):
    img = Photo.objects.all().order_by('-id')
    return render_to_response("team.html", {"img": img})