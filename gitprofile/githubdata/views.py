from django.shortcuts import render
import requests

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        url = "https://api.github.com/users/{}".format(username)
        print(url)
        data = requests.get(url).json()
        print(data)
        return render(request, 'index.html',{'data':data})
    else:
        return render(request, 'index.html')
