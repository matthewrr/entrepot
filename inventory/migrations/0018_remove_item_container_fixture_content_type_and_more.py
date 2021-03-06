# Generated by Django 4.0.3 on 2022-03-12 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('inventory', '0017_alter_container_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='container',
        ),
        migrations.AddField(
            model_name='fixture',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'inventory'), ('model', 'room')), models.Q(('app_label', 'inventory'), ('model', 'building')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'inventory'), ('model', 'fixture')), models.Q(('app_label', 'inventory'), ('model', 'room')), models.Q(('app_label', 'inventory'), ('model', 'building')), models.Q(('app_label', 'inventory'), ('model', 'container')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='item',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
