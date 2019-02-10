from django.shortcuts import render

# Create your views here.
def page(request):
	context = {
	'msg': "Hello World!"
	# 'test': list(range(10))
	}

	return render(request, 'page1.html', context)