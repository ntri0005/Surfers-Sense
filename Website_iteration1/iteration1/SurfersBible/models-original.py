# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class beach_df_24_04(models.Model):
    beach_address = models.TextField(blank=True, null=True)
    beach_name = models.TextField(blank=True, null=True)
    country_state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    formatted_address = models.TextField(blank=True, null=True)
    location_type = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beach_df_24_04'



class join_weather_tide_df_24_04(models.Model):
    date_beach_address = models.TextField(blank=True, null=True)
    temperature_max = models.FloatField(blank=True, null=True)
    temperature_min = models.FloatField(blank=True, null=True)
    temperature_mean = models.FloatField(blank=True, null=True)
    temperature_median = models.FloatField(blank=True, null=True)
    temperature_std = models.FloatField(blank=True, null=True)
    temperature_var = models.FloatField(blank=True, null=True)
    temperature_sem = models.FloatField(blank=True, null=True)
    apparenttemperature_max = models.FloatField(db_column='apparentTemperature_max', blank=True, null=True)  # Field name made lowercase.
    apparenttemperature_min = models.FloatField(db_column='apparentTemperature_min', blank=True, null=True)  # Field name made lowercase.
    apparenttemperature_mean = models.FloatField(db_column='apparentTemperature_mean', blank=True, null=True)  # Field name made lowercase.
    apparenttemperature_median = models.FloatField(db_column='apparentTemperature_median', blank=True, null=True)  # Field name made lowercase.
    apparenttemperature_std = models.FloatField(db_column='apparentTemperature_std', blank=True, null=True)  # Field name made lowercase.
    apparenttemperature_var = models.FloatField(db_column='apparentTemperature_var', blank=True, null=True)  # Field name made lowercase.
    apparenttemperature_sem = models.FloatField(db_column='apparentTemperature_sem', blank=True, null=True)  # Field name made lowercase.
    dewpoint_max = models.FloatField(db_column='dewPoint_max', blank=True, null=True)  # Field name made lowercase.
    dewpoint_min = models.FloatField(db_column='dewPoint_min', blank=True, null=True)  # Field name made lowercase.
    dewpoint_mean = models.FloatField(db_column='dewPoint_mean', blank=True, null=True)  # Field name made lowercase.
    dewpoint_median = models.FloatField(db_column='dewPoint_median', blank=True, null=True)  # Field name made lowercase.
    dewpoint_std = models.FloatField(db_column='dewPoint_std', blank=True, null=True)  # Field name made lowercase.
    dewpoint_var = models.FloatField(db_column='dewPoint_var', blank=True, null=True)  # Field name made lowercase.
    dewpoint_sem = models.FloatField(db_column='dewPoint_sem', blank=True, null=True)  # Field name made lowercase.
    humidity_max = models.FloatField(blank=True, null=True)
    humidity_min = models.FloatField(blank=True, null=True)
    humidity_mean = models.FloatField(blank=True, null=True)
    humidity_median = models.FloatField(blank=True, null=True)
    humidity_std = models.FloatField(blank=True, null=True)
    humidity_var = models.FloatField(blank=True, null=True)
    humidity_sem = models.FloatField(blank=True, null=True)
    windspeed_max = models.FloatField(db_column='windSpeed_max', blank=True, null=True)  # Field name made lowercase.
    windspeed_min = models.FloatField(db_column='windSpeed_min', blank=True, null=True)  # Field name made lowercase.
    windspeed_mean = models.FloatField(db_column='windSpeed_mean', blank=True, null=True)  # Field name made lowercase.
    windspeed_median = models.FloatField(db_column='windSpeed_median', blank=True, null=True)  # Field name made lowercase.
    windspeed_std = models.FloatField(db_column='windSpeed_std', blank=True, null=True)  # Field name made lowercase.
    windspeed_var = models.FloatField(db_column='windSpeed_var', blank=True, null=True)  # Field name made lowercase.
    windspeed_sem = models.FloatField(db_column='windSpeed_sem', blank=True, null=True)  # Field name made lowercase.
    windbearing_max = models.FloatField(db_column='windBearing_max', blank=True, null=True)  # Field name made lowercase.
    windbearing_min = models.FloatField(db_column='windBearing_min', blank=True, null=True)  # Field name made lowercase.
    windbearing_mean = models.FloatField(db_column='windBearing_mean', blank=True, null=True)  # Field name made lowercase.
    windbearing_median = models.FloatField(db_column='windBearing_median', blank=True, null=True)  # Field name made lowercase.
    windbearing_std = models.FloatField(db_column='windBearing_std', blank=True, null=True)  # Field name made lowercase.
    windbearing_var = models.FloatField(db_column='windBearing_var', blank=True, null=True)  # Field name made lowercase.
    windbearing_sem = models.FloatField(db_column='windBearing_sem', blank=True, null=True)  # Field name made lowercase.
    uvindex_max = models.FloatField(db_column='uvIndex_max', blank=True, null=True)  # Field name made lowercase.
    uvindex_min = models.FloatField(db_column='uvIndex_min', blank=True, null=True)  # Field name made lowercase.
    uvindex_mean = models.FloatField(db_column='uvIndex_mean', blank=True, null=True)  # Field name made lowercase.
    uvindex_median = models.FloatField(db_column='uvIndex_median', blank=True, null=True)  # Field name made lowercase.
    uvindex_std = models.FloatField(db_column='uvIndex_std', blank=True, null=True)  # Field name made lowercase.
    uvindex_var = models.FloatField(db_column='uvIndex_var', blank=True, null=True)  # Field name made lowercase.
    uvindex_sem = models.FloatField(db_column='uvIndex_sem', blank=True, null=True)  # Field name made lowercase.
    cloudcover_max = models.FloatField(db_column='cloudCover_max', blank=True, null=True)  # Field name made lowercase.
    cloudcover_min = models.FloatField(db_column='cloudCover_min', blank=True, null=True)  # Field name made lowercase.
    cloudcover_mean = models.FloatField(db_column='cloudCover_mean', blank=True, null=True)  # Field name made lowercase.
    cloudcover_median = models.FloatField(db_column='cloudCover_median', blank=True, null=True)  # Field name made lowercase.
    cloudcover_std = models.FloatField(db_column='cloudCover_std', blank=True, null=True)  # Field name made lowercase.
    cloudcover_var = models.FloatField(db_column='cloudCover_var', blank=True, null=True)  # Field name made lowercase.
    cloudcover_sem = models.FloatField(db_column='cloudCover_sem', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(blank=True, null=True)
    beach_address = models.TextField(blank=True, null=True)
    beach_name = models.TextField(blank=True, null=True)
    country_state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    height_rise_max = models.FloatField(blank=True, null=True)
    height_rise_min = models.FloatField(blank=True, null=True)
    height_rise_mean = models.FloatField(blank=True, null=True)
    height_rise_median = models.FloatField(blank=True, null=True)
    height_rise_std = models.FloatField(blank=True, null=True)
    height_rise_var = models.FloatField(blank=True, null=True)
    height_rise_sem = models.FloatField(blank=True, null=True)
    height_fall_max = models.FloatField(blank=True, null=True)
    height_fall_min = models.FloatField(blank=True, null=True)
    height_fall_mean = models.FloatField(blank=True, null=True)
    height_fall_median = models.FloatField(blank=True, null=True)
    height_fall_std = models.FloatField(blank=True, null=True)
    height_fall_var = models.FloatField(blank=True, null=True)
    height_fall_sem = models.FloatField(blank=True, null=True)
    height_high_tide_max = models.FloatField(blank=True, null=True)
    height_high_tide_min = models.FloatField(blank=True, null=True)
    height_high_tide_mean = models.FloatField(blank=True, null=True)
    height_low_tide_max = models.FloatField(blank=True, null=True)
    height_low_tide_min = models.FloatField(blank=True, null=True)
    height_low_tide_mean = models.FloatField(blank=True, null=True)
    lat_datum_mean = models.FloatField(db_column='LAT_datum_mean', blank=True, null=True)  # Field name made lowercase.
    hat_datum_mean = models.FloatField(db_column='HAT_datum_mean', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    month_day = models.IntegerField(blank=True, null=True)
    shark_attack_percentage = models.FloatField(blank=True, null=True)
    shark_sighting_percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'join_weather_tide_df_24_04'
