from django.db import models
from authentication.models import CustomUser
import datetime
from django.utils import timezone
from datetime import datetime
import uuid

class UploadedProject(models.Model):
    user_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    owner_email = models.EmailField(default='')
    email_to_report = models.EmailField(default='')
    Date_Uploaded = models.DateTimeField(default=datetime.now())
    file_uuid = models.CharField(max_length=128, default='')
    file_name = models.CharField(max_length=128, default='')
    file_system_name = models.CharField(max_length=256, default='')
    file_type = models.CharField(max_length=16, default='')
    file_size = models.CharField(max_length=256, default='')
    linked_to_node_uuid = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.owner_email
        

class Purchases(models.Model):
    user_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(default='')
    purchase_id = models.CharField(max_length=256, default='')
    
class api_service(models.Model):
    user_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    owner_email = models.EmailField(default='')
    email_to_report = models.EmailField(default='')
    date_created = models.DateTimeField(default=datetime.now())
    aws_account_id = models.CharField(max_length=12, default='')
    aws_access_key = models.CharField(max_length=22, default='')
    aws_secret_key = models.CharField(max_length=40, default='')
    api_id = models.CharField(max_length=20, default='')
    cloud_provider = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.owner_email

class UserTrait(models.Model):
    user_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(default='', unique=True)
    unique_id = models.CharField(max_length=64, default='')
    credit_card_number = models.CharField(max_length=64, default='')
    credit_card_holder_name = models.CharField(max_length=64, default='')
    credit_card_expire_month = models.CharField(max_length=12, default='')
    credit_card_expire_year = models.CharField(max_length=12, default='')
    credit_card_security_code = models.CharField(max_length=64, default='')
    low_nodes_count = models.IntegerField(default=0)
    aws_uid = models.IntegerField(default=0)
    medium_nodes_count = models.IntegerField(default=0)
    high_nodes_count = models.IntegerField(default=0)
    web_app_nodes_active = models.IntegerField(default=0)
    db_nodes_active = models.IntegerField(default=0)
    dbms_username = models.CharField(max_length=64, default='')
    dbms_password = models.CharField(max_length=64, default='')
    dbms_enabled = models.BooleanField(default=False)
    order_price_beginning = models.IntegerField(default=0)
    total_billing_history = models.IntegerField(default=0)
    order_count = models.IntegerField(default=0)
    monthly_billing = models.IntegerField(default=0)
    deleted_nodes_history = models.IntegerField(default=0)


    def __str__(self):
        return self.email


class DBNode(models.Model):
    user_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Email = models.EmailField(default='')
    id_link_color = models.CharField(max_length=10, default='')
    linked_to_node_uuid = models.CharField(max_length=256, default='')
    Status = models.BooleanField(default=True)
    db_hostname = models.CharField(max_length=256, default='')
    Date_Created = models.DateTimeField(default=datetime.now())
    link_status = models.BooleanField(default=True)
    internal_hostname = models.CharField(max_length=64, default='')
    external_hostname = models.CharField(max_length=64, default='')
    db_internal_ip = models.CharField(max_length=64, default='')
    db_external_ip = models.CharField(max_length=64, default='')
    db_name = models.CharField(max_length=256, default='')
    db_username = models.CharField(max_length=128, default='')
    db_password = models.CharField(max_length=128, default='')
    db_port = models.IntegerField(default=0)
    db_uid = models.CharField(max_length=256, default='')
    db_engine = models.CharField(max_length=16, default='')
    db_version = models.CharField(max_length=16, default='')
    db_load_type = models.CharField(max_length=16, default='')

    def __str__(self):
        return self.Email

class Node(models.Model):
    user_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    node_ID = models.CharField(max_length=256, default='')
    id_link_color = models.CharField(max_length=10, default='')
    linked_to_project = models.BooleanField(default=False)
    projet_link_uuid = models.CharField(max_length=64, default='')
    Email = models.EmailField(default='')
    exposed = models.BooleanField(default=False)
    Status = models.BooleanField()
    Name = models.CharField(max_length=32)
    Framework = models.CharField(max_length=32, default='') # Show only if instance is webapp
    Date_Created = models.DateTimeField(default=datetime.now())
    Load_Type = models.CharField(max_length=16, default='')
    link_status = models.BooleanField(default=False)
    server_region = models.CharField(max_length=32, default='')
    order_node_count = models.IntegerField(default=0)
    linked_to_db_uuid = models.CharField(max_length=256, default='')
    is_webapp = models.BooleanField(default=False)
    framework_version = models.CharField(max_length=256, default='')
    IPv4 = models.CharField(max_length=16, default='')
    Private_IPv4 = models.CharField(max_length=16, default='')
    Domain_Name = models.CharField(max_length=128, default='')
    Subdomain = models.CharField(max_length=128, default='')
    Monitoring = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.Email

class Deleted_Node(models.Model):
    node_id = models.CharField(max_length=128 ,default='')
    user_id = models.CharField(max_length=128 ,default='')
    email = models.EmailField(default='')
    instance_type = models.CharField(max_length=16, default='')
    date_deleted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.email
    