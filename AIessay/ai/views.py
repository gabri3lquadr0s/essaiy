from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='../core')
def dashboard(request):
    return render(request, 'ai/dashboard.html')

@staff_member_required(login_url='../core')
def feedModel(request):
    return render(request, 'ai/feedModel.html')

@staff_member_required(login_url='../core')
def addThemes(request):
    return render(request, 'ai/addThemes.html')

@staff_member_required(login_url='../core')
def checkEssays(request):
    return render(request, 'ai/checkEssays.html')
