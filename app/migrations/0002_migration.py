from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_migration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
    ]
