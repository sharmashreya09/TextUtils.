
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request,'index.html')

def analyze(request):
     djtext=request.POST.get('text','default')
     removepunc=request.POST.get('removepunc','off')
     fullcaps=request.POST.get('fullcaps','off')
     lineremove=request.POST.get('lineremove','off')
     spaceremove=request.POST.get('spaceremove','off')

     if (removepunc == "on"):
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analyzed = ""
          for char in djtext:
               if char not in punctuations:
                    analyzed = analyzed + char

          params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
          djtext = analyzed

     if (fullcaps == "on"):
          analyzed = ""
          for char in djtext:
               analyzed = analyzed + char.upper()

          params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
          djtext = analyzed

     if (spaceremove == "on"):
          analyzed = ""
          for index, char in enumerate(djtext):
               if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char

          params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
          djtext = analyzed

     if (lineremove == "on"):
          analyzed = ""
          for char in djtext:
               if char != "\n" and char != "\r":
                    analyzed = analyzed + char

          params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

     if (removepunc != "on" and lineremove != "on" and spaceremove!= "on" and fullcaps != "on"):
          return HttpResponse("please select any operation and try again")

     if(analyzed==""):
          return HttpResponse("Please type some text first ")


     return render(request, 'analyze.html', params)

