# Generated by Django 5.0.6 on 2024-07-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(choices=[('Toyota', 'TOYOTA'), ('Volkswagen', 'VOLKSWAGEN'), ('Ford', 'FORD'), ('Honda', 'HONDA'), ('Chevrolet', 'CHEVROLET'), ('Nissan', 'NISSAN'), ('Hyundai', 'HYUNDAI'), ('Mercedes-Benz', 'MERCEDES_BENZ'), ('BMW', 'BMW'), ('Audi', 'AUDI'), ('Kia', 'KIA'), ('Mazda', 'MAZDA'), ('Subaru', 'SUBARU'), ('Lexus', 'LEXUS'), ('Peugeot', 'PEUGEOT'), ('Fiat', 'FIAT'), ('Mitsubishi', 'MITSUBISHI'), ('Jeep', 'JEEP'), ('Suzuki', 'SUZUKI'), ('RAM', 'RAM'), ('Porsche', 'PORSCHE'), ('Land Rover', 'LAND_ROVER'), ('Jaguar', 'JAGUAR'), ('Cadillac', 'CADILLAC'), ('Chrysler', 'CHRYSLER'), ('Tesla', 'TESLA')], max_length=100),
        ),
    ]
