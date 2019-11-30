from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def count(request):
    
    # full text is the name of text area

    fulltext = request.GET['fulltext'] 
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 
           'sortedwords':sortedwords})

        

