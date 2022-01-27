from django.shortcuts import render

from .models import GroceryItem


def grocery_list(request):
    if request.method == "POST":
        if "create_item" in request.POST:
            GroceryItem.objects.create(description=request.POST.get("description"))
        elif "complete" in request.POST:
            GroceryItem.objects.filter(pk=request.POST.get("complete")).update(completed=True)
        elif "incomplete" in request.POST:
            GroceryItem.objects.filter(pk=request.POST.get("incomplete")).update(completed=False)
        elif "delete" in request.POST:
            GroceryItem.objects.filter(pk=request.POST.get("delete")).delete()
    return render(request, "grocery_list.html", {"grocery_list": GroceryItem.objects.all()})