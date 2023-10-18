# i have created this file and was not created from before!!
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("hello world in DJango programming!!!")
# def about(request):
#     return HttpResponse("hello world in DJango programming!!!... THIS IS THE ABOUT PAGE IN DJANGO PROGRAMING!!")

# def test(response):
#     return HttpResponse("<h1>testing the test endpoint of html element embedded</h1>")
# these were the codes for basic understanding!!

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name':'json', 'place':'new delhi'}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')
    # return HttpResponse("hello views")

def analyze(request):
    # the next line is geting the text
    djtext=request.GET.get('text', 'default')

    # check the checkbox values
    removepunc=request.GET.get('removepunc', 'off')
    fullcaps=request.GET.get('fullcaps', 'on')
    lineremover=request.GET.get('lineremover', 'off')
    # print(removepunc)
    # print(djtext)

    # chec which checkbox is "on"
    if removepunc=="on":        
        # return HttpResponse("analyze the given text from frontend!!!")
        punctuations=''':;'",./?><{}[]()*&^%$#@!~`|-+'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+ char
        params={'purpose':'removed punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    # hcek if full caps checkbox is on or not!!
    elif(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params={'purpose':'Changed to UPPER CASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
        
    elif(lineremover == "on"):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed= analyzed + char
        params={'purpose':'REMOVED NEW LINES', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("error!!")