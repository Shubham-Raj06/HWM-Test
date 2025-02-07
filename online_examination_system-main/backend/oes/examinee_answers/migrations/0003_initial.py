# Generated by Django 5.0.3 on 2024-03-04 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('examinee_answers', '0002_initial'),
        ('questions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='examineeanswer',
            name='examinee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examineeanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question'),
        ),
        migrations.AddField(
            model_name='flag',
            name='examinee_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examinee_answers.examineeanswer'),
        ),
    ]
