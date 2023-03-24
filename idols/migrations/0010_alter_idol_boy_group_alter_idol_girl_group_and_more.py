# Generated by Django 4.1.7 on 2023-03-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0009_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idol',
            name='Boy_group',
            field=models.CharField(blank=True, choices=[('AB6IX', 'AB6IX'), ('AKMU', 'AKMU'), ('BTOB', 'BTOB'), ('BTS', 'BTS'), ('DAY_6', 'DAY6'), ('EXO', 'EXO'), ('HIGH_LIGHT', 'HIGH_LIGHT')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='idol',
            name='Girl_group',
            field=models.CharField(blank=True, choices=[('AKMU', 'AKMU'), ('ASEPA', 'ASEPA'), ('BILLLIE', 'BILLLIE'), ('BLACKPINK', 'BLACKPINK'), ('BRAVEGIRLS', 'BRAVEGIRLS'), ('CELEBFIVE', 'CELEBFIVE'), ('CHERRY-BULLET', 'CHERRY-BULLET'), ('CHOBOM', 'CHOBOM'), ('CLASSY', 'CLASSY'), ('DAVICHI', 'DAVICHI'), ('EXID', 'EXID'), ('FROMIS_9', 'FROMIS_9'), ('GIDLE', 'GIDLE'), ('ITZY', 'ITZY')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
