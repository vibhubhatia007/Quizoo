# Generated by Django 3.1.1 on 2020-10-16 17:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0013_auto_20201016_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correctoptions',
            name='option',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='options',
            name='option',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
