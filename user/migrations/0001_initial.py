# Generated by Django 2.2.3 on 2019-07-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.CharField(max_length=50, verbose_name='E-Mail')),
                ('password', models.CharField(max_length=50, verbose_name='Şifre')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Ad')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Soyad')),
                ('is_active', models.BooleanField(default=True, verbose_name='Hesap Aktif')),
                ('last_login', models.DateField(auto_now=True, verbose_name='Son Giriş Tarihi')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon Numarası')),
                ('verification_code', models.IntegerField(blank=True, null=True, unique_for_year=True, verbose_name='Doğrulama Kodu')),
                ('image', models.CharField(blank=True, max_length=100, null=True, verbose_name='Profil Fotoğrafı')),
            ],
        ),
    ]
