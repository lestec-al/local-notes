from django.shortcuts import render, redirect
from text.models import Text
from run import LINK
import pyqrcode

def homeView(request):
    if request.method == "POST":
        Text.objects.all().delete()
        idx = 1
        for i in zip(request.POST.getlist("noteTitles"), request.POST.getlist("notes")):
            title = i[0]
            # Simple validation, no need use forms
            if len(title) > 120:
                title = title[0:121]
            text = i[1]
            Text.objects.create(id=idx, title=title, text=text)
            idx += 1
    context = {}
    context["objs"] = Text.objects.all()
    context["linkImg"] = pyqrcode.create(LINK).png_as_base64_str(scale=5)
    return render(request, "home.html", context)

def otherView(request, *args, **kwargs):
    return redirect("home")