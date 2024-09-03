

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0007_auto_20200218_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='', max_length=15),
        ),
    ]
