# Generated by Django 5.1.6 on 2025-02-19 15:14
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('complaints', '0002_complaint_email_complaint_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.AddField(
            model_name='complaint',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='complaints/'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='is_urgent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaint',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='priority',
            field=models.CharField(choices=[('HI', 'High'), 
                                            ('ME', 'Medium'),
                                              ('LO', 'Low')],
                                             default='ME', max_length=2),
        ),
        migrations.AddField(
            model_name='complaint',
            name='resolution',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='resolved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='resolved_by',
            field=models.ForeignKey(blank=True, null=True,
             on_delete=django.db.models.deletion.SET_NULL,
            related_name='resolved_complaints', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complaint',
            name='status_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(blank=True, null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='StatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, 
                                           primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('old_status', models.CharField(choices=[('PE', 'Pending'),
                                                        ('RE', 'Resolved'), 
                                                        ('IP', 'In Progress')],
                                                          max_length=2)),
                ('new_status', models.CharField(choices=[('PE', 'Pending'), 
                                                         ('RE', 'Resolved'),
                                                           ('IP', 'In Progress')],
                                                             max_length=2)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, 
                                                to='complaints.complaint')),
            ],
        ),
    ]
