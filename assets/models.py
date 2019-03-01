from django.db import models

# Create your models here.

class Asset(models.Model):
    asset_type_choice = (
        ('server','服务器'),
        ('networkdevice','网络设备'),
        ('storagedevice','存储设备'),
        ('securitydevice','安全设备'),
        ('software','软件资产'),
    )

    asset_status = (
        (0,'在线'),
        (1,'下线'),
        (2,'未知'),
        (3,'故障'),
        (4,'备用'),
    )

    asset_type = models.CharField(choices=asset_type_choice,max_length=64,default='server',verbose_name='资产类型')
    name = models.CharField('资产名称',max_length=64,unique=True)
    sn = models.CharField('资产序列号',max_length=128,unique=True)
    business_unit = models.ForeignKey(BusinessUnit,null=True,blank=True,verbose_name='所属业务线')
    status = models.SmallIntegerField(choices=asset_status,default=0,verbose_name='设备状态')
    manufacture = models.ForeignKey(Manufacturer,null=True,blank=True,verbose_name='制造商')
    manage_ip = models.IPAddressField
