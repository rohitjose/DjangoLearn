from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	"""docstring for SignUpForm"""
	class Meta:
		model = SignUp
		#fields = ['full_name','email','age']
		exclude = ['age']

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if not  "@gmail.com" in email:
			raise forms.ValidationError("Enter a valid email address")
		return email
