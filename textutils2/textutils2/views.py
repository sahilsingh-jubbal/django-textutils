#I am created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def analyse(request):
    #get the text
    djtext = request.GET.get('text1','default')
    print(djtext)
    check1 = request.GET.get('check', 'off')
    print(check1)
    check2 = request.GET.get('check2', 'off')
    print(check2)
    check3 = request.GET.get('check3', 'off')
    print(check3)

    check4 = request.GET.get('check4', 'off')
    print(check4)
    check5 = request.GET.get('check5', 'off')
    print(check5)


    #analysed=djtext
    if(check1 == 'on'):
        punc = '''!()-[];:'"\,<>./?@#$%^&*~'''
        analysed=""

        for char in djtext:
            if char not in punc:
                analysed= analysed + char

        wow={'purpose': 'punctions remover' , 'analyzed_text': analysed}
        djtext = analysed

        #return render(request,'analyse.html',wow)

    if (check2 == 'on'):
        analysed = ""

        for char in djtext:
            analysed = analysed + char.upper()

        wow = {'purpose': 'punctions remover', 'analyzed_text': analysed}
        djtext= analysed

        #return render(request, 'analyse.html', wow)


    if (check3 == 'on'):
        count=0
        for char in djtext:
            if char !=" ":
                count=count+1


        wow = {'purpose': 'punctions remover', 'analyzed_text': count}
        djtext=count
        #return render(request, 'analyse.html', wow)


    if (check4 == 'on'):
        analyse=""

        for char in djtext:
            if char != " ":
                analyse = analyse+ char

        wow = {'purpose': 'punctions remover', 'analyzed_text': analyse}
        djtext=analyse
        #return render(request, 'analyse.html', wow)


    if (check5 == 'on'):
        analyse = djtext.strip()


        wow = {'purpose': 'punctions remover', 'analyzed_text': analyse}
        djtext=analyse
        #return render(request, 'analyse.html', wow)



    # else:
    #     return HttpResponse("Error")

    elif(check1 == 'off' and check2 == 'off' and check3 == 'off' and check4 == 'off' and check5 == 'off'):
        return HttpResponse("<h1><font color='red'>Error</font></h1>")
    return render(request,'analyse.html',wow)
