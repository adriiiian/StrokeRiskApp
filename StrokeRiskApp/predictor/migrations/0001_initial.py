# Generated by Django 4.2.3 on 2023-07-26 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StrokeRisk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=6)),
                ('smoking_status', models.CharField(choices=[('formerly smoked', 'formerly smoked'), ('never smoked', 'never smoked'), ('smokes', 'smokes'), ('Unknown', 'Unknown')], default='Unknown', max_length=15)),
                ('hypertension', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('heart_disease', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('avg_glucose_level', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, validators=[django.core.validators.MinValueValidator(0.1)])),
                ('bmi', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, validators=[django.core.validators.MinValueValidator(0.1)])),
            ],
        ),
    ]
