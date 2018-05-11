from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from django import forms
from .models import ModelWithFileField

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def index(request):
    return render(request, "fileupload_app/index.html")

def upload_file(request):
    if request.method == "POST":
        print("1st if")
        form = UploadFileForm(request.POST, request.FILES)
        print("request.POST", request.POST)
        print("request.FILES", request.FILES)
        print("form.is_valid()",form.is_valid())
        print(form.errors)
        print(form.non_field_errors)
        if form.is_valid():
            print("2nd if")
            instance  = ModelWithFileField(uploadedImage=request.FILES["file"])
            instance.save()
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
        print("else")
    return render(request, "fileupload_app/upload.html", {"form": form})
