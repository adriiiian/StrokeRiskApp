from django.forms import ModelForm
from predictor.models import StrokeRisk
from django import forms

class StrokeRiskForm(ModelForm):
    class Meta:
        model = StrokeRisk
        fields = ('age', 'gender', 'smoking_status', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi')
        
        labels = {
            'age': 'Age: ',
            'gender': 'Gender: ',   
            'smoking_status': 'Smoking Status: ',
            'hypertension': 'Has Hypertension: ',
            'heart_disease': 'Has Heart disease: ',
            'avg_glucose_level': 'Average Glucose Level: ',
            'bmi': 'BMI (Body Mass Index): '
        }

        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'id':'age'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'smoking_status': forms.Select(attrs={'class': 'form-control', 'id': 'smoking_status'}),
            'hypertension': forms.Select(attrs={'class': 'form-control', 'id': 'hypertension'}),
            'heart_disease': forms.Select(attrs={'class': 'form-control', 'id': 'heart_disease'}),
            'avg_glucose_level': forms.NumberInput(attrs={'class': 'form-control', 'id': 'avg_glucose_level'}),
            'bmi': forms.NumberInput(attrs={'class': 'form-control', 'id': 'bmi'})
        }