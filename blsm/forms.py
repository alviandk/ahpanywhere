from django import forms
from .models import *

class AHPForm(forms.ModelForm):

    gaji_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control '}))
    gaji_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gaji_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    umur_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    umur_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    umur_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    luas_rumah_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    luas_rumah_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    luas_rumah_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Alternatif
        fields = ('gaji','umur','luas')
        widgets = {

            'gaji':forms.HiddenInput(),
            'umur':forms.HiddenInput(),
            'luas':forms.HiddenInput(),
        }
class AHPKriteriaForm(forms.ModelForm):
    PLANNING_CHOICES_WITH_TITLES = (
        (1./9, 'Mutlak Kurang Penting (1/9)'),
        (1./8, 'Diantara Sangat dan Mutlak Kurang Penting (1/8)'),
        (1./7, 'Sangat Kurang Penting (1/7)'),
        (1./6, 'Diantara Kurang dan Sangat Kurang Penting (1/6)'),
        (1./5, 'Kurang Penting (1/5)'),
        (1./4, 'Diantara Kurang Cukup dan Kurang Penting (1/4)'),
        (1./3, 'Kurang Cukup Penting (1/3)'),
        (1./2, 'Diantara Sama dan Kurang Cukup Penting (1/2)'),
        (1.0, 'Sama Penting (1)'),
        (2.0, 'Diantara Sama dan Cukup Penting (2)'),
        (3.0, 'Cukup Penting (3)'),
        (4.0, 'Diantara Cukup dan Lebih Penting (4)'),
        (5.0, 'Lebih Penting (5)'),
        (6.0, 'Diantara Lebih dan Sangat Lebih Penting (6)'),
        (7.0, 'Sangat Lebih Penting (7)'),
        (8.0, 'Diantara Sangat dan Mutlak Lebih Penting (8)'),
        (9.0, 'Mutlak Lebih Penting (9)'),
    )


    kriteria_umur_gaji=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kriteria_umur_luas=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kriteria_gaji_luas=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    class Meta:
        model = Alternatif
        fields = ('kri',)
        widgets = {
            'kri':forms.HiddenInput(),
        }

