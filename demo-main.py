from flask import Flask, render_template, flash, redirect, url_for, request

from main_logic import *
from helper_form import *
from flask_wtf import FlaskForm

from wtforms import widgets ,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
import random,os
app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'secret string')

@app.route('/',methods=['GET','POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        if username == "testing":
            flash('Welcome, %s!' % username)
            return redirect(url_for('mainpage'))
        else:

            flash('cannot find, %s!' % username)
    return render_template('login.html',form=form)




@app.route('/main',methods=['GET','POST'])
def mainpage():
    # if the db_secure_score is too low, then there may be a attack
    if db_secure_score <=50:
        seed = random.randint(0,2)
        if seed >= 1:
            return redirect(url_for("response",status="success"))
    return render_template('main.html',score = score)

@app.route('/response/<status>',methods=['GET','POST'])
def response(status):
    try:
        if status == "success":
            global  response_index
            response_index = response_index + 1
            return render_template("response.html",message = response_task_messages[response_index-1])
        else:
            return render_template("response.html", message=response_task_messages[response_index-1])
    except:
        return "<h1>Thanks for playing</h1>"



@app.route('/config/food')
def show_food_config():
    return render_template('config.html',type="Food and Price",config=config_food,score = score)
@app.route('/config/user')
def show_user_config():
    return render_template('config.html',type="user information",config=config_user,score = score)
@app.route('/config/test')
def show_test_config():
    return render_template('config.html',type="Testing",config=config_test,score = score)

@app.route('/log')
def show_log():
    global current_task_index
    current_task_index = current_task_index +1
    if current_task_index>4:
        current_task_index = 1

    return  render_template('log.html',message=task_messages[current_task_index-1])
@app.route('/log/<cost>')
def log_result(cost):
    global score
    change_secure = eval(str(cost).split('*')[0])
    change_us = eval(str(cost).split('*')[1])

    score['user_score'] = score['user_score'] + change_us
    score['db_score'] = score['db_score'] +change_secure

    return redirect(url_for('mainpage',score=score))


@app.route('/audit/<db>',methods=['GET','POST'])
def handelaudit(db):
    form = auditform()
    if form.validate_on_submit():
        choices = form.choices.data
        num_choices = len(choices)

        for choice in choices:
            choice = eval(choice)
            if db== "Food and Price":
                # modify the db_secure_score
                score['db_score'] = min(score['db_score'] + (11-choice)*2, 100)
                score['user_score']= score['user_score']-(13-choice)
                score['invest_score']=score['invest_score']-(13-choice)
                for key in config_food.keys():
                    config_food[key]['cpu'] = config_food[key]['cpu'] + num_choices*0.01*(11-choice)


            if db== "testing":
                # modify the db_secure_score
                score['db_score'] = min(score['db_score'] + (12 - choice), 100)
                for key in config_test.keys():
                    config_test[key]['cpu'] = config_test[key]['cpu'] + num_choices*0.01*(11-choice)


            if db== "user information":
                # modify the db_secure_score
                score['db_score'] = min(score['db_score'] + (12 - choice)*2, 100)
                score['user_score'] = score['user_score'] - (11 - choice)
                score['invest_score'] = score['invest_score'] - (11 - choice)
                for key in config_user.keys():
                    config_user[key]['cpu'] = config_user[key]['cpu'] + num_choices*0.01*(11-choice)

        return render_template('main.html',score = score)
    return render_template('auditform.html',form=form)

@app.route('/mask/<db>',methods=['GET','POST'])
def handelmask(db):

    if db == "Food and Price":
        form = maskform_food()

    if db== "testing":
        form =maskform_test()

    if db == "user information":
        form=maskform_user()

    if form.validate_on_submit():
        choices = form.choices.data
        num_choices = len(choices)

        for choice in choices:
            choice = eval(choice)
            if db== "Food and Price":
                # modify the db_secure_score
                score['db_score'] = min(score['db_score'] + (10-choice), 100)
                score['user_score']= score['user_score']-(8-choice)
                score['invest_score']=score['invest_score']-(8-choice)
                for key in config_food.keys():
                    config_food[key]['cpu'] = config_food[key]['cpu'] + num_choices*0.01*(5-choice)



            if db== "user information":
                # modify the db_secure_score
                score['db_score'] = min(score['db_score'] + (12 - choice), 100)
                score['user_score'] = score['user_score'] - (7 - choice)
                score['invest_score'] = score['invest_score'] - (7 - choice)
                for key in config_user.keys():
                    config_user[key]['cpu'] = config_user[key]['cpu'] + num_choices*0.01*(4-choice)

        return render_template('main.html',score = score)
    return render_template('maskform.html',form=form)

@app.route('/query/<db>',methods=['GET','POST'])
def handelquery(db):

    if db == "Food and Price":
        form = queryform_food()

    if db== "testing":
        form =queryform_test()

    if db == "user information":
        form=queryform_user()

    if form.validate_on_submit():
        choices = form.choices.data
        num_choices = len(choices)

        for choice in choices:
            choice = eval(choice)
            if db== "Food and Price":
                # modify the db_secure_score
                score['db_score'] = min(score['db_score'] + (10-choice), 100)
                score['user_score']= score['user_score']-(8-choice)
                score['invest_score']=score['invest_score']-(8-choice)
                for key in config_food.keys():
                    config_food[key]['cpu'] = config_food[key]['cpu'] + num_choices*0.01*(5-choice)



            if db== "user information":
                # modify the db_secure_score
                score['db_score'] = min(score['db_score'] + (7-choice), 100)
                score['user_score'] = score['user_score'] + (6-choice)
                score['invest_score'] = score['invest_score'] - (7 - choice)
                for key in config_user.keys():
                    config_user[key]['cpu'] = config_user[key]['cpu'] + num_choices*0.01*(4-choice)

        return render_template('main.html',score = score)
    return render_template('queryform.html',form=form)
@app.route('/handel/<type1>/<index1>/<db>',methods=['GET','POST'])
def handelrequest(type1,index1,db):
    index1 = eval(index1)
    if type1 == "audit":
        return redirect(url_for('handelaudit', db=db))
    if type1 == "mask":
        return redirect((url_for('handelmask', db=db)))
    if type1 == "query":
        return redirect((url_for('handelquery', db=db)))


    if str(db) == "Food and Price":
        if type1=="encrypt":
            return
        if type1=="backup":
            config_food[len(dict(config_food).keys())+1]=config_food[index1]
            config_food[len(dict(config_food).keys())]['name']=config_food[len(dict(config_food).keys())]['name']+"-back up"
            score['db_score'] = min(score['db_score']  +10,100)
            score['budget'] = max(score['budget']-1000,0)
            return render_template('config.html', type="Food and Price", config=config_food,score = score)
    if str(db) == "Testing":
        if type1=="encrypt":
            return
        if type1=="backup":
            config_test[len(dict(config_test).keys())+1]=config_test[index1]
            config_test[len(dict(config_test).keys())]['name']=config_test[len(dict(config_test.keys()))]['name']+"-back up"

            score['budget'] = max(score['budget'] - 1000, 0)
            return render_template('config.html', type="Testing", config=config_test,score = score)

    if str(db) == "user information":
        if type1=="encrypt":
            return
        if type1=="backup":
            config_user[len(dict(config_user).keys())+1]=config_user[index1]
            config_user[len(dict(config_user).keys())]['name']=config_user[len(dict(config_user).keys())]['name']+"-back up"
            score['db_score'] = min(score['db_score'] + 15, 100)

            score['budget'] = max(score['budget'] - 1000, 0)
            return render_template('config.html', type="user information", config=config_user,score = score)




