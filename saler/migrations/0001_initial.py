

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('sub_Categories', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SalerDetail',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(default='default.png', upload_to='user_photos')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('gst_Number', models.CharField(max_length=15, null=True)),
                ('shop_Name', models.CharField(max_length=500, null=True)),
                ('alternate_mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('shop_Address', models.TextField()),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('landmark', models.CharField(blank=True, max_length=500, null=True)),
                ('locality', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=50, null=True)),
                ('account_Holder_Name', models.CharField(max_length=50, null=True)),
                ('account_Number', models.CharField(max_length=20, null=True)),
                ('ifsc_Code', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellerSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('image', models.ImageField(upload_to='seller_slider_img')),
                ('url', models.CharField(default='#', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WholeSaleProduct',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.TextField()),
                ('size', models.TextField(verbose_name='Size Avialabe(Separated by Comma)')),
                ('color', models.TextField(verbose_name='Enter Color Separated by Comma')),
                ('min_Quantity', models.IntegerField(default=0, null=True)),
                ('pub_date', models.DateField(auto_now=True)),
                ('image1', models.ImageField(default='', null=True, upload_to='products/images')),
                ('image2', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image3', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image4', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image5', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='saler.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('shop', models.CharField(default='', max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('buyer_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('All', 'All')], default='All', max_length=6)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.TextField()),
                ('size_s', models.BooleanField(default=False, verbose_name='Small')),
                ('size_s_quantity', models.IntegerField(default=0, null=True, verbose_name='Quantity')),
                ('size_l', models.BooleanField(default=False, verbose_name='Large')),
                ('size_l_quantity', models.IntegerField(default=0, null=True, verbose_name='Quantity')),
                ('size_xl', models.BooleanField(default=False, verbose_name='XL')),
                ('size_xl_quantity', models.IntegerField(default=0, null=True, verbose_name='Quantity')),
                ('size_xxl', models.BooleanField(default=False, verbose_name='XXL')),
                ('size_xxl_quantity', models.IntegerField(default=0, null=True, verbose_name='Quantity')),
                ('pub_date', models.DateField(auto_now=True)),
                ('image1', models.ImageField(default='', null=True, upload_to='products/images')),
                ('image2', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image3', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image4', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image5', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='saler.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('number', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='dow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('product', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='saler.Product', verbose_name='Product Id')),
            ],
        ),
    ]
