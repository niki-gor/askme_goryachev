from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='Questions', to='app.Tag', verbose_name='Question tags'),
        ),
    ]
