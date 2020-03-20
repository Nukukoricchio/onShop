from django import forms 


QUANTITY_CHOICES = [(i, str(i)) for in in range(1, 21)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES,
		                                coerce=int)
	update = forms.BooleanField(required=False,
		                        initial=False,
		                        widget=forms.HiddenInput)