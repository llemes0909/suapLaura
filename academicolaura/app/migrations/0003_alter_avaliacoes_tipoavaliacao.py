# Generated by Django 4.2.5 on 2023-09-22 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_disciplina_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacoes',
            name='tipoavaliacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoavaliacao'),
        ),
    ]