from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm
def home(request):
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		print instance.email
		print instance.full_name

	context = {
		"title": request.user,
		"form" : form,
	}
	
	if request.method == "POST":
		print request.POST
	return render(request,"base.html",context)
