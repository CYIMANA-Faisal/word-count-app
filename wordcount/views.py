from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def count(request):
    fulltext = request.GET['full_text']
    lst_fulltext = fulltext.split()

    def histogram(lst):
        word_list = dict()
        for word in lst:
            if word in word_list:
                word_list[word] = word_list[word] + 1
            else:
                word_list[word] = 1
        return word_list

    def invert_dct(d):
        inverse = dict()
        for key, val in d.items():
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
        return inverse

        return inverse
    word_lst = histogram(lst_fulltext)
    inverted = invert_dct(word_lst)
    return render(request, 'count.html',{'fulltext':fulltext, 'words':len(lst_fulltext), 'most':inverted[max(inverted)]})
def about(request):
    return render(request, 'about.html', {})









