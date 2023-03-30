from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='Questions_dislikes', to='app.Profile'),
        ),
        migrations.AlterField(
            model_name='question',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='Questions_likes', to='app.Profile'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='app.Tag'),
        ),
    ]
