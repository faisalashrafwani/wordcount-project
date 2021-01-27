# This code helps to return the response as Http.
from django.http import HttpResponse
from django.shortcuts import render
import operator


def intro(request):
    return HttpResponse('Hello There!, This is my default page. this is being sent as string. You can create HTML code right here in the string for some weird reason but thats just a dumb idea like <h1> HELLO </h1> Rather use your already created HTML page and use Template.')


def myprofile(request):
    return render(request, 'profile.html')


def homepage(request):
    return render(request, 'homepage.html')


def count(request):

    fetchedtext = request.GET['fulltext']  # coming from Homepage
    # coming from Homepage, splits the "string" into "list".
    wordlist = fetchedtext.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True) #worddict.items() converts dict into list
    return render(request, 'count.html', {'sendintocount': fetchedtext, 'countedwords': len(wordlist), 'sendworddict': sortedwords})
