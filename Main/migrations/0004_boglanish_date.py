# Generated by Django 4.0.4 on 2022-06-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_section_text_en_alter_section_text_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boglanish',
            name='date',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
