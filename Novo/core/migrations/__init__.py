from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('ingredientes', models.CharField(max_length=300)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('email', models.EmailField(default=None, max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('regiao', models.CharField(max_length=20)),
            ],
        ),

        migrations.CreateModel(
            name='Indicacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao2', models.TextField()),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
    ]