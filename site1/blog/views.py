from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.context_processors import csrf
from blog.models import Account, Blog
import datetime
from django.utils import timezone

now = datetime.datetime.now()
udate = '{}-{}-{}'.format(now.year, now.month, now.day)
accounts = Account.objects.all()

def say_hi(request):
    #return render(request, 'index.html', {'variable': 'world'})
    a = {'variable': 'world'}
    #return HttpResponse(json.dumps(a), content_type='application/json')    
    return JsonResponse(a, safe=False)

def test(request):
    return render(request, 'ajax_test.html')

def index(request):
    c = {}
    c.update(csrf(request))
    if 'txt_name' in request.POST:
        r = request.POST
        for a in accounts:
            if a.name == r['txt_name'] and a.pwd == r['txt_pwd']:
                return render(request, 'write_blog.html', locals())
            else:
                return HttpResponse("Wrong username or password!")

    elif 'txt_area' in request.POST:
        r = request.POST
        utitle = r['title']
        uauthor = r['author']
        upost = r['txt_area']
        udtime = timezone.now()
        for a in accounts:
            if a.name == uauthor:
                p = Blog(title=utitle, author=a, post=upost, publish=udtime)
                p.save()
                return HttpResponseRedirect('read')
            else:
                return HttpResponse('Well, ' + request.POST['author'] + '. Some thing went wrong!')
    else:
        return render(request, 'login_signup.html', locals())


def signup(request):
    c = {}
    c.update(csrf(request))
    if 'txt_name' and 'txt_pwd' in request.POST:
        uname = request.POST.get('txt_name', '')
        upwd = request.POST.get('txt_pwd', '')
        a = Account(name=uname, pwd=upwd, date=udate)
        a.save()
        return HttpResponse("OK! You've successfully signed up!!")
    else:
        return render(request, 'login_signup.html')


def read_blog(request):
    blogs = Blog.objects.all().order_by('-publish')
    return render(request, 'show_blog.html', {'blogs': blogs})

