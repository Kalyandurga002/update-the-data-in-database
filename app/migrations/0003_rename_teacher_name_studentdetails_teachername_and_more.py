# Generated by Django 4.1.7 on 2023-04-06 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_studentdetails_contactnumber"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentdetails",
            old_name="teacher_name",
            new_name="teachername",
        ),
        migrations.RenameField(
            model_name="teacherdetails",
            old_name="teacher_id",
            new_name="teacherid",
        ),
        migrations.RenameField(
            model_name="teacherdetails",
            old_name="teacher_name",
            new_name="teachername",
        ),
    ]