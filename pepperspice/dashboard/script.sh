#!/bin/bash
arg1=$1 # DB UID
arg2=$2 # DB Username
arg3=$3 # DB Password
arg4=$4 # DB Name

echo toor | sudo -S docker run -d --name $arg1 --network=net1 -e MYSQL_ROOT_PASSWORD=toor --ip 192.168.8.56 mysql
sleep 30
echo toor | sudo -S docker exec -i $arg1 mysql -u root -p -e "CREATE USER '$arg2'@'localhost' IDENTIFIED BY '$arg3'; FLUSH PRIVILEGES;"
sleep 2
echo toor | sudo -S docker exec -i $arg1 mysql -u root -p -e "GRANT ALL PRIVILEGES ON $arg4.* TO '$arg2'@'localhost'; FLUSH PRIVILEGES;"
sleep 2
echo toor | sudo -S docker exec -i $arg1 mysql -u root -p -e "DELETE FROM mysql.user WHERE User='root'; FLUSH PRIVILEGES;"
sleep 2
echo $arg3 | docker exec -i $arg1 mysql -u $arg2 -p -e "CREATE DATABASE $arg4;"
