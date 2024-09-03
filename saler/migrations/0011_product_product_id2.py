

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0010_auto_20200220_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id2',
            field=models.CharField(default='', max_length=100),
        ),
    ]
