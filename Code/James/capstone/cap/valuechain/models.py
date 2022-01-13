from django.db import models

class Supplier(models.Model):
    supplierid = models.CharField(max_length=200)
    capacity = models.FloatField(default=0)
    quality = models.FloatField(default=0)
    timeliness = models.FloatField(default=0)
    capacity_ave = models.FloatField(default=0)
    quality_ave = models.FloatField(default=0)
    timeliness_ave = models.FloatField(default=0)
    capacity_stdev = models.FloatField(default=0)
    quality_stdev = models.FloatField(default=0) 
    timeliness_stdev = models.FloatField(default=0)
    item_id = models.CharField(max_length=200, default=0)
    item_value = models.FloatField(default=0)
    
    def __str__(self):
        return self.supplierid

class Manufacturer(models.Model):
    manufacturer_id = models.CharField(max_length=200)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    m_capacity = models.FloatField(default=0)
    m_quality = models.FloatField(default=0)
    m_timeliness = models.FloatField(default=0)
    m_capacity_ave = models.FloatField(default=0)
    m_quality_ave = models.FloatField(default=0)
    m_timeliness_ave = models.FloatField(default=0)
    m_capacity_stdev = models.FloatField(default=0)
    m_quality_stdev = models.FloatField(default=0) 
    m_timeliness_stdev = models.FloatField(default=0)
    agg_sys_id = models.CharField(max_length=200, default=0)
    agg_sys_value = models.FloatField(default=0)

    def __str__(self):
        return self.manufacturer_id

class Customer(models.Model):
    customer_id = models.CharField(max_length=200)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    c_capacity = models.FloatField(default=0)
    c_quality = models.FloatField(default=0)
    c_timeliness = models.FloatField(default=0)
    c_capacity_ave = models.FloatField(default=0)
    c_quality_ave = models.FloatField(default=0)
    c_timeliness_ave = models.FloatField(default=0)
    c_capacity_stdev = models.FloatField(default=0)
    c_quality_stdev = models.FloatField(default=0) 
    c_timeliness_stdev = models.FloatField(default=0)
    c_sys_id = models.CharField(max_length=200, default=0)
    c_sys_value = models.FloatField(default=0)
    split_shipments = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_id