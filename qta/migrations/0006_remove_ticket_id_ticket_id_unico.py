# Generated by Django 4.2.4 on 2023-09-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qta', '0005_ticket_first_follow_up_ticket_second_follow_up_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='id',
        ),
        migrations.AddField(
            model_name='ticket',
            name='id_unico',
            field=models.IntegerField(default=True, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
