from django.shortcuts import render

from main.models import Main


def main(request):
    main = Main.objects.all()
    return render(request, 'main/main.html', {'model': main})
