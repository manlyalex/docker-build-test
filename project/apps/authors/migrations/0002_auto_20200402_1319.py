# Generated by Django 3.0.4 on 2020-04-02 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthorsModels',
            new_name='Authors',
        ),
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name': 'Authors', 'verbose_name_plural': 'Authors'},
        ),
    ]