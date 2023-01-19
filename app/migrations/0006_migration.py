from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dislike',
            field=models.ManyToManyField(related_name='Questions_dislikes', to='app.Profile', verbose_name='Dislikes'),
        ),
        migrations.AlterField(
            model_name='question',
            name='like',
            field=models.ManyToManyField(related_name='Questions_likes', to='app.Profile', verbose_name='Likes'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='Questions', to='app.Tag', verbose_name='Question tags'),
        ),
    ]
