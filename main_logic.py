global user_s_score
global invest_s_score
global db_secure_score
global current_task # track the task number
global score
global config_food
global config_user
global config_test

global current_task_index
global response_index
global task_messages
global response_task_messages

current_task_index=0
response_index = 0
task_messages=[
    {"task":"Please finish the daily code review",
     "content":"sql1.png",
     "options":["hash the password before passing","Everything is fine",
                "perform a input checking before execute the sql"],
     "change_secure":[5,-30,10],
     "change_us":[0,0,0]
     },
    {"task": "Here is a new message from oracle",
      "content":"patch1.png",
     "options": ["assign a test plan for the new patch",
                 "ignore it", "disable the http port in the db and check the bug"],
     "change_secure": [10, 20, 5],
     "change_us": [-10, 0, -5]
     },
    {"task":"Here is a log from the listener",
     "content":"sqlinject.png",
     "options":["report a possible sql injection attack","report a ddos attack",
                "Everything is fine"],
     "change_secure":[5,-30,-20],
     "change_us":[0,0,0]
     },


    {"task":"Here is a new message from oracle",
      "content":"patch4.png",
     "options":["assign a test plan for the new patch","add strict privilege control"
                "ignore it","disable the http port in the db and check the bug"],
     "change_secure":[10,10,20,5],
      "change_us":[-10,-5,0,-5]
     },



]

response_task_messages = [
    {"task":"Your secure level is too low and some one  published our users bank account below",
     "content":"breach.png",
     "options":["Click to response for the data breach accident"],
     "answer":0
     }
    ,
    {
        "task":"The first step is to establish if the data posted to the Internet was genuine,help us "
               "to fill in the blank"
               ,
        "content":"sql-fill.png",
        "options":["table_name,'CREDIT'","table_name,'%user%'","table_name,'%order%'",
                   "table_name,'%CREDIT%'"],
        "answer":3
    },
{
        "task":"Finall you locate that the information comes from bof_pay_details schema and you verify"
               "that the data is leaked"

               ,
        "content":"verify.png",
        "options":["click to see the next step"],
        "answer":0
    },
    {
        "task":"Next, look at the access log for the web server. A search of the access"\
"log looking for the database table BOF_PAY_DETAILS shows just two entries"\
"in 2017, please choose the possible way the attacker hack into db",
        "content":"weblog.png",
        "options":["An admin steals the data","using malicious listener to steal the data when transmitting",
                   "Using sqlmap to find the structure of sql and perform sql injection",
                   "using crawler and find the possible data"],
        "answer":2
    },
    {
        "task":"Now you know that the attacker is using the ip of 192.168.1.56,please choose the next step",
        "content": "clue.png",
        "options":["block the ip address","shut down the server","collecting evidence"],
        "answer":2


    },
    {
        "task":"Now you begin to collect evidence,some of the steps you have done are listed"
               "below, choose the next step for collecting evidence",
        "content":"step.png",
        "options":["Getting copies of the .bash_history files","connect to the db and dump the modified data"],
        "answer":0
    },
    {
        "task":"now you have collected a lot evidence, before shutting down the server,you need to store the data,choose the"
               "correct way to store it",
        "content":"checksum.png",
        "options":["create a checksum for each evidence","encrypt the evidence in case some one modify it",
                   "hash all the evidence and store in a new db"],
        "answer":0
    }


    ]

user_s_score = 70
db_secure_score = 60
invest_s_score = 80
budget = 100000

score = {
    'user_score':user_s_score,
    'db_score':db_secure_score,
    'invest_score':invest_s_score,
    'budget':budget

}

config_food={
    1:{"name":"food list",
              "version":"12.1.3.0",
              "server":"ubuntu 18.04",
              "usage":"15.8G/16G",
"cpu":0.8

    },
    2:{"name":"order history",
              "version":"12.1.3.0",
              "server":"ubuntu 18.04",
              "usage":"11.8G/16G",
                "cpu":0.7

    }

}

config_user = {
    1: {"name": "user information",
               "version": "12.1.3.0",
               "server": "ubuntu 18.04",
               "usage": "10.8G/16G",
"cpu":0.9

               },
    2: {"name": "payment account",
               "version": "8.0.21",
               "server": "ubuntu 14.04",
               "usage": "10.8G/16G",
                "cpu":0.8
               },
    3:{"name": "admin",
               "version": "12.1.3.0",
               "server": "ubuntu 18.04",
               "usage": "2.1G/16G",
"cpu":0.4
               },

}
config_test ={
    1:{
               "name": "playground",
               "version": "18.1.1.0",
               "server": "ubuntu 18.04",
               "usage": "0.8G/16G",
               "cpu":0.1

    }
}


def Calcuate_Fail():
    if user_s_score <= 0 or db_secure_score <= 0 or invest_s_score <= 0:
        return True
    return False

def track_flow():
    raise NotImplemented
