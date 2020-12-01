from django.shortcuts import render, redirect
from authentication.models import CustomUser
from django.conf import settings
from django.utils import timezone
from .models import Node
from authentication.models import CustomUser
from django.http import HttpResponse
from .models import UserTrait      
from .models import DBNode   
import subprocess      
from datetime import datetime
import uuid
import os
import time
import docker
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedProject


@csrf_exempt
def supply_container_count(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if UserTrait.objects.filter(email=request.user).exists():
                    low_nodes_count = UserTrait.objects.filter(email=request.user).first().low_nodes_count
                    medium_nodes_count = UserTrait.objects.filter(email=request.user).first().medium_nodes_count
                    high_nodes_count = UserTrait.objects.filter(email=request.user).first().high_nodes_count
                    return HttpResponse(str(low_nodes_count)+'&'+str(medium_nodes_count)+'&'+str(high_nodes_count))
            else:
                return HttpResponse('false')

def dashboard(request):

    if request.user.is_authenticated:
        node = CustomUser.objects.filter(email=request.user).first()
        node.last_login = datetime.now()
        node.save()
 
        web_app_count = 0
        a = Node.objects.filter(Email=request.user)
        for node in a:
            if len(node.Framework) > 0:
                web_app_count += 1
        
        database_count = 0
        db = DBNode.objects.filter(Email=request.user)
        for database in db:
            database_count += 1 

        if UserTrait.objects.filter(email=request.user).exists():
            dbms_user_name = UserTrait.objects.filter(email=request.user).first().dbms_username
            dbms_user_password = UserTrait.objects.filter(email=request.user).first().dbms_password
            dbms_status = UserTrait.objects.filter(email=request.user).first().dbms_enabled

        else:
            dbms_user_name = 'false'
            dbms_user_password = 'false'
            dbms_status = 'false'

        ready_to_deploy = Node.objects.filter(linked_to_project=True)
        ready_to_deploy_count = 0
        for app in ready_to_deploy:
            ready_to_deploy_count += 1

        return render(request, 'html/spec-comp/dashboard/entrypoint.html', {})
        # return render(request, 'html/spec-comp/dashboard/overview.html', {'instances':Node.objects.filter(Email=request.user), 
        #                                                                     'initials':str(request.user).split('@')[0],
        #                                                                     'webapps':Node.objects.filter(is_webapp=True), 
        #                                                                     # 'dbs': Node.objects.filter(is_db=True),
        #                                                                     'uuid':uuid.uuid4().hex,
        #                                                                     'dbs':DBNode.objects.filter(Email=request.user),
        #                                                                     'webapplications': web_app_count, 
        #                                                                     'databases':database_count,
        #                                                                     'datenow':datetime.now(),
        #                                                                     'ready_to_deploy_count':ready_to_deploy_count,
        #                                                                     'databases_currently':DBNode.objects.filter(Email=request.user).count(),
        #                                                                     'dbms_username':dbms_user_name,
        #                                                                     'dbms_password':dbms_user_password,
        #                                                                     'dbms_status':dbms_status})
    else:
        return redirect('/accounts/login/')

def new_db_instance(request):
    if request.user.is_authenticated:


        global request_key_


        
        if UserTrait.objects.filter(email=request.user).exists():
            
            request_key_ = str(uuid.uuid4())
           
            low_node = UserTrait.objects.filter(email=request.user).first().low_nodes_count
            low_node_status = None
            medium_node = UserTrait.objects.filter(email=request.user).first().medium_nodes_count
            medium_node_status = None
            high_node = UserTrait.objects.filter(email=request.user).first().high_nodes_count
            high_node_status = None
        

            container_end_count = 0

            if low_node == 0:
                low_node_status = 'disabled'
                container_end_count += 1
            if medium_node == 0:
                medium_node_status = 'disabled'
                container_end_count += 1
            if high_node == 0:
                high_node_status = 'disabled'
                container_end_count += 1

            if container_end_count == 3: 
                return render(request, 'html/spec-comp/dashboard/db_instance.html', {'request_key':request_key_,
                                                                                    'user_id':request.user,
                                                                                    'no_low':low_node,
                                                                                    'no_medium':medium_node,
                                                                                    'no_high':high_node, 
                                                                                    'if_disabled_low':low_node_status, 
                                                                                    'if_disabled_medium':medium_node_status,
                                                                                    'internal_hostname': 'localhost',
                                                                                    # 'internal_hostname': str(uuid.uuid4()),
                                                                                    'if_disabled_high':high_node_status,
                                                                                    'applications':Node.objects.filter(Email=request.user),
                                                                                    'number_of_applications':Node.objects.filter(Email=request.user).count()
                                                                                    })
            else:
                return render(request, 'html/spec-comp/dashboard/db_instance.html', {'request_key':request_key_,
                                                                                'user_id':request.user,
                                                                                'no_low':low_node,
                                                                                'no_medium':medium_node,
                                                                                'no_high':high_node, 
                                                                                'if_disabled_low':low_node_status, 
                                                                                'if_disabled_medium':medium_node_status,
                                                                                'internal_hostname': 'localhost',
                                                                                # 'internal_hostname': str(uuid.uuid4()),
                                                                                'if_disabled_high':high_node_status,
                                                                                'applications':Node.objects.filter(Email=request.user),
                                                                                'number_of_applications':Node.objects.filter(Email=request.user).count()
                                                                                })
        
        
        
        
        
        
        
        
        
        
        else:
            request_key_ = 'false'
            return render(request, 'html/spec-comp/dashboard/db_instance.html', {'request_key':request_key_,
                                                                                'user_id':request.user,
                                                                                'no_low':False,
                                                                                'no_medium':False,
                                                                                'no_high':False, 
                                                                                'if_disabled_low':False, 
                                                                                'if_disabled_medium':False,
                                                                                'internal_hostname': 'localhost',
                                                                                # 'internal_hostname': str(uuid.uuid4()),
                                                                                'if_disabled_high':False,
                                                                                'applications':Node.objects.filter(Email=request.user),
                                                                                'number_of_applications':Node.objects.filter(Email=request.user).count()
                                                                                })

    else:
        return redirect('/accounts/login/')

@csrf_exempt
def verify_request(request, user_id, request_key):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request_key_ == request_key:
                if request_key_ == 'false':
                    return HttpResponse('true')
                else:
                    return HttpResponse('match')
            else:
                return HttpResponse('no_match')

@csrf_exempt
def verify_db_eligibility(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if UserTrait.objects.filter(email=request.user).exists():
                return HttpResponse('true')
            else:
                return HttpResponse('false')

def new_db(request):
    if request.user.is_authenticated:
        import random
        if request.method == 'POST':
            
            if not UserTrait.objects.filter(email=request.user).exists():
                return render(request, 'html/spec-comp/dashboard/buy_containers.html', {'message_1':'You appear to not have available containers.', 'message_2':'You can get any number of containers for any need at any time, at the best price.', 'hide_or_not':'dont_hide'})

            else:
                low_node = UserTrait.objects.filter(email=request.user).first().low_nodes_count
                low_node_status = None
                medium_node = UserTrait.objects.filter(email=request.user).first().medium_nodes_count
                medium_node_status = None
                high_node = UserTrait.objects.filter(email=request.user).first().high_nodes_count
                high_node_status = None

                container_end_count = 0

                if low_node == 0:
                    low_node_status = 'disabled'
                    container_end_count += 1
                if medium_node == 0:
                    medium_node_status = 'disabled'
                    container_end_count += 1
                if high_node == 0:
                    high_node_status = 'disabled'
                    container_end_count += 1

                if container_end_count == 3: # If there are is no resource space left
                    return render(request, 'html/spec-comp/dashboard/buy_containers.html', {'message_1':'You appear to not have available containers.', 'message_2':'You can get any number of containers for any need at any time, at the best price.', 'hide_or_not':'dont_hide'})


                color_list = ['red', 'green', 'orange', 'teal', 'violet', 'pink', 'yellow', 'blue', 'purple', 'black']
                random_color = random.choice(color_list)
    
                
                
                    


                class DB_Details():
                    linked_to_app = request.POST.get('linked_node_id')
                    Date_Created = datetime.now()
                    db_name = request.POST.get('db_name_form')
                    db_uid = str((uuid.uuid4().hex)[0:12])
                    username = str((uuid.uuid4().hex)[0:12])
                    password = str((uuid.uuid4().hex)[0:12])  
                    db_engine = request.POST.get('db_engine')
                    db_port = random.randint(4000, 30000)
                    db_version = request.POST.get('db_name_form_version')
                    load_option = request.POST.get('load_type')

                if DB_Details.linked_to_app:
                    link_status = True
                    db_id_link_color= Node.objects.filter(node_ID=DB_Details.linked_to_app).first().id_link_color

                else:
                    link_status = False
                    db_id_link_color= random_color

                if DB_Details.load_option == 'low_load':
                    d = UserTrait.objects.filter(email=request.user).first()
                    d.low_nodes_count = d.low_nodes_count - 1 
                    d.save()
                if DB_Details.load_option == 'medium_load':
                    e = UserTrait.objects.filter(email=request.user).first()
                    e.medium_nodes_count = e.medium_nodes_count - 1 
                    e.save()
                if DB_Details.load_option == 'high_load':
                    f = UserTrait.objects.filter(email=request.user).first()
                    f.high_nodes_count = f.high_nodes_count - 1 
                    f.save()

                if DB_Details.linked_to_app:
                    db = DBNode(user_ID=request.user,
                    Email=request.user,
                    linked_to_node_uuid=DB_Details.linked_to_app,
                    db_hostname=request.POST.get('database_hostname'),
                    Date_Created=DB_Details.Date_Created,
                    link_status=link_status,
                    id_link_color=db_id_link_color,
                    db_name=DB_Details.db_name,
                    db_username=DB_Details.username,
                    db_password=DB_Details.password,
                    db_uid=DB_Details.db_uid,
                    db_engine=DB_Details.db_engine,
                    # db_port=DB_Details.db_port,
                    db_port=3309,
                    db_version=DB_Details.db_version,
                    db_load_type=DB_Details.load_option)
                    db.save()

                    os.system("echo toor | sudo -S docker run -d " + "--name '" + DB_Details.db_uid + "' -e MYSQL_ROOT_PASSWORD=KmQfcsnpdUrrRL2qzE8P --network=net1 mysql")
                    time.sleep(30)             
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"CREATE USER '" + DB_Details.username + "'@'localhost' IDENTIFIED BY '" + DB_Details.password + "';\"")
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"CREATE USER '" + DB_Details.username + "'@'%' IDENTIFIED BY '" + DB_Details.password + "';\"")             
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"CREATE DATABASE " + DB_Details.db_name + ";\"")
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"GRANT ALL ON " + DB_Details.db_name + ".* TO '" + DB_Details.username + "'@'localhost'; FLUSH PRIVILEGES;\"")
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"GRANT ALL ON " + DB_Details.db_name + ".* TO '" + DB_Details.username + "'@'%'; FLUSH PRIVILEGES;\"")

                    a = DBNode.objects.filter(db_uid=DB_Details.db_uid).first()
                    a.db_internal_ip = os.popen("echo toor | sudo -S docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' " + DB_Details.db_uid).read().strip()
                    a.save()
                    
                    
                    return HttpResponse('success')
            #    The creation of mysql docker container and the omnidb container will be done here.
                else:
                    

                    os.system("echo esxiforme | sudo -S docker run -d " + "--name '" + DB_Details.db_uid + "' -e MYSQL_ROOT_PASSWORD=KmQfcsnpdUrrRL2qzE8P --network=net1 mysql")
                    time.sleep(30)             
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"CREATE USER '" + DB_Details.username + "'@'localhost' IDENTIFIED BY '" + DB_Details.password + "';\"")
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"CREATE USER '" + DB_Details.username + "'@'%' IDENTIFIED BY '" + DB_Details.password + "';\"")             
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"CREATE DATABASE " + DB_Details.db_name + ";\"")
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"GRANT ALL ON " + DB_Details.db_name + ".* TO '" + DB_Details.username + "'@'localhost'; FLUSH PRIVILEGES;\"")
                    os.system("echo KmQfcsnpdUrrRL2qzE8P | sudo -S docker exec -i " + DB_Details.db_uid + " mysql -u root -p -e \"GRANT ALL ON " + DB_Details.db_name + ".* TO '" + DB_Details.username + "'@'%'; FLUSH PRIVILEGES;\"")

                    time.sleep(1)
                    check_val = os.system("echo esxiforme | sudo -S docker ps -a | grep " + str(DB_Details.db_uid))
                    if check_val == 0:
                        db = DBNode(user_ID=request.user,
                        Email=request.user,
                        linked_to_node_uuid=DB_Details.linked_to_app,
                        db_hostname=request.POST.get('database_hostname'),
                        Date_Created=DB_Details.Date_Created,
                        link_status=link_status,
                        id_link_color=db_id_link_color,
                        db_name=DB_Details.db_name,
                        db_username=DB_Details.username,
                        db_password=DB_Details.password,
                        db_uid=DB_Details.db_uid,
                        db_engine=DB_Details.db_engine,
                        # db_port=DB_Details.db_port,
                        db_port=3309,
                        db_version=DB_Details.db_version,
                        db_load_type=DB_Details.load_option)
                        db.save()

                        a = DBNode.objects.filter(db_uid=DB_Details.db_uid).first()
                        a.db_internal_ip = os.popen("echo esxiforme | sudo -S docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' " + DB_Details.db_uid).read().strip()
                        a.save()
                        
                      
                        return HttpResponse('success')
                    else:
                        return HttpResponse('error')
                    
    
