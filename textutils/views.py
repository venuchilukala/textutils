from django.http import HttpResponse
from django.shortcuts import render 


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('<h1>Home</h1>')

def analyze(request):
    #Get text in the text area
    dj_text = request.POST.get('text', 'default')
    #Get status of check box of utils
    #request.GET => to get query params in GET request 
    # get('removepunc', 'off') => to get value of a 'removepunc'
    removepunc = request.POST.get('removepunc', 'off')
    capsall = request.POST.get('capsall', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
     
    analyzed_text = ""
    purpose = []
   #Render the result
    if removepunc == 'on':
        punctuations = '''.,?!:;'"()[]—-…/^_&'''
        for char in dj_text:
            if char not in punctuations:
                analyzed_text += char        
        dj_text = analyzed_text
        purpose.append('Removed Punctuations')
    
    if capsall == 'on':
        analyzed_text = dj_text.upper()
        dj_text = analyzed_text
        purpose.append('Capitalized the Text')
    
    if newlineremover == 'on':
        analyzed_text = ''
        for char in dj_text:
            if char != '\n' and char != '\r':
                analyzed_text += char 
        dj_text = analyzed_text
        purpose.append('New Lines Removed')
    
    if extraspaceremove == 'on':
        analyzed_text = ''      
        for index, char in enumerate(dj_text):
            if not(dj_text[index] == ' ' and dj_text[index+1] == ' '):
                analyzed_text += char         
        dj_text = analyzed_text
        purpose.append('Extra Spaces Removed')
        
    char_count_message = ''
    
    if charcount == 'on':
        char_count_message = f"The number of characters are: {len(dj_text)}"
        purpose.append('Characters counted')
         
        
    params ={
            'purpose' : ', '.join(purpose) if purpose else 'No operations done',
            'analyzed_text' : analyzed_text + (f"<br>{char_count_message}" if char_count_message else '')
        }
    
    if(removepunc != 'on' and capsall != 'on' and newlineremover != 'on' and extraspaceremove != 'on' and charcount != 'on'):    
        return HttpResponse('Please Select any operationtion')
    else:
        return render(request, 'analyze.html', params)
