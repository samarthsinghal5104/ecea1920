from django.shortcuts import render

def home(request):
	return render(request,'home.html',{'title':'Home'})

def phard(request):
	return render(request,'phard.html',{'title':'Placement_Hardware'})

def ihard(request):
	return render(request,'ihard.html',{'title':'Internship_Hardware'})

def psoft(request):
	return render(request,'psoft.html',{'title':'Placement_Software'})

def isoft(request):
	return render(request,'isoft.html',{'title':'Internship_Software'})

def calender(request):
	return render(request,'calender.html',{'title':'Calender'})

def component(request):
	return render(request,'components.html',{'title':'Components'})

def academics(request):
	return render(request,'academics.html',{'title':'Academics'})

def preparation(request):
	return render(request,'preparation.html',{'title':'Preparations'})

def event(request):
	return render(request,'events.html',{'title':'Events'})

def gallery(request):
	return render(request,'gallery.html',{'title':'Gallery'})

def alumni(request):
	return render(request,'alumni.html',{'title':'Alumni'})

def project(request):
	return render(request,'projects.html',{'title':'Projects'})

def team(request):
	return render(request,'team.html',{'title':'Team'})

