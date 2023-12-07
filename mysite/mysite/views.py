# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')  # entering the inputted text in the variable djtext
    print(djtext)
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # check which check box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if char != " " or (index + 1 < len(djtext) and djtext[index + 1] != " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and uppercase != "on":
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)