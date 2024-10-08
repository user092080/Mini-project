

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0015_auto_20200224_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='size',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='products',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='', max_length=15),
        ),
    ]
