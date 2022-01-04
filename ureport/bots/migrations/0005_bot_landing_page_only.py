# Generated by Django 3.2.8 on 2021-11-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bots", "0004_alter_bot_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="bot",
            name="landing_page_only",
            field=models.BooleanField(
                default=False, help_text="Whether this bot is hidden on public pages except landing pages"
            ),
        ),
    ]