from django import forms


class GroceryListForm (forms.Form):
    Item = forms.CharField(label="Add item to list ",
                           max_length=100, required=True)
