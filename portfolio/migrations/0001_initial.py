# Generated by Django 4.2.4 on 2023-08-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=245)),
                ('subject', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Infos',
            },
        ),
        migrations.CreateModel(
            name='PDFDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
