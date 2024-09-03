

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0006_auto_20200218_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dow',
            name='product',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='saler.Product', verbose_name='Product Id'),
        ),
        migrations.AlterField(
            model_name='trend',
            name='product',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='saler.Product'),
        ),
    ]
