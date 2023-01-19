import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='User nickname')),
                ('rating', models.IntegerField(default=0, verbose_name='User rating')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Tag name')),
                ('count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='References number')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='User nickname')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Question title')),
                ('text', models.TextField(verbose_name='Question text')),
                ('rating', models.IntegerField(db_index=True, default=0, verbose_name='Diff between like and dislike')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is published question')),
                ('pub_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Publication time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Questions', to='app.Profile', verbose_name='Question author')),
                ('dislike', models.ManyToManyField(blank=True, related_name='Questions_dislikes', to='app.Profile', verbose_name='Dislikes')),
                ('like', models.ManyToManyField(blank=True, related_name='Questions_likes', to='app.Profile', verbose_name='Likes')),
                ('tags', models.ManyToManyField(blank=True, related_name='Questions', to='app.Tag', verbose_name='Question tags')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Answer text')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is correct answer')),
                ('rating', models.IntegerField(default=0, verbose_name='Diff between like and dislike')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is published answer')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Answers', to='app.Profile', verbose_name='Question')),
                ('dislike', models.ManyToManyField(blank=True, related_name='Answers_dislikes', to='app.Profile', verbose_name='Dislikes')),
                ('like', models.ManyToManyField(blank=True, related_name='Answers_likes', to='app.Profile', verbose_name='Likes')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Answers', to='app.Question', verbose_name='Question')),
            ],
        ),
    ]
