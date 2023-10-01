from django import forms


class ProductCreateForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.FloatField()


class ProductUpdateForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.FloatField()


class ProductDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="Are you sure you want to delete?")
