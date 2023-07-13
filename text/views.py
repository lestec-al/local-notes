from django.shortcuts import render
from text.models import Text


def homeView(request):

    if request.method == "POST":

        if request.POST.get("save"):
            Text.objects.all().delete()
            
            idx = 1
            for text in request.POST.getlist("notes"):
                if text != None:
                    Text.objects.update_or_create(id=idx, defaults={"text": text})
                idx += 1

    context = {}
    context["objs"] = Text.objects.all()

    return render(request, "home.html", context)