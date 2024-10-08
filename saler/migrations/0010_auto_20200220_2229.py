

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0009_auto_20200219_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='buyer_gender',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_l',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_l_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_m',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_m_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_s',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_s_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_xl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_xl_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_xxl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_xxl_quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField(default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saler.Product')),
            ],
        ),
    ]
