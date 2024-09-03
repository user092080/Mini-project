

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_size',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
