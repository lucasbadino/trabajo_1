# Generated by Django 4.1 on 2022-09-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='text',
            new_name='comentario',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='notifications',
            new_name='notificaciones',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='query',
        ),
        migrations.AddField(
            model_name='contact',
            name='tipo_de_consulta',
            field=models.IntegerField(blank=True, choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'reseña']], null=True),
        ),
    ]