def mikro_instance(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/new_mikro_instance.html')
    else:
        return redirect('/accounts/login/')

def web_app(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/new_web_app.html', {'uuid':uuid.uuid4().hex})
    else:
        return redirect('/accounts/login/')

def our_web_app(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/our_web_app.html')
    else:
        return redirect('/accounts/login/')

def spice_service(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/new_spice_service.html')
    else:
        return redirect('/accounts/login/')

def firewall(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/firewall.html')
    else:
        return redirect('/accounts/login/')

def domains(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/domains.html')
    else:
        return redirect('/accounts/login/', {'message':'Not loged In'})

def monitoring(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/monitoring.html')
    else:
        return redirect('/accounts/login/')

def logs(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/logs.html')
    else:
        return redirect('/accounts/login/')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'html/spec-comp/dashboard/profile.html')
    else:
        return redirect('/accounts/login/')

def fast_easy(request):
    if request.user.is_authenticated:
        db_user = CustomUser.objects.filter(email=request.user).first()
        if UserTrait.objects.filter(email=db_user.email).exists():
            return render(request, 'html/spec-comp/dashboard/new_node.html')
        
        else:
            return render(request, 'html/spec-comp/dashboard/buy_containers.html', {'message_1':'You appear to not have available containers.', 'message_2':'You can get any number of containers for any need at any time, at the best price.', 'hide_or_not':'dont_hide'})
        return render(request, 'html/spec-comp/dashboard/buy_containers.html')
    else:
        return redirect('/accounts/login/')

def technical(request):
    if request.user.is_authenticated:

        return render(request, 'html/spec-comp/dashboard/technical.html')
    else:
        return redirect('/accounts/login/')

def billing(request):
    if request.user.is_authenticated:
        if UserTrait.objects.filter(email=request.user).exists():
            a = UserTrait.objects.filter(email=request.user).first()
            
            return render(request, 'html/spec-comp/dashboard/billing.html', {'card_number_1':a.credit_card_number.split(' ')[0],
                                                                                'card_number_2':a.credit_card_number.split(' ')[3],
                                                                                'card_handler':a.credit_card_holder_name,
                                                                                'card_exp_month':a.credit_card_expire_month,
                                                                                'card_exp_year':a.credit_card_expire_year})
        else:
            return render(request, 'html/spec-comp/dashboard/billing.html', {'no_card':True})                                                                     
    else:
        return redirect('/accounts/login/')

def new_knot(request):
    if request.user.is_authenticated:
        if UserTrait.objects.filter(email=request.user).exists():
            return render(request, 'html/spec-comp/dashboard/buy_containers.html', {'hide_or_not':'hideme'})
        else:
            messages.success(request, 'You need to add a credit card')
            
            return render(request, 'html/spec-comp/dashboard/buy_containers.html', {'hide_or_not':'hideme', 'disable_or_not':'disabled', 'variable':True})
    else:
        return redirect('/accounts/login/')

def create_order(request):
    
    if request.user.is_authenticated:

        class OrderDetails():
            vcpu = None
            vram = None
            bandwidth = None
            container_number = None
            total_price = None
            container_price = None
            order_category = None
            purchase_id = None


        OrderDetails.vcpu = request.POST.get('vcpu_alloc')
        OrderDetails.vram = request.POST.get('ram_alloc')
        OrderDetails.bandwidth_alloc = request.POST.get('bandwidth_alloc')
        OrderDetails.container_number = request.POST.get('container_number')
        OrderDetails.total_price = request.POST.get('order_price')
        OrderDetails.container_price = request.POST.get('container_price')
        OrderDetails.order_category = request.POST.get('order_category')
        OrderDetails.purchase_id = uuid.uuid4().hex

        db_user = CustomUser.objects.filter(email=request.user).first()
            
           
        if UserTrait.objects.filter(email=db_user.email).exists():
            a = UserTrait.objects.filter(email=db_user.email).first()

            if OrderDetails.order_category == 'low_load':
                a.low_nodes_count += int(OrderDetails.container_number)
                a.save()
            elif OrderDetails.order_category == 'medium_load':
                a.medium_nodes_count += int(OrderDetails.container_number)
                a.save()
            elif OrderDetails.order_category == 'high_load':
                a.high_nodes_count += int(OrderDetails.container_number)
                a.save()
                
        else:
            if OrderDetails.order_category == 'low_load':
                user_trait = UserTrait(user_ID=request.user, low_nodes_count=OrderDetails.container_number, email=db_user.email)
                user_trait.save()
            elif OrderDetails.order_category == 'medium_load':
                user_trait = UserTrait(user_ID=request.user, medium_nodes_count=OrderDetails.container_number, email=db_user.email)
                user_trait.save()
            elif OrderDetails.order_category == 'high_load':
                user_trait = UserTrait(user_ID=request.user, high_nodes_count=OrderDetails.container_number, email=db_user.email)
                user_trait.save()

        return HttpResponse("success")

        
    else:
        return redirect('/accounts/login/')

def new_node(request, uuid, mode):
    import uuid
    if request.user.is_authenticated:

        global key
        request_key = str(uuid.uuid4().hex)[0:12]
        key = request_key

        db_user = CustomUser.objects.filter(email=request.user).first()
        if UserTrait.objects.filter(email=db_user.email).exists():

            low_node = UserTrait.objects.filter(email=db_user.email).first().low_nodes_count
            low_node_status = None
            medium_node = UserTrait.objects.filter(email=db_user.email).first().medium_nodes_count
            medium_node_status = None
            high_node = UserTrait.objects.filter(email=db_user.email).first().high_nodes_count
            high_node_status = None

            container_end_count = 0

            if low_node == 0:
                low_node_status = 'disabled'
                container_end_count += 1
            if medium_node == 0:
                medium_node_status = 'disabled'
                container_end_count += 1
            if high_node == 0:
                high_node_status = 'disabled'
                container_end_count += 1

            if container_end_count == 3:
                return render(request, 'html/spec-comp/dashboard/buy_containers.html', {'message_1':'You appear to not have available containers.', 'message_2':'You can get any number of containers for any need at any time, at the best price.', 'hide_or_not':'dont_hide'})

            if mode == 'technical':
                total_containers = UserTrait.objects.filter(email=db_user.email).first().low_nodes_count + UserTrait.objects.filter(email=db_user.email).first().medium_nodes_count + UserTrait.objects.filter(email=db_user.email).first().high_nodes_count
                if total_containers >= 2:
                 
                    return render(request, 'html/spec-comp/dashboard/new_node.html', {
                    'if_disabled_low':low_node_status, 
                    'if_disabled_medium':medium_node_status, 
                    'if_disabled_high':high_node_status,
                    'no_low':low_node,
                    'no_medium':medium_node,
                    'no_high':high_node,
                    'db_1_disable':False,
                    'db_2_disable':False,
                    'db_3_disable':False,
                    'db_4_disable':False,
                    'key':key,
                    'true_or_false':'false',
                    'to_be_hidden':'easy',
                    'subdomain_domain': str(uuid.uuid4().hex)[0:12]
                    })
                elif total_containers <= 2:
                    return render(request, 'html/spec-comp/dashboard/new_node.html', {
                                                                                'if_disabled_low':'disabled', 
                                                                                'if_disabled_medium':'disabled', 
                                                                                'if_disabled_high':'disabled',
                                                                                'db_1_disable':'disabled',
                                                                                'db_2_disable':'disabled',
                                                                                'db_3_disable':'disabled',
                                                                                'db_4_disable':'disabled',
                                                                                'disable_dropdown_low':'disabled',
                                                                                'disable_dropdown_medium':'disabled',
                                                                                'disable_dropdown_high':'disabled',
                                                                                'key':key,
                                                                                'no_low':low_node,
                                                                                'no_medium':medium_node,
                                                                                'no_high':high_node, 
                                                                                'if_disabled_low':low_node_status, 
                                                                                'if_disabled_medium':medium_node_status, 
                                                                                'if_disabled_high':high_node_status,
                                                                                'subdomain_domain':str((uuid.uuid4().hex)[0:12]),
                                                                                'true_or_false':'false',
                                                                                'to_be_hidden':'easy'})

            if mode == 'easy':
                total_containers = UserTrait.objects.filter(email=db_user.email).first().low_nodes_count + UserTrait.objects.filter(email=db_user.email).first().medium_nodes_count + UserTrait.objects.filter(email=db_user.email).first().high_nodes_count
                if total_containers >= 2:
               
                    return render(request, 'html/spec-comp/dashboard/new_node.html', {
                                                                                    'if_disabled_low':'disabled', 
                                                                                    'if_disabled_medium':'disabled', 
                                                                                    'if_disabled_high':'disabled',
                                                                                    'db_1_disable':False,
                                                                                    'db_2_disable':False,
                                                                                    'db_3_disable':False,
                                                                                    'db_4_disable':False,
                                                                                    'key':key,
                                                                                    'no_low':low_node,
                                                                                    'no_medium':medium_node,
                                                                                    'no_high':high_node, 'if_disabled_low':low_node_status, 
                                                                                    'if_disabled_medium':medium_node_status, 
                                                                                    'if_disabled_high':high_node_status,
                                                                                    'subdomain_domain':str((uuid.uuid4().hex)[0:12]),
                                                                                    'true_or_false':'true',
                                                                                    'to_be_hidden':'technical'})

                elif total_containers <= 2:
                    return render(request, 'html/spec-comp/dashboard/new_node.html', {
                                                                                    'if_disabled_low':'disabled', 
                                                                                    'if_disabled_medium':'disabled', 
                                                                                    'if_disabled_high':'disabled',
                                                                                    'db_1_disable':'disabled',
                                                                                    'db_2_disable':'disabled',
                                                                                    'db_3_disable':'disabled',
                                                                                    'db_4_disable':'disabled',
                                                                                    'key':key,
                                                                                    'disable_dropdown_low':'disabled',
                                                                                    'disable_dropdown_medium':'disabled',
                                                                                    'disable_dropdown_high':'disabled',
                                                                                    'no_low':low_node,
                                                                                    'no_medium':medium_node,
                                                                                    'no_high':high_node, 'if_disabled_low':low_node_status, 
                                                                                    'if_disabled_medium':medium_node_status, 
                                                                                    'if_disabled_high':high_node_status,
                                                                                    'subdomain_domain':str((uuid.uuid4().hex)[0:12]),
                                                                                    'true_or_false':'true',
                                                                                    'to_be_hidden':'technical'})

        else:
            return render(request, 'html/spec-comp/dashboard/buy_containers.html', {'message_1':'You appear to not have available containers.', 'message_2':'You can get any number of containers for any need at any time, at the best price.', 'hide_or_not':'dont_hide', 'variable':True, 'disable_or_not':'disabled'})
    else:
        return redirect('/accounts/login/')

def create_node(request, name_domain):
    import random
    from django.http import HttpResponse
    if request.user.is_authenticated:

        request_key_ = request.POST.get('request_key')
        if request_key_ == key:
            request_key = None
        else:
            print('bad news')

        color_list = ['red', 'green', 'orange', 'teal', 'violet', 'pink', 'yellow', 'blue', 'purple', 'black']
        color_pick = random.choice(color_list)

        class NodeDetails():
            app_type = None
            monitor_type = None
            server_region = None
            node_name = name_domain.split('&')[0]
            domain_name = name_domain.split('&')[1]
            load_type = None
            framework = None
            
            
        if request.method == 'POST':
            NodeDetails.app_type = request.POST.get('app_type')
            NodeDetails.monitor_type = request.POST.get('monitor_type')
            NodeDetails.server_region = request.POST.get('server_region')
            NodeDetails.load_type = request.POST.get('load_type')
            NodeDetails.framework = request.POST.get('framework')

            db_user = CustomUser.objects.filter(email=request.user).first()

            if NodeDetails.load_type == 'low_load':
                NodeDetails.load_type = 'Low Load'
                d = UserTrait.objects.filter(email=request.user).first()
                d.low_nodes_count = d.low_nodes_count - 1 
                d.save()
            if NodeDetails.load_type == 'medium_load':
                NodeDetails.load_type = 'Medium Load'
                e = UserTrait.objects.filter(email=request.user).first()
                e.medium_nodes_count = e.medium_nodes_count - 1 
                e.save()
            if NodeDetails.load_type == 'high_load':
                NodeDetails.load_type = 'High Load'
                f = UserTrait.objects.filter(email=request.user).first()
                f.high_nodes_count = f.high_nodes_count - 1 
                f.save()
            
            
            b = Node(user_ID=request.user, 
            node_ID=str(uuid.uuid4()).split('-')[0], 
            Email=request.user, 
            Status=True, 
            Name=NodeDetails.node_name, 
            Framework=NodeDetails.framework,
            framework_version=request.POST.get('framework_version'),
            is_webapp=True, 
            id_link_color=color_pick,
            Date_Created=datetime.now(), 
            Load_Type=NodeDetails.load_type, 
            Private_IPv4='152.25.33.54', 
            Monitoring=NodeDetails.monitor_type, 
            Domain_Name=NodeDetails.domain_name, 
            order_node_count =+ 1,
            link_status=False,
            )
            b.save()
        
        return HttpResponse('success')
            
    else:
        return redirect('/accounts/login/')

def get_data(request, node_id):
    if request.user.is_authenticated:
        db_user = Node.objects.filter(Email=request.user)
        a = db_user.filter(node_ID=node_id).first()
        
        app_icon = None

        if a.Framework == 'angular':
            app_icon = '<i class="angular icon" style="position: absolute; top: 3px; right: 10px; font-size: 40px; color:red;"></i>'
        if a.Framework == 'laravel':
            app_icon = '<i class="laravel icon" style="position: absolute; top: 3px; right: 10px; font-size: 40px; color:orangered;"></i>'
        if a.Framework == 'django':
            app_icon = '<img src="https://cdn2.hubspot.net/hubfs/3885898/django.png" width="45px" height="40px" style="top: 3px; right: 10px;position: absolute;">'
        if a.Framework == 'wordpress':
            app_icon = '<i class="wordpress icon" style="position: absolute; top: 3px; right: 10px; font-size: 40px; color:skyblue;"></i>'
        
    
        return HttpResponse(a.Name+'&'+a.node_ID+'&'+str(a.Date_Created)+'&'+a.Private_IPv4+'&'+a.IPv4+'&'+a.Domain_Name+'&'+app_icon)
    
def get_container_data(request):
    if request.user.is_authenticated:
        db_user = Node.objects.filter(Email=request.user)

        free_containers_count = 0
        w = UserTrait.objects.filter(email=request.user).first()
        free_containers_count += w.low_nodes_count
        free_containers_count += w.medium_nodes_count
        free_containers_count += w.high_nodes_count

        used_containers_count = 0
        for node in db_user:
            used_containers_count += 1
        
        
        return HttpResponse(str(used_containers_count)+'&'+str(free_containers_count))

def delete_container(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            node_id = str(id)

            if Node.objects.filter(node_ID=node_id).exists():
                a = Node.objects.filter(node_ID=node_id).first()
                a.delete()
                return HttpResponse('success')

            if DBNode.objects.filter(db_uid=node_id).exists():
                a = DBNode.objects.filter(db_uid=node_id).first()
                os.system("echo esxiforme | sudo -S docker stop " + str(node_id))
                a.delete()

                return HttpResponse('success')
                
            messages.success(request, 'Something went wrong, we couldn\'t finish your request.')
            return redirect('/overview/')

def send_credit_card(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            ms_username = str((uuid.uuid4().hex)[0:8])
            ms_password = str((uuid.uuid4().hex)[0:8])

            a = UserTrait(credit_card_number=request.POST.get('cc-number'), 
            user_ID=request.user, 
            email=request.user, 
            credit_card_holder_name=request.POST.get('card-holder'),
            credit_card_expire_month=request.POST.get('cc-exp').split('/')[0], 
            credit_card_expire_year=request.POST.get('cc-exp').split('/')[1], 
            credit_card_security_code=request.POST.get('cc-cvc'),
            dbms_username=ms_username,
            dbms_password=ms_password,
            dbms_enabled=True
            )
            a.save()
            os.system("omnidb-config-server -u " + ms_username + " " + ms_password)
            return HttpResponse('success')

def edit_credit_card(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if UserTrait.objects.filter(email=request.user).exists():
                a = UserTrait.objects.filter(email=request.user).first()
                a.credit_card_number = request.POST.get('cc-number')
                a.credit_card_holder_name = request.POST.get('card-holder')
                a.credit_card_expire_month = request.POST.get('cc-exp').split('/')[0]
                a.credit_card_expire_year = request.POST.get('cc-exp').split('/')[1]
                a.credit_card_security_code = request.POST.get('cc-cvc')
                a.save()
        
                
        
        
        
        
        
        
                return HttpResponse('success')
        
def create_node_technical(request, name_domain_subdomain):
    import uuid
    import random
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            color_list = ['red', 'green', 'orange', 'teal', 'violet', 'pink', 'yellow', 'blue', 'purple', 'black']
            color_pick = random.choice(color_list)
            
            class NodeDetailsTechnical():
                user_ID = None
                node_ID = None
                Email = None
                Status = None
                Name = None
                Framework = None
                NodeType = None
                Date_Created = None
                Load_Type = None
                order_node_count = None
                IPv4 = None
                Private_IPv4 = None
                Domain_Name = None
                Monitoring = None
                Subdomain = None
                Database = None
                DatabaseEngine = None
                DatabaseVersion = None
                DatabaseUUID = str((uuid.uuid4().hex)[0:12])
                FrameworkVersion = None

            NodeDetailsTechnical.user_ID = request.user
            NodeDetailsTechnical.node_ID = str(uuid.uuid4()).split('-')[0]
            NodeDetailsTechnical.Email = request.user
            NodeDetailsTechnical.Status = True
            NodeDetailsTechnical.Name = name_domain_subdomain.split('&')[0]
            NodeDetailsTechnical.Framework = request.POST.get('framework_1')
            NodeDetailsTechnical.NodeType = request.POST.get('app_type')
            NodeDetailsTechnical.Date_Created = datetime.now()
            NodeDetailsTechnical.Load_Type = request.POST.get('load_type_1')
            NodeDetailsTechnical.IPv4 = '195.25.15.35'
            NodeDetailsTechnical.Private_IPv4 = '172.14.23.66'
            NodeDetailsTechnical.Domain_Name = name_domain_subdomain.split('&')[1]
            NodeDetailsTechnical.Monitoring = request.POST.get('monitor_type_1')
            NodeDetailsTechnical.Subdomain = name_domain_subdomain.split('&')[2]
            NodeDetailsTechnical.DatabaseEngine = request.POST.get('database')
            NodeDetailsTechnical.DatabaseVersion = request.POST.get('database_version')
            NodeDetailsTechnical.FrameworkVersion = request.POST.get('framework_version_1')

            
            db_user = CustomUser.objects.filter(email=request.user).first()
            

            if NodeDetailsTechnical.DatabaseEngine == "":
                b = Node(user_ID=request.user, 
                node_ID=NodeDetailsTechnical.node_ID, 
                Email=request.user,
                Status=True, 
                Name=NodeDetailsTechnical.Name, 
                Framework=NodeDetailsTechnical.Framework, 
                is_webapp=True, 
                Date_Created=NodeDetailsTechnical.Date_Created, 
                Load_Type=NodeDetailsTechnical.Load_Type, 
                IPv4=NodeDetailsTechnical.IPv4,
                Private_IPv4=NodeDetailsTechnical.Private_IPv4, 
                Monitoring=NodeDetailsTechnical.Monitoring, 
                Domain_Name=NodeDetailsTechnical.Domain_Name, 
                Subdomain=NodeDetailsTechnical.Subdomain, 
                framework_version=NodeDetailsTechnical.FrameworkVersion,
                link_status=False,
                linked_to_db_uuid='none',
                id_link_color='none',
                order_node_count =+ 1)
                b.save()

            if NodeDetailsTechnical.Load_Type == 'low_load':
                NodeDetailsTechnical.Load_Type = 'Low Load'
                d = UserTrait.objects.filter(email=request.user).first()
                if NodeDetailsTechnical.DatabaseEngine != "":
                    db = DBNode(user_ID=request.user, 
                    Email=request.user, 
                    Status=True, 
                    db_hostname=str(uuid.uuid4()).split('-')[0],
                    db_engine=NodeDetailsTechnical.DatabaseEngine,
                    db_version=NodeDetailsTechnical.DatabaseVersion, 
                    db_uid=NodeDetailsTechnical.DatabaseUUID,
                    db_username=str((uuid.uuid4().hex)[0:12]),
                    db_password=str((uuid.uuid4().hex)[0:12]),
                    Date_Created=datetime.now(),
                    id_link_color=color_pick,
                    linked_to_node_uuid=NodeDetailsTechnical.node_ID,
                    link_status=True,
                    db_load_type='low_load')
                    db.save()
                    b = Node(user_ID=request.user, 
                    node_ID=NodeDetailsTechnical.node_ID, 
                    Email=request.user,
                    Status=True, 
                    Name=NodeDetailsTechnical.Name, 
                    Framework=NodeDetailsTechnical.Framework, 
                    is_webapp=True, 
                    Date_Created=NodeDetailsTechnical.Date_Created, 
                    Load_Type=NodeDetailsTechnical.Load_Type, 
                    IPv4=NodeDetailsTechnical.IPv4,
                    Private_IPv4=NodeDetailsTechnical.Private_IPv4, 
                    Monitoring=NodeDetailsTechnical.Monitoring,
                    link_status=True,
                    Domain_Name=NodeDetailsTechnical.Domain_Name, 
                    Subdomain=NodeDetailsTechnical.Subdomain, 
                    linked_to_db_uuid=NodeDetailsTechnical.DatabaseUUID,
                    id_link_color=color_pick,
                    framework_version=NodeDetailsTechnical.FrameworkVersion,
                    order_node_count =+ 1)
                    b.save()
                    d.low_nodes_count = d.low_nodes_count - 2 
                else:
                    d.low_nodes_count = d.low_nodes_count - 1   
                d.save()
            if NodeDetailsTechnical.Load_Type == 'medium_load':
                NodeDetailsTechnical.Load_Type = 'Medium Load'
                e = UserTrait.objects.filter(email=request.user).first()
                if NodeDetailsTechnical.DatabaseEngine != "":
                    db = DBNode(user_ID=request.user, 
                    Email=request.user, 
                    Status=True, 
                    internal_hostname=str(uuid.uuid4()).split('-')[0],
                    external_hostname=str(uuid.uuid4()).split('-')[0], 
                    db_engine=NodeDetailsTechnical.DatabaseEngine,
                    db_version=NodeDetailsTechnical.DatabaseVersion, 
                    link_status=True,
                    linked_to_node_uuid=NodeDetailsTechnical.node_ID,
                    db_uid=NodeDetailsTechnical.DatabaseUUID,
                    db_username=str((uuid.uuid4().hex)[0:12]),
                    db_password=str((uuid.uuid4().hex)[0:12]),
                    Date_Created=datetime.now(),
                    id_link_color=color_pick,
                    db_load_type='medium_load')
                    db.save()
                    b = Node(user_ID=request.user, 
                    node_ID=NodeDetailsTechnical.node_ID, 
                    Email=request.user,
                    Status=True, 
                    Name=NodeDetailsTechnical.Name, 
                    Framework=NodeDetailsTechnical.Framework, 
                    is_webapp=True, 
                    Date_Created=NodeDetailsTechnical.Date_Created, 
                    Load_Type=NodeDetailsTechnical.Load_Type, 
                    link_status=True,
                    IPv4=NodeDetailsTechnical.IPv4,
                    Private_IPv4=NodeDetailsTechnical.Private_IPv4, 
                    Monitoring=NodeDetailsTechnical.Monitoring, 
                    Domain_Name=NodeDetailsTechnical.Domain_Name, 
                    Subdomain=NodeDetailsTechnical.Subdomain, 
                    linked_to_db_uuid=NodeDetailsTechnical.DatabaseUUID,
                    id_link_color=color_pick,
                    framework_version=NodeDetailsTechnical.FrameworkVersion,
                    order_node_count =+ 1)
                    b.save()
                    e.medium_nodes_count = e.medium_nodes_count - 2 
                else:
                    e.medium_nodes_count = e.medium_nodes_count - 1 
                e.save()
            if NodeDetailsTechnical.Load_Type == 'high_load':
                NodeDetailsTechnical.Load_Type = 'High Load'
                f = UserTrait.objects.filter(email=request.user).first()
                if NodeDetailsTechnical.DatabaseEngine != "":
                    db = DBNode(user_ID=request.user, 
                    Email=request.user, 
                    Status=True, 
                    internal_hostname=str(uuid.uuid4()).split('-')[0],
                    external_hostname=str(uuid.uuid4()).split('-')[0], 
                    db_engine=NodeDetailsTechnical.DatabaseEngine,
                    db_version=NodeDetailsTechnical.DatabaseVersion, 
                    db_uid=NodeDetailsTechnical.DatabaseUUID,
                    db_username=str((uuid.uuid4().hex)[0:12]),
                    db_password=str((uuid.uuid4().hex)[0:12]),
                    Date_Created=datetime.now(),
                    link_status=True,
                    linked_to_node_uuid=NodeDetailsTechnical.node_ID,
                    id_link_color=color_pick,
                    db_load_type='high_load')
                    db.save()
                    b = Node(user_ID=request.user, 
                    node_ID=NodeDetailsTechnical.node_ID, 
                    Email=request.user,
                    Status=True, 
                    Name=NodeDetailsTechnical.Name, 
                    Framework=NodeDetailsTechnical.Framework, 
                    is_webapp=True, 
                    Date_Created=NodeDetailsTechnical.Date_Created, 
                    Load_Type=NodeDetailsTechnical.Load_Type, 
                    IPv4=NodeDetailsTechnical.IPv4,
                    link_status=True,
                    Private_IPv4=NodeDetailsTechnical.Private_IPv4, 
                    Monitoring=NodeDetailsTechnical.Monitoring, 
                    Domain_Name=NodeDetailsTechnical.Domain_Name, 
                    Subdomain=NodeDetailsTechnical.Subdomain, 
                    linked_to_db_uuid=NodeDetailsTechnical.DatabaseUUID,
                    id_link_color=color_pick,
                    framework_version=NodeDetailsTechnical.FrameworkVersion,
                    order_node_count =+ 1)
                    b.save()
                    f.high_nodes_count = f.high_nodes_count - 2 
                else:
                    f.high_nodes_count = f.high_nodes_count - 1 
                f.save()

            
            
            
            
            

            return HttpResponse("success")

        
    else:
        return redirect('/accounts/login/')

def get_db_data(request, node_id):
    if request.user.is_authenticated:
        db = DBNode.objects.filter(db_uid=node_id).first()
      
        return HttpResponse(db.db_name+'&'+db.db_uid+'&'+str(db.Date_Created)+'&'+db.db_internal_ip+'&'+db.db_external_ip+'&'+db.db_hostname+'&'+db.db_name+'&'+str(db.db_port)+'&'+db.db_username+'&'+db.db_password)

def get_payment(request, user_id):
    if request.user.is_authenticated:
        if not UserTrait.objects.filter(email=user_id).exists():

            return HttpResponse('false')



@csrf_exempt
def check_duplicate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            if os.path.isfile('uploaded_projects/' + str(request.user) + '_' + request.POST['file_name']):
                return HttpResponse('true')
            else:          
                return HttpResponse('false')


            

def warehouse(request):
    from hurry.filesize import size
    from .forms import DocumentForm
    from os.path import basename
    from django.core.files import File
    from django.core.files.storage import FileSystemStorage
    
    if request.method == 'POST':


        accepted_types = ['zip', 'x-rar', 'tar', '7zip', 'sql']

        class FileDetails():
            file_size = request.FILES['myfile'].size
            file_name = request.FILES['myfile'].name
            file_type = request.FILES['myfile'].content_type.split('/')[1]  
       
       

        if FileDetails.file_type in accepted_types:
            fs = FileSystemStorage()  

            
            
            filename = fs.save(str(request.user) + '_' + FileDetails.file_name, request.FILES['myfile'])
            # uploaded_file_url = fs.url(FileDetails.file_name)
            db = UploadedProject(user_ID=request.user, email=request.user,
                            Date_Uploaded=datetime.now(), file_name=FileDetails.file_name, file_type=FileDetails.file_type, file_size=size(FileDetails.file_size),
                            linked_to_node_uuid='', file_system_name=filename, file_uuid=uuid.uuid4().hex)
            db.save()
            
            return HttpResponse('true')
        else:
            return HttpResponse('not_supported')
        
    

        
    else:



        nodes = Node.objects.filter(Email=request.user)
        db_files = UploadedProject.objects.filter(email=request.user)

        

        if nodes.count() == 0:
            for file in db_files:
                file.linked_to_node_uuid = ''

        elif nodes.count() > 0:
            for file in db_files:
                if not Node.objects.filter(node_ID=file.linked_to_node_uuid).exists():
                    file.linked_to_node_uuid = ''

        webapp_count =Node.objects.filter(Email=request.user).count()


        return render(request, 'html/spec-comp/dashboard/warehouse.html', {'db_files':db_files, 'applications':Node.objects.filter(Email=request.user), 'webapp_count':webapp_count})
    
@csrf_exempt
def link_file(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            print(request.POST.get)
            app_id = request.POST['app_id']
            file_name = request.POST['file_name']

            project = UploadedProject.objects.filter(file_system_name=file_name).first()

            node = Node.objects.filter(node_ID=app_id).first()
            node.linked_to_project = True
            node.projet_link_uuid = project.file_uuid
            node.save()

            
            project.linked_to_node_uuid = app_id
            project.save()


            return HttpResponse('succes')

@csrf_exempt
def unlink_file(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            
            project = UploadedProject.objects.filter(file_name=request.POST['file_name']).first()
            try:
                node = Node.objects.filter(node_ID=project.linked_to_node_uuid).first()
                node.linked_to_project = False
                node.projet_link_uuid = ''
                node.save()
            except:
                pass
            
            project.linked_to_node_uuid = ''
            project.save() 
            return HttpResponse('success')

@csrf_exempt
def delete_file(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            os.remove("uploaded_projects/" + request.POST['file_name'])
            db_file = UploadedProject.objects.filter(file_system_name=request.POST['file_name']).first()
            db_file.delete()

            return HttpResponse('true')