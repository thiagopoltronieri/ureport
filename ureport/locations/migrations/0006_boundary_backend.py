# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-05 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

import time
from ureport.utils import chunk_list, prod_print


def populate_boundary_backend(apps, schema_editor):
    Boundary = apps.get_model("locations", "Boundary")
    Org = apps.get_model("orgs", "Org")

    start = time.time()

    for org in Org.objects.all():
        backend = org.backends.filter(slug="rapidpro").first()
        boundaries_ids = Boundary.objects.filter(org=org).values_list("id", flat=True)

        i = 0

        for batch in chunk_list(boundaries_ids, 1000):
            updated = Boundary.objects.filter(id__in=batch).update(backend=backend)

            i += updated
            prod_print("Processed %d / %d boundaires in %ds" % (i, len(boundaries_ids), time.time() - start))

        prod_print("Finished setting boundaries backend for org %s" % org.name)


class Migration(migrations.Migration):

    dependencies = [("orgs", "0025_auto_20180322_1415"), ("locations", "0005_remove_boundary_backend")]

    operations = [
        migrations.AddField(
            model_name="boundary",
            name="backend",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="orgs.OrgBackend"),
        ),
        migrations.RunPython(populate_boundary_backend),
    ]
