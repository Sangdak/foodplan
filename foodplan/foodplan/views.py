from django.shortcuts import render


def user_profile(request):
    context = {
        'user_info': request.user,
    }
    return render(request, 'lk.html', context)
