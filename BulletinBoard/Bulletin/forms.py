from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'contact', 'category']
        labels = {
            'title': 'Введите заголовок',
            'description': 'Описание поста',
            'image': 'Выберите файл',
            'contact': 'Контактный телефон',
            'category': 'Выберите категорию',
        }

        widgets = {
            'title': forms.Textarea(attrs={
                'class':'form-control', 
                'placeholder':'Заголовок объявления'
                }),

            'description': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Описание объявления'
                }),
        
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'type': 'file'
                })

        }