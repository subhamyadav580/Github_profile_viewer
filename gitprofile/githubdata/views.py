from django.shortcuts import render
import requests

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        url = "https://api.github.com/users/{}".format(username)
        data = requests.get(url).json()
        return render(request, 'index.html',{'data':data})
    else:
        return render(request, 'index.html')
