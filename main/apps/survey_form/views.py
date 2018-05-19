from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request,"index.html")

def process(request):
	if request.method == "POST":
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comments'] = request.POST['comments']

	return redirect(success)

def success(request):
	return render(request, "success.html")
