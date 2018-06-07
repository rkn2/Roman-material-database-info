# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bibliography(models.Model):
    bibliography_id = models.AutoField(primary_key=True)
    bib_no = models.IntegerField(blank=True, null=True)
    full_citation = models.TextField(blank=True, null=True)
    page_range = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_citation


'''
class Citation(models.Model):
    citation_id = models.AutoField(primary_key=True)
    bibliography = models.ForeignKey(Bibliography, models.DO_NOTHING, blank=True, null=True)
    place_marker = models.CharField(max_length=50, blank=True, null=True)
    page_range = models.TextField(blank=True, null=True)
    classical_identifier = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
'''


class CitationStone(models.Model):
    citation_stone_id = models.AutoField(primary_key=True)
    bibliography = models.ForeignKey(Bibliography, models.DO_NOTHING, blank=True, null=True)
    stone = models.ForeignKey('Stones', models.DO_NOTHING, blank=True, null=True)
    supports = models.TextField(blank=True, null=True)
    stone_attribute = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)



class CitationTree(models.Model):
    citation_tree_id = models.AutoField(primary_key=True)
    bibliography = models.ForeignKey(Bibliography, models.DO_NOTHING, blank=True, null=True)
    tree = models.ForeignKey('Trees', models.DO_NOTHING, blank=True, null=True)
    supports = models.TextField(blank=True, null=True)
    tree_attribute = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)



class Stones(models.Model):
    name = models.TextField(blank=True, null=True)
    alternate_name = models.TextField(blank=True, null=True)
    petrographic_details = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    appearance = models.TextField(blank=True, null=True)
    poisson_ratio = models.FloatField(blank=True, null=True)
    absorption = models.FloatField(blank=True, null=True)
    quarry_location = models.TextField(blank=True, null=True)
    archaeological_sources = models.TextField(blank=True, null=True)
    primary_sources = models.TextField(blank=True, null=True)
    secondary_sources = models.TextField(blank=True, null=True)
    shapefile = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)
    dates_of_use = models.TextField(blank=True, null=True)
    density_avg = models.FloatField(blank=True, null=True)
    density_low = models.FloatField(blank=True, null=True)
    density_high = models.FloatField(blank=True, null=True)
    elastic_modulus_average = models.FloatField(blank=True, null=True)
    elastic_modulus_low = models.FloatField(blank=True, null=True)
    elastic_modulus_high = models.FloatField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    rupture_modulus_average = models.FloatField(blank=True, null=True)
    rupture_modulus_low = models.FloatField(blank=True, null=True)
    rupture_modulus_high = models.FloatField(blank=True, null=True)
    compressive_strength_average = models.FloatField(blank=True, null=True)
    compressive_strength_low = models.FloatField(blank=True, null=True)
    compressive_strength_high = models.FloatField(blank=True, null=True)


    def __str__(self):
        return self.name


class Trees(models.Model):
    common_name = models.TextField(blank=True, null=True)
    sci_name = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    tree_rad_low = models.FloatField(blank=True, null=True)
    tree_rad_high = models.FloatField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    janka_hardness = models.FloatField(blank=True, null=True)
    rupture_modulus = models.FloatField(blank=True, null=True)
    elastic_modulus = models.FloatField(blank=True, null=True)
    crushing_strength = models.FloatField(blank=True, null=True)
    shrink_rad = models.FloatField(blank=True, null=True)
    shrink_tan = models.FloatField(blank=True, null=True)
    shrink_volumetric = models.FloatField(blank=True, null=True)
    rot_resistance = models.TextField(blank=True, null=True)
    workability = models.TextField(blank=True, null=True)
    common_uses = models.TextField(blank=True, null=True)
    primary_sources = models.TextField(blank=True, null=True)
    archaeological_sources = models.TextField(blank=True, null=True)
    shapefile = models.TextField(blank=True, null=True)  # This field type is a guess.
    secondary_sources = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tree_height_low = models.FloatField(blank=True, null=True)
    tree_height_high = models.FloatField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.common_name
