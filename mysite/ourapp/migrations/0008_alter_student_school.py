# Generated by Django 3.2.2 on 2021-05-12 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0007_alter_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='School',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourapp.school'),
        ),
    ]
