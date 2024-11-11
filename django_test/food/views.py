from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm
from faker import Faker

def item_list(request):
    """
    View function for listing all items.
    """
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, pk):
    """
    View function for displaying details of a specific item.
    """
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

def item_create(request):
    """
    View function for creating a new item.
    """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('item:item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form, 'action': 'Create'})

def item_update(request, pk):
    """
    View function for updating an existing item.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('item:item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form, 'action': 'Update'})

def item_delete(request, pk):
    """
    View function for deleting an item.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item:item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})


def fake_item(request, total):
    fake= Faker() 

    for _ in range(total):
        Item.objects.create(item_name=fake.sentence(), 
                            item_desc=fake.text(), 
                            item_price=fake.random_number(digits=2) )
        
        # Item.objects.create(title=fake.sentence(), description=fake.text(), price=fake.random_number(digits=2) )
    return redirect('item:item_list')