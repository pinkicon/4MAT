


#"""
#Routes and views for the flask application.
#"""

#from datetime import datetime
#from flask import render_template
#from App import app

#@app.route('/')
#@app.route('/home')
#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )



"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from App import app
from flask import g 
#from pymysql import

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

    ##MySql Connection 연결 
    #conn = pymysql.connect(host='localhost' , user='root', password='root', db='world', charset='utf8')

    ##Connection으로 부터 Cursor생성 
    #curs = conn.cursor()

    ##SQL문 실행 
    #sql = "select * From t_example where exampleType='A'" 
    #curs.execute(sql) 

    ##데이터 fetch 
    #rows = curs.fetchall()
    #print(rows) 
    
    ### print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')

    #conn.close()

    return render_template('partA.html' , 
                           title = 'PART A',
                           message='아래 질문들은 당신의 학습행동과 참여 선호도를 나타내도록 만들어져 있습니다. 어떤 항목이 가장 본인과 비슷합니까? 본인과 가장 비슷한 항목에 "4"를 기입하고 가장 비슷하지 않은 항목에 "1" 을 기입하십시오. 나머지 항목에는 "2", "3" 을 기입하십시오. 4개의 모든 숫자를 한번씩만 기입해 주십시오')


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
