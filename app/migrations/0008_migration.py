import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='like',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='question',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='question',
            name='like',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='count',
        ),
        migrations.AddField(
            model_name='answer',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='answer_dislikes', to='app.Profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='answer_likes', to='app.Profile'),
        ),
        migrations.AddField(
            model_name='question',
            name='answers_number',
            field=models.IntegerField(db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='question',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='question_dislikes', to='app.Profile'),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='question_likes', to='app.Profile'),
        ),
        migrations.AddField(
            model_name='tag',
            name='references_num',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
