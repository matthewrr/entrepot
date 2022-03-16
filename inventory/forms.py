from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            'name',
            'quantity',
            'description',
            'img',
            'high_value',
            'tags',
            'category',
            'subcategory',
            'content_type',
        )