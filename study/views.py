from typing import List

from django.shortcuts import render

# Create your views here.

def some_list(request):
    someList: list[str] = ["abc", "def", "ghi"]
    context = {"someList": someList}
    return render(request, "someList.html", context)