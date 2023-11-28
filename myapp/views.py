from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Image
from .forms import ImageForm
from django.contrib import messages

# Create your views here.
def home(request):
    img = Image.objects.all()           #jese hi yha all() use kiya to matlab ki humko html file me for loop use krna hoga kyoki multiple values hogi.
    if request.method == 'POST':
        fm = ImageForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Image Uploaded Successfully.')
        return redirect('home')
    else:
        fm = ImageForm()
    return render(request,'myapp/home.html',{'form':fm,'img':img})

def delete1(request,id):
    img = Image.objects.all()
    imga = Image.objects.get(pk=id)
    imga.delete()
    messages.success(request,'Image deleted successfully')
    return redirect('home')