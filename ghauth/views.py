from django.shortcuts import render
from github import Github
from django.http import HttpResponse

def home(request):
    repos = []
    if request.user.is_authenticated:
        access_token = request.user.social_auth.get(provider='github').extra_data['access_token']
        g = Github(access_token)
        user = g.get_user()
        repos = user.get_repos()
    return render(request,'home.html', {'repos': repos})
