from django.http import HttpResponse
from django.shortcuts import render 



def index(request):
    return render(request, 'index.html')
    # return HttpResponse('<h1>Home</h1>')

def analyze(request):
    dj_text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(dj_text)
    print(removepunc)
    
    
    if removepunc == 'on':
        punctuations = '''.,?!:;'"()[]—-…/^_&'''
        analyzed_text = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed_text += char 
        print(analyzed_text)
        
        params ={
            'purpose' : 'Removed Punctuations',
            'analyzed_text' : analyzed_text
        }
        
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('Error')



# def capfirst(request):
#     return HttpResponse('<p>Capitalize first character</p>')

# def newlineremove(request):
#     return HttpResponse('<p>New line removed</p>')

# def spaceremove(request):
#     return HttpResponse('<p>Space is removed</p>')

# def charcount(request):
#     return HttpResponse('<p>Character count</p>')