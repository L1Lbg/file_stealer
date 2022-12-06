from django.http import HttpResponse
import os
# Create your views here.

os.chdir(os.path.dirname(__file__))
def file(request):
    if request.GET.get('file_name') not in os.listdir('./files/'):
        with open(f"./files/{request.GET.get('file_name')}", 'wb') as f:
            f.write(request.body)
    else:
        i = f"./files/repeated-{request.GET.get('file_name')}"
        while i in os.listdir('./files/'):
            i = 'repeated-' + i 
        with open(i, 'wb') as f:
            f.write(request.body)
    return HttpResponse('received')
