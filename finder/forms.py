from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Item

# 1. Form for a regular user to register
class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

# 2. Form for an administrator to register
class AdminRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

# 3. Form for login (uses a built-in form)
class UserLoginForm(AuthenticationForm):
    pass

# 4. This is your "Lost Complaint" form
class ItemReportForm(forms.ModelForm):
    class Meta:
        model = Item
        # We only ask the user for these fields
        # 'reported_by' and 'status' will be set automatically in the view
        fields = ['name', 'description', 'location']