

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0014_auto_20200224_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gst',
            field=models.CharField(choices=[('0', '0'), ('3', '3'), ('5', '5'), ('12', '12'), ('18', '18'), ('28', '28')], default='0', max_length=3),
        ),
    ]
