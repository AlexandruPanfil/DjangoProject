from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # is_published = forms.BooleanField(required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Empty")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Not Selected"

    class Meta:
        model = PC
        # fields = '__all__'    # This field is adding all fields of our class
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input'}),
                   'slug': forms.TextInput(attrs={'class': 'form-input'}),
                   'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
                   }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Must be maximum 200 words')

        return title