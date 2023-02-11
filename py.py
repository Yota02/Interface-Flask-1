from flask import *
import mysql.connector

cnx = mysql.connector.connect(user = 'root', password = '',
                              host = 'localhost',
                              port = 3306,
                              database = 'bdfilms')

app = Flask(__name__)
cur = cnx.cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/resultats', methods=['POST', 'GET'])
def resultats():
    if request.method == 'POST':
        donnee = request.form
        select = donnee.get('select')
        select2 = donnee.get('select2')
        select3 = donnee.get('select3')

        where= donnee.get('where')
        where2= donnee.get('where2')
        
        num = donnee.get('num')
        num2 = donnee.get('num2')
        
        signe = donnee.get('signe')
        signe2 = donnee.get('signe2')
        
        selwh = donnee.get('selwh')

        like = donnee.get('like')
        selike = donnee.get('selike')
        likea = donnee.get('likea')
        if select != '*': 
            if like != 'select' and selike == 'com' :
                txt = f"SELECT {select} {select2} {select3} FROM films WHERE {where} {signe} {num} {selwh} {where2} {signe2} {num2} AND {like} LIKE '{likea}%' ORDER BY {select}"
                cur.execute(txt)
            elif like != 'select' and selike == 'fin' :
                txt = f"SELECT {select} {select2} {select3} FROM films WHERE {where} {signe} {num} {selwh} {where2} {signe2} {num2} AND {like} LIKE '%{likea}'ORDER BY {select} "
                cur.execute(txt)
            elif like != 'select' and selike == 'cont' :
                txt = f"SELECT {select} {select2} {select3} FROM films WHERE {where} {signe} {num} {selwh} {where2} {signe2} {num2} AND {like} LIKE '%{likea}%'ORDER BY {select} "
                cur.execute(txt)
            else : 
                txt = f"SELECT {select} {select2} {select3} FROM films WHERE {where} {signe} {num} {selwh} {where2} {signe2} {num2} "
                cur.execute(txt)
        else : 
            txt = f"SELECT {select} {select2} {select3} FROM films WHERE {where} {signe} {num} {selwh} {where2} {signe2} {num2} "
            cur.execute(txt)
        return render_template('resultats.html',films=cur, requette = txt)
    else:
        return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug= True)

cnx.close()