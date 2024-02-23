from flask import Flask, render_template ,request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
import random
from load import predict
# from soap import emooo

###########################################################################################################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///chatbot.db"
db=SQLAlchemy(app)
alpha=["How are you?","Tell me more", "What happened?"]


name1=["How was your day?","Is there something which you wanted to speak to me about?","During the last week. What affected you the most?","Tell me more"]
name2=["How was today? How are you feeling?","In your schedule of things to do, what made you think of me as a priority?","So last week, tell me more about it.","Tell me more"]
name3=["What events happened during your day today?","What made you come and talk to me?","How was your last week?","Tell me more"]
the_name=[name1,name2,name3]
question=random.choice(the_name)


class chatbot(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    message = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name} - {self.message}"




@app.route('/', methods=["GET" , "POST"])
def hello_world():
    if request.method=="POST":
        i=srno()
        k=adjust(i)
        if i<8:
            name=""
            message=request.form['message']
            text =chatbot(name=name,message=message)
            db.session.add(text)
            db.session.commit()
            name2=question[k]
            message2=""
            text2 =chatbot(name=name2,message=message2)
            db.session.add(text2)
            db.session.commit()
        elif i>=10:
            delete()
        else:
            name=""
            message=request.form['message']
            text =chatbot(name=name,message=message)
            db.session.add(text)
            db.session.commit()
            name2=output()
            message2=""
            text2 =chatbot(name=name2,message=message2)
            db.session.add(text2)
            db.session.commit()
            name3="Type Anything to Restart"
            message3=""
            text3 =chatbot(name=name3,message=message3)
            db.session.add(text3)
            db.session.commit()
    alltexts = chatbot.query.all()
    return render_template("index.html", alltexts=alltexts)

@app.route('/show')
def products():
    alltexts = chatbot.query.all()
    return render_template("table.html", alltexts=alltexts)

@app.route('/delete')
def delete():
    # count = letschat.query.count()    
    sample = chatbot.query.first()
    if sample==None:
        pass
    else:
        db.session.delete(sample)
        db.session.commit()
        delete()
    return redirect("/")


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=="POST":
        name=request.form['name']
        message=request.form['message']
        text = chatbot.query.filter_by(sno=sno).first()
        text.name = name
        text.message = message
        db.session.add(text)
        db.session.commit()
        return redirect("/")
    text = chatbot.query.filter_by(sno=sno).first()
    return render_template("update.html", text=text)

def output():
    con = sqlite3.connect("instance\chatbot.db")
    cur = con.cursor()
    str=""
    for row in cur.execute('SELECT message FROM chatbot;'):
        temp=' '.join(row)
        str=str+" "+temp
    con.close()
    answer= predict(str)
    return answer

def srno():
    con = sqlite3.connect("instance\chatbot.db")
    cur = con.cursor()
    tup=(None,)
    for row in cur.execute('SELECT MAX(sno) FROM chatbot;'):
        if row==tup:
            no=0
        else:
            no = int(''.join(map(str, row)))
    print(no)
    con.close()
    return no

def adjust(u):
    if u==0:
        v=0
    elif u==2:
        v=1
    elif u==4:
        v=2
    elif u==6:
        v=3
    else:
        v=4
    return v

if __name__=="__main__":
    app.run(debug=True)

