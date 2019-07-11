# Generated by Django 2.2.2 on 2019-06-17 10:10

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields
import response.slack.models.workflow


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', slack.models.workflow.EncryptedField(blank=True, field_type=django.db.models.fields.CharField, max_length=500, null=True)),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='slack.Workflow')),
            ],
        ),
    ]
