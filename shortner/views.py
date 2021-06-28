from django.core.checks import messages
from django.shortcuts import render
from .models import ShortUrl
import random,string

def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(6))

def index(request):
    if request.method == 'POST':
        if request.POST.get('original') and request.POST.get('short'):
            original = request.POST.get('original')
            short = request.POST.get('short')
            check = ShortUrl.objects.filter(short_query = short)
            if not check:
                newurl = ShortUrl(
                    original_url = original,
                    short_query = short
                )
                newurl.save()
                res = 'success'
                msg = 'https://shrinkthelink.herokuapp.com/'+ str(short)
                return render(request,'index.html',{'msg':msg})
            else:
                msg = "Oops! unique name already exists"
                return render(request,'index.html',{'msg':msg})
        elif request.POST.get('original'):
            original=request.POST.get('original')
            generated = False
            while not generated:
                short = randomgen()
                check = ShortUrl.objects.filter(short_query = short)
                if not check:
                    newurl = ShortUrl(
                    original_url = original,
                    short_query = short
                )
                    newurl.save()
                    msg = 'https://shrinkthelink.herokuapp.com/'+ str(short)
                    return render(request,'index.html',{'msg':msg})
                else:
                    msg = "Oops! unique name already exists"
                    return render(request,'index.html',{'msg':msg})

    return render(request,'index.html')