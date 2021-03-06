# -*- coding: utf-8 -*-

from django import forms
from .models import Category, Catalog, ExpresFiles, FilesCatalog, FilesExpres

class CatalogForms(forms.ModelForm):
    cover = forms.ImageField()
    title = forms.CharField(
        label='',
        error_messages='',
        required=True,
        max_length=50,
        widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Название'})
    )
    category = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        widget=forms.Select({'name': 'city', 'id': 'city', 'class': 'form-control', 'aria-describedby': 'basic-amount'})
    )

    description = forms.CharField(
        label='Описание',
        max_length=300,
        widget=forms.Textarea({'class': 'form-control', 'placeholder': 'Описание'}))
    # is_open = forms.BooleanField(
    #     label='Опубликован',
    #     help_text='Доступен всем',
    #     required=False,
    #     widget=forms.CheckboxInput({'onclick': 'return OptionsSelectedIsOpen(window.event)'}))
    # is_slug = forms.BooleanField(
    #     label='Доступ по ссылке',
    #     help_text='Доступно только по ссылке',
    #     required=False,
    #     widget=forms.CheckboxInput({'onclick': 'return OptionsSelectedIsSlug(window.event)'}))
    # is_for_me = forms.BooleanField(
    #     label='Только для меня',
    #     help_text='Доступно только для Вас',
    #     required=False,
    #     widget=forms.CheckboxInput({'onclick': 'return OptionsSelectedIsForMe(window.event)'}))
    CHOICES = [('is_open', 'Опубликован'),
               ('is_slug', 'Доступ по ссылке'),
               ('is_for_me', 'Только для меня')]
    choices = forms.ChoiceField(
        label='Публикация',
        choices=CHOICES,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Catalog
        fields = ['title',
                  'cover',
                  'category',
                  'description',
                  'choices'
                  # 'is_open',
                  # 'is_slug',
                  # 'is_for_me',
                  ]

class FilesExpresForms(forms.ModelForm):
    files_s = forms.FileField(
        label='Файл',
        required=False,
        widget= forms.FileInput({'multiple':''})
    )
    class Meta:
        model=FilesExpres
        fields=['files_s']

class FilesCatalogForms(forms.ModelForm):
    files_s = forms.FileField(
        label='Файл',
        required=False,
        widget= forms.FileInput({'multiple':''}))
    class Meta:
        model=FilesCatalog
        fields=['files_s']


class ExpresFilesForms(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput({'class': 'form-control','placeholder': 'Email'})
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea({'class': 'form-control','placeholder': 'Описание'}))
    class Meta:
        model=ExpresFiles
        fields=['email', 'description']

class TestForm(ExpresFilesForms, FilesExpresForms):
    inlineformset_factory = ['email', 'description', 'files_s']

class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        widget=forms.TextInput({'class':'form-control', 'placeholder':'Поиск'})
    )
    field = ['search']

class SearchKey(forms.Form):
    s_key = forms.CharField(
        label='',
        widget=forms.TextInput({'class':'form-control', 'placeholder':'Введите ключ'})
    )
    field = ['s_key']

class AddCatalogForm(CatalogForms, FilesCatalogForms):
    title = forms.CharField(
        label='',
        error_messages='',
        required=True,
        max_length=50,
        widget=forms.TextInput({'class': 'form-control','placeholder': 'Название'})
    )
    category = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        widget=forms.Select({'name':'city', 'id':'city', 'class':'form-control', 'aria-describedby':'basic-amount'})
    )

    description = forms.CharField(
        label='Описание',
        max_length=300,
        widget=forms.Textarea({'class': 'form-control', 'placeholder': 'Описание'}))
    inlineformset_factory = ['title',
                             'cover',
                             'category',
                             'description',
                             'is_open',
                             'is_slug',
                             'is_for_me'
                             'catalog'
                             'forms_s']