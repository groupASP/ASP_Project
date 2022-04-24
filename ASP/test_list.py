# import mysql.connector
#
#
# conn = mysql.connector.connect(user="root", password="", host="Localhost",database="asp_base")
# curs = conn.cursor()
#
#
# #combobox form database
# curs.execute('select v_Name from tb_village;')
# results = curs.fetchall()
# comboboxVillage = [result[0] for result in results]
#
# v_Id = comboboxVillage
# listToStr = ' '.join(map(str, v_Id))
# print(listToStr)


