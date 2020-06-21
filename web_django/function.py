# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('李宝华')
    return render(request, 'index.html')


def result(request):
    user_text = request.GET['text']
    count_sum = len(user_text)
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)


    return render(request, 'result.html',
                  {'num_sum' : count_sum , 'text': user_text,
                   'dict': word_dict,
                   'sorted':sorted_dict})

def about(request):
    # return HttpResponse('李宝华')
    return render(request, 'about.html')