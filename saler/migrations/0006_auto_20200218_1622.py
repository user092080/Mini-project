

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0005_trend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='product',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='saler.Product'),
        ),
    ]
