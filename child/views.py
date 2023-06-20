from django.shortcuts import render
from .helpers import ImageKitClient
from .models import filedata

def home(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        # print(file)
        imgkit = ImageKitClient(file)
        result = imgkit.upload
        print(result)
        filedata.objects.create(
            file = result['url']
        )

    all_files = filedata.objects.all()
    return render(request, 'main.html',{"all_files":all_files})