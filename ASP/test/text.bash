select st_Id, Name, Surname, cl_Name, time_In, time_Out, first_Absence, second_Absence, date from tb_attandance where cl_Name = "HCS6B" and date = "2022-05-02"
select * from tb_attandance where cl_Name="HCS6B" and r_Name="309" and date BETWEEN "2022-05-01" and "2022-06-01"

SELECT st_Id, Name, Surname, s_Name, cl_Name, SUM(first_Absence + second_Absence) as total from tb_attandance 
where cl_Name="HCS6B" and s_Name="linux system administration" and 
date BETWEEN "2022-5-01" and "2022-6-01" HAVING SUM(first_Absence + second_Absence) > 7

SELECT st_Id, Name, Surname, s_Name, cl_Name, sc_Period, sc_Year, SUM(first_Absence + second_Absence) as total, 
(CASE 
 	WHEN SUM(first_Absence + second_Absence) > 7 THEN 'ບໍ່ມີສິດເສັງ'
 	WHEN SUM(first_Absence + second_Absence) IS NULL THEN 'ບໍ່ມີສິດເສັງ'
 	ELSE 'ມີສິດເສັງ' END) AS Final_Report 
 FROM tb_attandance WHERE s_Name="linux system administration" and cl_Name="HCS6B" GROUP BY st_Id

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

select t.*,
       (case when A > B then 1 else 0 end) as true_col,
       (case when A > B then 0 else 1 end) as false_col
from t;






        "select st.st_Id, st.st_Name, st.st_Surname, d.d_Name, s.s_Name, \
            r.r_Name, cl.cl_Name, sc.sc_Period, sc.sc_Year, f.Name, f.Surname, sc.start_Class, \
            sc.end_Class \
            from tb_face f inner join tb_student st on f.st_Id = st.st_Id\
            inner join tb_class cl on st.cl_Id = cl.cl_Id\
            inner join tb_schedule sc on sc.cl_Id=cl.cl_Id\
            inner join tb_day d on d.d_Id=sc.d_Id\
            inner join tb_subject s on s.s_Id=sc.s_Id\
            inner join tb_room r on r.r_Id=sc.r_Id\
            where cl.cl_Name='"
        + cl_Name
        + "' and r.r_Name='"
        + r_Name
        + "';"



select st.st_Id, st.st_Name, st.st_Surname, att.cl_Name, att.sc_Period, att.sc_Year, SUM(att.first_Absence + att.second_Absence) as total,
(
 CASE
     WHEN SUM(att.first_Absence + att.second_Absence) <7 THEN 'ມີສິດເສັງ'
     ELSE 'ບໍ່ມີສິດເສັງ'
END
) as FINALREPORT
from tb_student st left join tb_attandance att on st.st_Id=att.st_Id where att.cl_Name="HCS6B" and att.s_Name ="linux system administration" group by st.st_Id