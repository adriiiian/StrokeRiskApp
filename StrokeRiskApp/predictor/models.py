from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class StrokeRisk(models.Model):
    age = models.IntegerField(validators=[MinValueValidator(0)])
    gender_m = "Male"
    gender_f = "Female"
    gender_o = "Others"
    gender_choices = [
        (gender_m, "Male"),
        (gender_f, "Female"),
        (gender_o, "Others"),
    ]
    gender = models.CharField(max_length=6, choices=gender_choices, default=gender_m)
    ['formerly smoked' 'never smoked' 'smokes' 'Unknown']
    smoke_f = "formerly smoked"
    smoke_n = "never smoked"
    smoke_s = "smokes"
    smoke_u = "Unknown"
    smoke_choices = [
        (smoke_f, "formerly smoked"),
        (smoke_n, "never smoked"),
        (smoke_s, "smokes"),
        (smoke_u, "Unknown"),
    ]
    smoking_status = models.CharField(max_length=15, choices=smoke_choices, default=smoke_u)
    hypertension_choices = [
        (1, "Yes"),
        (0, "No"),
    ]
    hypertension = models.IntegerField(choices=hypertension_choices, default=0)
    heartdisease_choices = [
        (1, "Yes"),
        (0, "No"),
    ]
    heart_disease = models.IntegerField(choices=heartdisease_choices, default=0)
    avg_glucose_level = models.DecimalField(default=0.0, decimal_places=2, max_digits=6, validators=[MinValueValidator(0.1)])
    bmi = models.DecimalField(default=0.0, decimal_places=2, max_digits=6, validators=[MinValueValidator(0.1)])
    # married_y = "Yes"
    # married_n = "No"
    # married_choices = [
    #     (married_y, "Yes"),
    #     (married_n, "No"),
    # ]
    # ever_married = models.CharField(choices=married_choices, default=married_n)

    # work_p = "Private"
    # work_s = "Self-employed"
    # work_g = "Govt_job"
    # work_c = "children"
    # work_n = "Never_worked"
    # work_choices = [
    #     (work_p, "Private"),
    #     (work_s, "Self-employed"),
    #     (work_g, "Govt_job"),
    #     (work_c, "children"),
    #     (work_n, "Never_worked"),
    # ]
    # work_type = models.CharField(choices=work_choices, default=work_n)

