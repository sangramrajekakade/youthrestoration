from django import forms
from .models import *
from django.forms import ModelForm



class AppointmentForm(ModelForm):
	F_Name = forms.CharField(required=False, widget=forms.TextInput(
		attrs=
		{
		'placeholder'							: "First Name",
		
		}
		))
	L_Name = forms.CharField(required=False, widget=forms.TextInput(
		attrs=
		{
		'placeholder'							: "Last Name",
		
		}
		))
	Mobile = forms.CharField(required=False, widget=forms.TextInput(
		attrs=
		{
		'placeholder'							: "Mobile No.",
		
		}
		))
	Email = forms.CharField(required=False, widget=forms.TextInput(
		attrs=
		{
		'placeholder'							: "Email",

		}
		))
	message = forms.CharField(required=False, widget=forms.Textarea(
		attrs=
		{
		'placeholder'							: "Message",

		}
		))
	class Meta:
		model = Appointment
		fields = '__all__'
		exclude = ['created_at']

