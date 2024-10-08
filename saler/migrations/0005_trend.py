

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0004_auto_20200217_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('product', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='saler.Product', verbose_name='Product Id')),
            ],
        ),
    ]
