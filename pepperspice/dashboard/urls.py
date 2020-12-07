from django.urls import path

from .views import *

urlpatterns = [
    path('', dashboard, name='overview'),
    path('new/db_instance/', new_db_instance, name="new_db_instance"),
    path('new/mikro_instance/', mikro_instance, name="new_db_instance"),
    path('new/web_app/', web_app, name="new_db_instance"),
    path('new/web_app/our/', our_web_app, name="out_new_web_app"),
    path('new/spice_service/', spice_service, name="new_db_instance"),
    path('new/web_app/our/fast/', fast_easy, name="fast_easy"),
    path('new/web_app/our/technical/', technical, name="technical"),
    path('security/profile/', profile, name="profile"),
    path('network/firewall/', firewall, name="firewall"),
    path('network/domains/', domains, name="domains"),
    path('security/monitoring/', monitoring, name="monitoring"),
    path('security/logs/', logs, name="logs"),
    path('security/profile/', profile, name="profile"),
    path('billing/', billing, name='billing'),
    path('new/knot/', new_knot, name="new_knot"),
    path('new/web_app/our/fast/send_data/create_order/', create_order, name='create_order'),
    path('new/web_app/our/fast/send_data/create_node/<name_domain>/', create_node, name='create_order'),
    path('new/web_app/our/fast/send_data/create_node_/technical/<name_domain_subdomain>/', create_node_technical, name='create_node_technical'),
    path('new/node/<str:uuid>&mode=<mode>/', new_node, name='new_node'),
    path('get/data/<node_id>/', get_data, name="get_data"),
    path('get/payment/detail/<user_id>/', get_payment, name='get_payment'),
    path('get/container/data/', get_container_data, name="get_container_data"),
    path('send/delete/container/<id>/', delete_container, name="delete_container"),
    path('send/new/credit_card/', send_credit_card, name='send_credit_card'),
    path('send/data/edit/credit_card/', edit_credit_card, name='edit_credit_card'),
    path('new/db/send_data/create_db/', new_db, name='new_db'),
    path('get/db/<node_id>/', get_db_data, name='get_db_data'),
    path('verify/payment/detail/<user_id>/<request_key>/', verify_request, name='verify_request'),
    path('verify/db_eligibility/', verify_db_eligibility, name='verify_db_eligibility'),
    path('get/container/count/', supply_container_count, name='supply_container_count'),
    path('warehouse/', warehouse, name='warehouse'),
    path('link/file_to_app/', link_file, name='link_file'),
    path('unlink/file_to_app/', unlink_file, name='unlink_file'),
    path('check_duplicate/', check_duplicate, name='check_duplicate'),
    path('delete/file/', delete_file, name="delete_file"),
    path('check_email/', check_email, name="check_email")
]