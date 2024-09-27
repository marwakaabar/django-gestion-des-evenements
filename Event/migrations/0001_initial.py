# Generated by Django 4.2 on 2024-09-27 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('category', models.CharField(choices=[('Musique', 'Musique'), ('Cinema', 'Cinema'), ('Sport', 'Sport')], max_length=20)),
                ('state', models.BooleanField(default=False)),
                ('nbr_participants', models.IntegerField(default=0)),
                ('evt_date', models.DateTimeField(null=True)),
                ('creation_date', models.DateField(auto_now=True)),
                ('organisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]