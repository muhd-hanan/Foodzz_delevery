from django import forms
from dboy.models import DeliveryBoy
from restaurant.models import *
from customer.models import *



class StoreCategoryForm(forms.ModelForm):
    class Meta:
        model = StoreCategory
        fields = ["name", "image"]


        widgets = {
            "name":forms.widgets.TextInput(attrs={"class": "form-control" ,"placeholder": "Category name"}),
            "image":forms.widgets.FileInput(attrs={"class": "form-control"})
        }
        



class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["email", "password", "name", "tagline", "categories", "image", "rating", "time", "offer"]

        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Store name"}),
            "tagline": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tagline"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),  
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Rating"}),
            "time": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Time"}),
            "offer": forms.TextInput(attrs={"class": "form-control", "placeholder": "Store offer"}),
        }




class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ["name", "image", "store"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-slate-300 px-3 py-2",
                "placeholder": "Slider Name"
            }),
            "image": forms.FileInput(attrs={
                "class": "w-full rounded-lg border border-slate-300 px-3 py-2"
            }),
            "store": forms.Select(attrs={
                "class": "w-full rounded-lg border border-slate-300 px-3 py-2"
            }),
        }




class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ["name", "store"]


        widgets = {
            "name":forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"Category Name"}),
            "store":forms.widgets.Select(attrs={"class":"form-control"}),
        }







class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ["name", "image", "price", "categry", "is_veg"]


        widgets = {
            "name":forms.widgets.TextInput(attrs={"class":"form-control","placeholder":"Food Item Name"}),
            "image":forms.widgets.FileInput(attrs={"class":"form-control"}),
            "price":forms.widgets.NumberInput(attrs={"class":"form-control", "placeholder":"Price"}),
            "categry":forms.widgets.Select(attrs={"class":"form-control"}),
            "is_veg":forms.widgets.CheckboxInput(attrs={"class":"form-check-input"}),
        }

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ["coupon_code", "description", "offer", "is_percentage"]

        widgets = {
            "coupon_code": forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border rounded-lg focus:ring focus:ring-blue-300",
                "placeholder": "Enter Coupon Code"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-3 py-2 border rounded-lg focus:ring focus:ring-blue-300",
                "rows": 3,
                "placeholder": "Enter Description"
            }),
            "offer": forms.NumberInput(attrs={
                "class": "w-full px-3 py-2 border rounded-lg focus:ring focus:ring-blue-300",
                "placeholder": "Enter Offer Value"
            }),
            "is_percentage": forms.CheckboxInput(attrs={
                "class": "h-4 w-4 text-blue-600 focus:ring focus:ring-blue-300"
            }),
        }





class DeliveryBoyForm(forms.ModelForm):
    class Meta:
        model = DeliveryBoy
        fields = ["email", "password", "name", "phone", "address"]

        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "placeholder": "Enter email"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "placeholder": "Enter password"
            }),
            "name": forms.TextInput(attrs={
                "class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "placeholder": "Full name"
            }),
            "phone": forms.TextInput(attrs={
                "class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "placeholder": "Phone number"
            }),
            "address": forms.Textarea(attrs={
                "class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "rows": 3,
                "placeholder": "Address"
            }),
        }
