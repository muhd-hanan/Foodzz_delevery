# forms.py
from django import forms
from .models import *

class StoreEditForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["name", "tagline", "image", "rating", "time", "offer"]

        widgets = {
    "email": forms.EmailInput(attrs={
        "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500",
        "placeholder": "Email"
    }),
    "password": forms.PasswordInput(attrs={
        "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500",
        "placeholder": "Password"
    }),
    "name": forms.TextInput(attrs={
        "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500",
        "placeholder": "Store name"
    }),
    "tagline": forms.TextInput(attrs={
        "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500",
        "placeholder": "Tagline"
    }),
    "categories": forms.SelectMultiple(attrs={
        "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
    }),
    "image": forms.FileInput(attrs={
        "class": "w-full text-slate-600 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500"
    }),
    "rating": forms.NumberInput(attrs={
        "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500",
        "placeholder": "Rating"
    }),
    "time": forms.NumberInput(attrs={
        "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500",
        "placeholder": "Time"
    }),
    "offer": forms.TextInput(attrs={
        "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500",
        "placeholder": "Store offer"
    }),
}
        

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500",
                "placeholder": "Enter category name"
            }),
            "store": forms.Select(attrs={
                "class": "w-full px-3 py-2 border border-slate-300 rounded-lg bg-white outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
            }),
        }


from django import forms
from .models import FoodItem, FoodCategory

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'is_veg', 'price', 'image', 'categry']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-2',
                'placeholder': 'Enter food item name'
            }),
            'is_veg': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-green-600 border-slate-300 rounded'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-2',
                'placeholder': 'Enter price'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-2'
            }),
            'categry': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-2'
            }),
        }

    def __init__(self, *args, **kwargs):
        store = kwargs.pop('store', None)   # 👈 store passed from view
        super().__init__(*args, **kwargs)
        if store:
            self.fields['categry'].queryset = FoodCategory.objects.filter(store=store)
