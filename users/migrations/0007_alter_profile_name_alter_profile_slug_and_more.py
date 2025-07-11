from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_social_twitter_profile_social_telegram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_name',
            field=models.CharField(max_length=50, unique=True, null=False, blank=False),
        ),
    ]
