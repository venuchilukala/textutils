from django.http import HttpResponse
from django.shortcuts import render 



def index(request):
    return render(request, 'index.html')
    # return HttpResponse('<h1>Home</h1>')

def analyze(request):
    #Get text in the text area
    dj_text = request.GET.get('text', 'default')
    
    #Get status of check box of utils
    #request.GET => to get query params in GET request 
    # get('removepunc', 'off') => to get value of a 'removepunc'
    removepunc = request.GET.get('removepunc', 'off')
    capsall = request.GET.get('capsall', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremove = request.GET.get('extraspaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
     
   #Render the result
    if removepunc == 'on':
        punctuations = '''.,?!:;'"()[]—-…/^_&'''
        analyzed_text = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed_text += char        
        params ={
            'purpose' : 'Removed Punctuations',
            'analyzed_text' : analyzed_text
        }
        return render(request,'analyze.html',params)
    
    elif capsall == 'on':
        analyzed_text = dj_text.upper()
        params = {
            'purpose' : 'Capitalized the Text',
            'analyzed_text' : analyzed_text
        }
        return render(request, 'analyze.html', params)
    
    elif newlineremover == 'on':
        analyzed_text = ''
        for char in dj_text:
            if char != '\n':
                analyzed_text += char       
        params = {
            'purpose' : 'New Lines Removed',
            'analyzed_text' : analyzed_text
        }
        return render(request, 'analyze.html', params)
    
    elif extraspaceremove == 'on':
        analyzed_text = ''      
        for index, char in enumerate(dj_text):
            if not(dj_text[index] == ' ' and dj_text[index+1] == ' '):
                analyzed_text += char         
        params = {
            'purpose' : 'Extra Spaces Removed',
            'analyzed_text' : analyzed_text
        }
        return render(request, 'analyze.html', params)
        
    
    elif charcount == 'on':
        analyzed_text = 'The no of characters are : ' +  str(len(dj_text))
        params = {
            'purpose' : 'Extra Spaces Removed',
            'analyzed_text' : analyzed_text
        }    
        return render(request, 'analyze.html', params)
        
    else:
        return HttpResponse('Error')
