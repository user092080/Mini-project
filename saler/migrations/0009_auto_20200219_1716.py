

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0008_auto_20200218_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_not',
            field=models.IntegerField(default=999),
        ),
        migrations.AddField(
            model_name='product',
            name='size_m',
            field=models.BooleanField(default=False, verbose_name='Medium'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_m_quantity',
            field=models.IntegerField(default=0, null=True, verbose_name='Quantity'),
        ),
    ]
