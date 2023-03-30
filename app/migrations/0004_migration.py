from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='app.Tag'),
        ),
    ]
