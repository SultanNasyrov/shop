from django.shortcuts import render


def test(request):
    return render(request, 'ui_pack/ui_pack.html')
