from django.shortcuts import render
from .models import kwdata

# Create your views here.

def kw_list(request):
	kwrecs = kwdata.objects.all()
	return render(request, 'CracowDB/kw_list.html', {'kwrecs':kwrecs})
