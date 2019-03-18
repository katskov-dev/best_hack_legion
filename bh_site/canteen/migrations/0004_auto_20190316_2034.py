# Generated by Django 2.0 on 2019-03-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0003_auto_20190316_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название катогории')),
                ('image', models.ImageField(null=True, upload_to='static/', verbose_name='картинка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='DishModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('calories', models.IntegerField(verbose_name='калории')),
                ('proteins', models.IntegerField(verbose_name='белки')),
                ('fats', models.IntegerField(verbose_name='жиры')),
                ('carbohydrates', models.IntegerField(verbose_name='углеводы')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('mass', models.IntegerField(verbose_name='вес')),
                ('description', models.TextField(max_length=100, verbose_name='описание')),
                ('image', models.ImageField(null=True, upload_to='static/', verbose_name='картинка')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.AlterModelOptions(
            name='canteenmodel',
            options={'permissions': (('edit_canteen', 'Edit Canteen'),), 'verbose_name': 'Столовая', 'verbose_name_plural': 'Столовые'},
        ),
        migrations.AlterField(
            model_name='canteenmodel',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название столовой'),
        ),
        migrations.AddField(
            model_name='dishmodel',
            name='canteen',
            field=models.ForeignKey(null=True, on_delete=False, to='canteen.CanteenModel', verbose_name='столовая'),
        ),
        migrations.AddField(
            model_name='dishmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=False, to='canteen.CategoryModel', verbose_name='категория'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='canteen',
            field=models.ForeignKey(on_delete=False, to='canteen.CanteenModel', verbose_name='столовая'),
        ),
    ]