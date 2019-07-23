from django.shortcuts import render
from django.shortcuts import redirect
from .form import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .form import ImageUploadForm
from django.conf import settings
from .opencv_dface import opencv_dface

# Create your views here.


def first_view(request):
    return render(request, 'cv/first_view.html', {})


def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'cv/uimage.html', {
                'form': form, 'upload_file_url': uploaded_file_url
            })
    else:
        form = UploadImageForm()
        return render(request, 'cv/uimage.html', {
            'form': form
        })




def dface(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            opencv_dface(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'cv/dface.html', {'form': form, 'post': post})
    else:
        form = ImageUploadForm()
    return render(request, 'cv/dface.html', {'form': form})