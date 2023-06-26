from typing import List

from django.shortcuts import render

# Create your views here.

def some_list(request):
    some_list: list[str] = ["abc", "def", "ghi"]
    context = {"some_list": some_list}
    return render(request, "someList.html", context)