from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    """
    Form for creating and updating Item instances.
    
    This form is based on the Item model and includes fields for
    item_name, item_desc, and item_price.
    """

    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'item_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'item_name': 'Item Name',
            'item_desc': 'Item Description',
            'item_price': 'Item Price',
        }

    def clean_item_price(self):
        """
        Custom validation for item_price field.
        
        Ensures that the price is not negative.
        """
        price = self.cleaned_data.get('item_price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price