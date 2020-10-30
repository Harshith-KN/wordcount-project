from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html',{'apple':'siri'})

def eggs(request):
	return HttpResponse("Fuck u Eggs")

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	count = len(wordlist)
	dic={}
	for i in wordlist:
		if i in dic:
			#Increase
			dic[i]+=1
		else:
			#add to the dictionary
			dic[i]=1
		
	sw = sorted(dic.items(), key=operator.itemgetter(1) , reverse=True)

	return render(request,'count.html',{"full":fulltext,"count":count,"worddictionary":sw})

def about(request):
	return render(request,'about.html')
