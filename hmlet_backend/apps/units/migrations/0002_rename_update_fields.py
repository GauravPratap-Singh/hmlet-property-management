from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='units',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='units',
            old_name='update_by',
            new_name='updated_by',
        ),
    ]
