
from datetime import datetime 
from App import app
from flask import g , Flask, request, session, url_for, redirect, render_template, abort, flash 
from hashlib import md5
from contextlib import closing 
from werkzeug.security import check_password_hash, generate_password_hash 
import pymysql


def connect_db():
    return pymysql.connect(host='localhost' , user='root', password='root', db='world', charset='utf8') 

def executeQuery(query) : 
    conn = connect_db()
    curs = conn.cursor()
    curs.execute(query)  
    rv = [] 
    for row in curs._rows : 
        rv.append(row)
    conn.close()
    return rv  

def executeUpdate(query): 
    conn = connect_db()
    curs = conn.cursor() 
    curs.execute(query)
    conn.commit()  
    conn.close()

def execute(query):
    return true  

def get_choicecase(exampleNo):
    rv = g.db.execute('SELECT ChoiceCaseNo, Title, FigureType FROM t_choicecase where exampleNo = ?' , exampleNo).fetchone() 
    return rv 

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close() 

@app.before_request
def before_request():
     g.db = connect_db() 


@app.route('/')
@app.route('/home')
def home():

    pageUrl = 'index.html' 
    """Renders the home page."""
    return render_template(
        pageUrl,
        title='Home Page',
        year=datetime.now().year,
    ) 

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/partA', methods=['GET','POST']) 
def partA(): 
    if request.method == 'POST':  

        query = """ delete from t_answerchoice """ 
        executeUpdate(query) 

        for item in request.form :   
            if request.form[item] != "" :   
                query = """ INSERT INTO t_answerchoice ( ChoiceCaseNo, Point )  VALUES (""" + item  + """,""" +  request.form[item] + """)"""
                executeUpdate(query)  
        return render_template('graph_chartjs.html',
                        title='GRAPH',
                        message='THE 4MAT SYSTEM')

    else : 
        return render_template('partA.html', 
                            examples = executeQuery('''SELECT exampleNo, exampleTitle  From t_example where exampleType='A' order by exampleNo asc limit 10'''),
                            choices  = executeQuery('''SELECT A.exampleNo, A. exampleTItle  , B.Title ChoiceCase , B.ChoiceCaseNo, B.FiqureType  FROM t_example A, t_choicecase B 
                                                        WHERE A.exampleNo = B.exampleNo order by A.exampleNo asc '''))


@app.route('/partB')
def partB(): 
    return render_template('partB.html',
                           title='PART B',
                           message='각 문항마다 가장 당신을 잘 표현하는 항목에 표시하시오') 

@app.route('/graph')
def graph(): 

    Items = executeQuery('''
                                                SELECT SUM(A.Point) POINT  , C.FiqureType FigureType  FROM t_answerchoice A, t_choiceCase C 
                                                WHERE A.ChoiceCaseNo = C.ChoiceCaseNo 
                                                GROUP BY C.FiqureType''')

    #circle = ""
    #triangle = ""
    #star = ""
    #square = ""

    for item in Items:
        if item[1] == 'CIRCLE': 
            circle = str(item[0])
        elif item[1] == 'SQUARE':
            square = str(item[0])
        elif item[1] == 'STAR':
            star = str(item[0])
        elif item[1] == 'TRIANGLE':
            triangle = str(item[0])

    return render_template('graph_chartjs.html',
                           title='GRAPH',
                           message='THE 4MAT SYSTEM', 
                           T_circle = circle , T_square = square, T_star = star , T_triangle = triangle
                           )
