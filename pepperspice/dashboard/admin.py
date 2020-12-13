from django.contrib import admin
from .models import Node, Deleted_Node, UserTrait, DBNode, UploadedProject, api_service, credit_card, transaction_messages
admin.site.register(Node)
admin.site.register(Deleted_Node)
admin.site.register(UserTrait)
admin.site.register(DBNode)
admin.site.register(UploadedProject)
admin.site.register(api_service)
admin.site.register(credit_card)
admin.site.register(transaction_messages)