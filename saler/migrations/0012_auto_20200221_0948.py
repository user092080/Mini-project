

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0011_product_product_id2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsize',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
