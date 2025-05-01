from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category, Link
from .forms import LinkForm, CategoryForm

def dashboard(request):
    categories = Category.objects.all()
    return render(request, 'main.html', {'categories': categories})

def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Link berhasil ditambahkan!')
            return redirect('main:home')
    else:
        form = LinkForm()
    
    return render(request, 'form.html', {'form': form, 'title': 'Tambah Link'})

def edit_link(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Link berhasil diperbarui!')
            return redirect('main:home')
    else:
        form = LinkForm(instance=link)
    
    return render(request, 'form.html', {'form': form, 'title': 'Edit Link'})

def delete_link(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    link.delete()
    messages.success(request, 'Link berhasil dihapus!')
    return redirect('main:home')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil ditambahkan!')
            return redirect('main:home')
    else:
        form = CategoryForm()
    
    return render(request, 'form.html', {'form': form, 'title': 'Tambah Kategori'})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil diperbarui!')
            return redirect('main:home')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'form.html', {'form': form, 'title': 'Edit Kategori'})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, 'Kategori berhasil dihapus!')
    return redirect('main:home')