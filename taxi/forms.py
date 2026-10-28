from django import forms
from .models import Driver, Car
from django.core.exceptions import ValidationError


import re


class DriverLicenseUpdateForm(forms.ModelForm):
    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if not re.fullmatch(r"^[A-Z]{3}[0-9]{5}$", license_number):
            raise ValidationError("Invalid license number format")
        return license_number

    class Meta:
        model = Driver
        fields = ["license_number"]


class DriverCreateForm(forms.ModelForm):
    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if not re.fullmatch(r"^[A-Z]{3}[0-9]{5}$", license_number):
            raise ValidationError("Invalid license number format")
        return license_number

    class Meta:
        model = Driver
        fields = ["username", "first_name", "last_name", "license_number"]


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"
