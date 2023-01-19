from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static/img/avatar_1.jpg', upload_to='static/img/avatars'),
        ),
    ]
