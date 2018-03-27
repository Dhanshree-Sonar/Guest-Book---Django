from django import forms

class CommentForm(forms.Form):
    name = CharField(max_length=20)
    comment = forms.CharField(widget=forms.Textarea())
    
