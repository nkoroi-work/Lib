

from django import forms
 

from .models import *
 
# create a ModelForm
class bookForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = book
        fields = "__all__"

class publisherForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = publisher
        fields = "__all__"

class book_copiesForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = book_copies
        fields = "__all__"

class book_loansForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = book_loans
        fields = "__all__"

class book_authorsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = book_authors
        fields = "__all__"

class borrowerForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = borrower
        fields = "__all__"

class library_branchForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = library_branch
        fields = "__all__"