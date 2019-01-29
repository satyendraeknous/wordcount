from django.http import HttpResponse
from django.shortcuts import render
import operator



def homepage(request):
    return render(request, 'home.html')


def count(request):
    data = request.GET['fulltextarea'] 
    word_list = data.split()
    listlenght = len(word_list)

    #for word count
    wordsdic = {}
    for words in word_list:
        if words in wordsdic:
            wordsdic[words] += 1
        else:
            wordsdic[words] = 1

    #for sorted list
    sorted_list = sorted(wordsdic.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'data':data,
                                        'listlenght':listlenght,
                                        'wordsdic':sorted_list})


def about(request): 
    return render(request, 'about.html')