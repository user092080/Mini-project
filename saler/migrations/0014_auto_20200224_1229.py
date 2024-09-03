

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0013_product_gst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gst',
            field=models.CharField(choices=[('0', '0'), ('3', '3'), ('5', '5'), ('12', '12'), ('18', '18'), ('28', '28')], default='5', max_length=3),
        ),
    ]
