from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User
from django import forms


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(label='', 
		widget=forms.TextInput(
			attrs={'class':'form-control', 'placeholder':'Enter your first name'}))

	last_name = forms.CharField(label='', 
		widget=forms.TextInput(
			attrs={'class':'form-control', 'placeholder':'Enter your last name'}))

	email = forms.EmailField(label='', 
		widget=forms.TextInput(
			attrs={'class':'form-control', 'placeholder':'Enter your email address', 'size':100}))

	phone_number = forms.CharField(label='', 
		widget=forms.TextInput(
			attrs={'class':'form-control', 'placeholder':'Enter your phone_number'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name','email', 'phone_number', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
		self.fields['first_name'].label=""
		self.fields['first_name'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters only.</small></span>'

		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
		self.fields['last_name'].label=""
		self.fields['last_name'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters only.</small></span>'

		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
		self.fields['email'].label=""
		self.fields['email'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['phone_number'].widget.attrs['class'] = 'form-control'
		self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter your phone number'
		self.fields['phone_number'].label=""
		self.fields['phone_number'].help_text='<span class="form-text text-muted"><small style="color:red">Required.\nPhone numbers <b>MUST</b> contain your country code.\nPlease check the number to ensure it is right</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
		self.fields['password1'].label=""
		self.fields['password1'].help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Your Password'
		self.fields['password2'].label=""
		self.fields['password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification</small></span>'

