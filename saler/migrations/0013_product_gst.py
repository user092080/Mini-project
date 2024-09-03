

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0012_auto_20200221_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gst',
            field=models.CharField(choices=[('5', '5'), ('12', '12'), ('18', '18'), ('28', '28')], default='5', max_length=3),
        ),
    ]
