from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ("documents", "1068_alter_document_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="savedview",
            name="show_only_if_populated",
            field=models.BooleanField(
                verbose_name="Show only if populated",
                default=False,
            ),
        ),
    ]
