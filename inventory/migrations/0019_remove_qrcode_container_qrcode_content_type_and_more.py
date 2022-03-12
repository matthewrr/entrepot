# Generated by Django 4.0.3 on 2022-03-12 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('inventory', '0018_remove_item_container_fixture_content_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='container',
        ),
        migrations.AddField(
            model_name='qrcode',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'inventory'), ('model', 'container')), models.Q(('app_label', 'inventory'), ('model', 'item')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qrcode',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]