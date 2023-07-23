from django.shortcuts import render


def manager_index(request):
    return render(request, 'Manager/manager_index.html')
