from django.shortcuts import render,redirect,HttpResponse
from .models import Coffee
from .forms import CoffeeForm


def coffee_list(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffee/index.html', {'coffees': coffees})

def coffee_create(request):
    empty_form = CoffeeForm()
    if request.method == 'POST':
        data = CoffeeForm(request.POST, request.FILES)
        print(data)
        if data.is_valid():
            data.save()
            
            return redirect('coffee_list')
    return render(request, 'coffee/add.html', {'form':empty_form, 'error': 'Add is successfully!'})

def coffee_update(request, pk):
    data = Coffee.objects.get(pk=pk)
    form = CoffeeForm(instance=data)
    print(data)
    if request.method == 'POST':
        form = CoffeeForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('coffee_list')
    return render(request, 'coffee/update.html', {'form': form})

def coffee_delete(request, pk):
    coffee = Coffee.objects.get(pk=pk)
    if coffee:
        coffee.delete()
        return redirect('coffee_list')