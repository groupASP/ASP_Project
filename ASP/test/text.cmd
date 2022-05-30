select st_Id, Name, Surname, cl_Name, time_In, time_Out, first_Absence, second_Absence, date from tb_attandance where cl_Name = "HCS6B" and date = "2022-05-02"
select * from tb_attandance where cl_Name="HCS6B" and r_Name="309" and date BETWEEN "2022-05-01" and "2022-06-01"
SELECT st_Id, Name, Surname, s_Name, cl_Name, SUM(first_Absence + second_Absence) as total from tb_attandance where cl_Name="HCS6B" and s_Name="linux system administration" and 
date BETWEEN "2022-5-01" and "2022-6-01" HAVING SUM(first_Absence + second_Absence) > 7

//TODO 30.05.2022
sudo apt-get update

sudo apt-get -y install apache2 mysql-client mysql-server php5

mysql -u root -h localhost -p

sudo apt-get -y install graphviz aspell php5-pspell php5-curl php5-gd php5-intl php5-mysql php5-xmlrpc php5-ldap git-core

sudo mv moodle /var/www/html/

sudo chown -R www-data /var/www/html/moodle

sudo chmod -R 777 /var/www/html/moodle/

ifconfig

http://192.168.75.129/moodle/install.php

cd /var/www/

sudo mkdir moodledata

sudo chown -R www-data /var/www/moodledata

sudo cdmod -R 777 /var/www/moodledata

password Souliya@#2015