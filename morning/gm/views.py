from django.shortcuts import render
from .forms import workout_forms,workout_froms_f
from .models import workout_model
from django.http import HttpResponse

# Create your views here.
def workout_views(requst):
    form=workout_forms()
    if requst.method=='POST':
        form=workout_forms(requst.POST)
        form.is_valid()
        form.save()
        print('day:',form.cleaned_data['day'])
        print('workout_name:',form.cleaned_data['workout_name'])
    gym=workout_model.objects.all()
    return render(requst,'gm.html',{'form':form,'gym':gym})

def index(requst):
    requst.session.set_test_cookie()
    return HttpResponse('<h1>index page</h1>')
def check_view(requst):
    if requst.session.test_cookie_worked():
        print('cookies are working properly')
        requst.session.delete_test_cookie()
        return HttpResponse('<h1>checking page </h1>')
