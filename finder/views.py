from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, AdminRegisterForm, UserLoginForm, ItemReportForm
from .models import Item
from django.contrib.auth.decorators import login_required

# 1. Homepage View (fulfills "homepage", "20-25 things", "lost and found section")
def homepage(request):
    # Get up to 25 lost items
    lost_items = Item.objects.filter(status='lost').order_by('-date_reported')[:25]
    # Get up to 25 found items
    found_items = Item.objects.filter(status='found').order_by('-date_reported')[:25]
    
    context = {
        'lost_items': lost_items,
        'found_items': found_items,
    }
    return render(request, 'finder/home.html', context)

# 2. Registration View for regular users
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirect to login page after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'finder/register.html', {'form': form, 'type': 'User'})

# 3. Registration View for administrators
def register_admin(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_administrator = True  # <-- Set the admin flag
            user.save()
            return redirect('login')
    else:
        form = AdminRegisterForm()
    return render(request, 'finder/register.html', {'form': form, 'type': 'Administrator'})

# 4. Login View (fulfills "when user enters correct credentials... direct him")
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # This is the redirect you wanted!
                return redirect('dashboard') # We will create 'dashboard' next
    else:
        form = UserLoginForm()
    return render(request, 'finder/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')

# 5. Dashboard View (the "lost and found section" after login)
@login_required # This view is protected, user must be logged in
def dashboard(request):
    return render(request, 'finder/dashboard.html')

# 6. "Lost Complaint" Form View (fulfills "generate a form")
@login_required
def report_lost_item(request):
    if request.method == 'POST':
        form = ItemReportForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.status = 'lost'  # <-- Set status to 'lost' automatically
            item.save()
            return redirect('dashboard') # Go back to dashboard
    else:
        form = ItemReportForm()
        
    return render(request, 'finder/report_form.html', {'form': form, 'type': 'Lost'})

# 7. "Found Item" Form View (Good to have)
@login_required
def report_found_item(request):
    if request.method == 'POST':
        form = ItemReportForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.status = 'found' # <-- Set status to 'found' automatically
            item.save()
            return redirect('dashboard')
    else:
        form = ItemReportForm()
        
    return render(request, 'finder/report_form.html', {'form': form, 'type': 'Found'})