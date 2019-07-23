from django.shortcuts import render
from django.shortcuts import redirect
from .form import UploadImageForm
from django.core.files.storage import FileSystemStorage
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