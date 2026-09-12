import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contracts',
            name='logged_at',
        ),
        migrations.RemoveField(
            model_name='contracts',
            name='logged_by',
        ),
        migrations.AddField(
            model_name='contracts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contracts',
            name='created_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contracts',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contracts',
            name='updated_by',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
