
from datetime import datetime 
from App import app
from flask import g , Flask, request, session, url_for, redirect, render_template, abort, flash 
from hashlib import md5
from contextlib import closing 
from werkzeug.security import check_password_hash, generate_password_hash 
import pymysql


def connect_db():
    return pymysql.connect(host='localhost' , user='root', password='root', db='world', charset='utf8') 

def query_db(query) : 
    conn = pymysql.connect(host='localhost' , user='root', password='root', db='world', charset='utf8') 
    cur = conn.cursor()
    cur.execute(query)  
    rv = [] 
    for row in cur._rows : 
        rv.append(row)
    return rv  

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

@app.route('/partA') 
def partA():
      
     #return render_template('partA.html' ,
     #                       examples = query_db('''select exampleTitle  From t_example where exampleType='A' order by exampleNo asc limit 10'''))  

     return render_template('partA.html', 
                            examples = query_db('''select exampleNo, exampleTitle  From t_example where exampleType='A' order by exampleNo asc limit 10'''),
                            choices = query_db('''SELECT A.exampleNo, A. exampleTItle  , B.Title ChoiceCase , B.ChoiceCaseNo, B.FiqureType  FROM t_example A, t_choicecase B 
WHERE A.exampleNo = B.exampleNo order by A.exampleNo asc '''))


@app.route('/partB')
def partB():


    return render_template('partB.html',
                           title='PART B',
                           message='각 문항마다 가장 당신을 잘 표현하는 항목에 표시하시오') 

@app.route('/graph')
def graph():
    return render_template('graph.html',
                           title='GRAPH',
                           message='THE 4MAT SYSTEM')
