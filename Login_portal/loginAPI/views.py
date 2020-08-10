from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm

# Create your views here.
def user(request):
    print('user method called',)
    if request.method=='POST':
        form = UserForm(request.POST)
        print('hello ankur',form.is_valid())
        if form.is_valid():
            try:
                print('inside try')
                form.save()
                # return redirect('/show')
                return redirect('/show')
            except:
                pass
    else:
        form=UserForm()
        print(form)
    return render(request,'index.html',{'form':form})
def show(request):
    users=User.objects.all
    print('now inside the show method')
    return render(request,'show.html',{'users':users})

