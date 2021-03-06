# Generated by Django 3.2.3 on 2021-12-01 11:04

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('source', models.CharField(max_length=1000)),
                ('source_cat', models.CharField(choices=[('entertainment', 'Entertainment'), ('gaming', 'Gaming'), ('fashionandbeauty', 'Fashionandbeauty'), ('sports', 'Sports'), ('vlogs', 'Vlogs'), ('education', 'Education')], default='entertainment', max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='draft', max_length=28)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Trends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('link', models.CharField(max_length=1000)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('body', models.TextField()),
                ('source', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('choice', models.CharField(choices=[('national', 'National'), ('international', 'International')], default='national', max_length=13)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64, unique_for_date='publish')),
                ('name1', models.CharField(max_length=580)),
                ('image1', models.FileField(upload_to='images/')),
                ('link1', models.CharField(max_length=256)),
                ('rprice1', models.IntegerField()),
                ('oprice1', models.IntegerField()),
                ('off1', models.IntegerField()),
                ('company1', models.CharField(choices=[('flipkart', 'FlipKart'), ('amazon', 'Amazon'), ('ajio', 'Ajio'), ('myntra', 'Myntra'), ('ebay', 'Ebay'), ('puma', 'Puma'), ('adidas', 'Adidas'), ('tatacliq', 'TataCliq')], default='amazon', max_length=64)),
                ('product1', models.CharField(choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('others', 'Others'), ('sports', 'Sports')], default='fashion', max_length=64)),
                ('name2', models.CharField(blank=True, max_length=580, null=True)),
                ('image2', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link2', models.CharField(blank=True, max_length=256, null=True)),
                ('rprice2', models.IntegerField(blank=True, null=True)),
                ('oprice2', models.IntegerField(blank=True, null=True)),
                ('off2', models.IntegerField(blank=True, null=True)),
                ('company2', models.CharField(blank=True, choices=[('flipkart', 'FlipKart'), ('amazon', 'Amazon'), ('ajio', 'Ajio'), ('myntra', 'Myntra'), ('ebay', 'Ebay'), ('puma', 'Puma'), ('adidas', 'Adidas'), ('tatacliq', 'TataCliq')], default='amazon', max_length=64, null=True)),
                ('product2', models.CharField(blank=True, choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('others', 'Others'), ('sports', 'Sports')], default='fashion', max_length=64, null=True)),
                ('name3', models.CharField(blank=True, max_length=580, null=True)),
                ('image3', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link3', models.CharField(blank=True, max_length=256, null=True)),
                ('rprice3', models.IntegerField(blank=True, null=True)),
                ('oprice3', models.IntegerField(blank=True, null=True)),
                ('off3', models.IntegerField(blank=True, null=True)),
                ('company3', models.CharField(blank=True, choices=[('flipkart', 'FlipKart'), ('amazon', 'Amazon'), ('ajio', 'Ajio'), ('myntra', 'Myntra'), ('ebay', 'Ebay'), ('puma', 'Puma'), ('adidas', 'Adidas'), ('tatacliq', 'TataCliq')], default='amazon', max_length=64, null=True)),
                ('product3', models.CharField(blank=True, choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('others', 'Others'), ('sports', 'Sports')], default='fashion', max_length=64, null=True)),
                ('name4', models.CharField(blank=True, max_length=500, null=True)),
                ('image4', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link4', models.CharField(blank=True, max_length=256, null=True)),
                ('rprice4', models.IntegerField(blank=True, null=True)),
                ('oprice4', models.IntegerField(blank=True, null=True)),
                ('off4', models.IntegerField(blank=True, null=True)),
                ('company4', models.CharField(blank=True, choices=[('flipkart', 'FlipKart'), ('amazon', 'Amazon'), ('ajio', 'Ajio'), ('myntra', 'Myntra'), ('ebay', 'Ebay'), ('puma', 'Puma'), ('adidas', 'Adidas'), ('tatacliq', 'TataCliq')], default='amazon', max_length=64, null=True)),
                ('product4', models.CharField(blank=True, choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('others', 'Others'), ('sports', 'Sports')], default='fashion', max_length=64, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=28)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
    ]
