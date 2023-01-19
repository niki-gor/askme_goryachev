from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_migration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerManager',
        ),
        migrations.DeleteModel(
            name='QuestionManager',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='is_published',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='is_published',
            new_name='is_active',
        ),
    ]
