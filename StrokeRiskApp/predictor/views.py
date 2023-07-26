from django.http import HttpResponse
from django.template import loader
from predictor.forms import StrokeRiskForm
from predictor.forms import StrokeRisk
from predictor.apps import PredictorConfig
import numpy as np

# Create your views here.

def home(request):
    template = loader.get_template("predictor/home.html")
    form = StrokeRiskForm()
    context = {'form': form}

    return HttpResponse(template.render(context, request))

def predict(request):

    if request.method == 'POST':
        form = StrokeRiskForm(request.POST)
        context = {
            "form": form,
        }

        if form.is_valid():
            age = float(form.cleaned_data.get('age'))
            gender = form.cleaned_data.get('gender')
            smoking_status = form.cleaned_data.get('smoking_status')
            hypertension = form.cleaned_data.get('hypertension')
            heart_disease = form.cleaned_data.get('heart_disease')
            avg_glucose_level = float(form.cleaned_data.get('avg_glucose_level'))
            bmi = float(form.cleaned_data.get('bmi'))

            gender_Male = 0
            gender_Female = 0
            gender_Other = 0
            if(gender == "Male"):
                gender_Male = 1
                gender_Female = 0
                gender_Other = 0
            elif(gender == "Female"):
                gender_Male = 0
                gender_Female = 1
                gender_Other = 0
            else:
                gender_Male = 0
                gender_Female = 0
                gender_Other = 1

            smoking_status_Unknown = 0
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_smokes = 0
            if(smoking_status == "formerly smoked"):
                smoking_status_Unknown = 0
                smoking_status_formerly_smoked = 1
                smoking_status_never_smoked = 0
                smoking_status_smokes = 0
            elif(smoking_status == "never smoked"):
                smoking_status_Unknown = 0
                smoking_status_formerly_smoked = 0
                smoking_status_never_smoked = 1
                smoking_status_smokes = 0
            elif(smoking_status == "smokes"):
                smoking_status_Unknown = 0
                smoking_status_formerly_smoked = 0
                smoking_status_never_smoked = 0
                smoking_status_smokes = 1
            else:
                smoking_status_Unknown = 1
                smoking_status_formerly_smoked = 0
                smoking_status_never_smoked = 0
                smoking_status_smokes = 0

            features = np.array([age, hypertension, heart_disease, avg_glucose_level, bmi,
                                 gender_Female, gender_Male, gender_Other,
                                 smoking_status_Unknown, smoking_status_formerly_smoked,
                                 smoking_status_never_smoked, smoking_status_smokes])
            
            prediction = PredictorConfig.model.predict(features.reshape(1, -1))[0]
            if(prediction):
                message = "You are at risk of having a stroke."

            else:
                message = "You are not at risk of having a stroke."

            context = {
                'form': form,
                'message': message,
            }

    template = loader.get_template("predictor/home.html")

    return HttpResponse(template.render(context, request))
            
