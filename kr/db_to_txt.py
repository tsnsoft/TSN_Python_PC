import sqlite3

conn = sqlite3.connect("db\q.db ")

cursor_s = conn.cursor()
cursor_v = conn.cursor()

sql_sur = "SELECT sId, titleTranslation FROM S ORDER BY sId"
cursor_s.execute(sql_sur)
for s in cursor_s.fetchall():
    sId = s[0]
    title = s[1]
    sh = "Section " + "{:03d}".format(sId) + " " + title
    sh2 = 'Section ' + str(sId) + ' "' + title + '"'
    print(sh)
    f = open('TXT/' + sh + ".txt", 'w', encoding='UTF-8')
    f.writelines(sh2 + '\n\n')

    sql_vers = "SELECT * FROM V WHERE sId = ? ORDER BY _id"
    cursor_v.execute(sql_vers, [(sId)])
    for v in cursor_v.fetchall():
        vrId = v[2]
        vr = v[3]
        vrTxt = str(vrId) + '. ' + vr
        print(vrTxt)
        f.writelines(vrTxt + '\n')
    f.close()
