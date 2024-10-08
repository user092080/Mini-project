

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Delivered', 'Delivered')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='saler',
            field=models.CharField(default='wrappers@admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
