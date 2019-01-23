import sqlite3
from sqlite3 import Error

var_helping_verbs = {'is', 'am', 'are','was','were','shell', 'will','has','have','had'}
var_verb_category1 = {'contain','contains','contained','containing','available','present','presents', 'there'}
var_relational_pronoun = {'what', 'what\'s', 'it', 'it\'s','how','who','whome'}
var_item_name = {'part1','part2','part3','part4','part5','part6','part7','part8','part9','part10'}
var_item_keywords = {'blue','red','green','yellow','accessories'}

var_keywords = { 'protection','2D','3D','drawing','together','with','cap','tool','stp','mate','used','use'}
var_keywords_cat2 = {}

var_orignal_question = ''

def create_connection():
    db_file = "nlp.db"
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def login(user_and_pass):
    conn = create_connection()
    with conn:
        username = user_and_pass[0]
        password = user_and_pass[1]
        print('connectoin established')
        cur = conn.cursor()
        sql ="SELECT * FROM users WHERE name='" + username +"' AND password='"+password+"'"
        cur.execute(sql)
        rows = cur.fetchall()
        if len(rows)>0:
            return 'login,Login OK'
        else:
            return 'login,Login fialed'

    return True

def singup(user_and_pass):
    conn = create_connection()
    with conn:
        print('connectoin established')
        cur = conn.cursor()
        # sql ="SELECT * FROM users WHERE name='" + username +"' AND password='"+password+"'"
        sql = ''' INSERT INTO users(name,password)
                      VALUES(?,?) '''
        try:
            cur.execute(sql, user_and_pass)
            if cur.lastrowid > 0:
                return 'singup,Singup OK'
        except Error as e:
            return 'singup,Singup fialed'

    return True

def manipulate_question(question):
    var_orignal_question = question
    splited_small_question = var_orignal_question.lower().split(' ')
    matching_helping_verb = set(var_helping_verbs) & set(splited_small_question)
    matching_items = set(var_item_name) & set(splited_small_question)
    matching_varb_category1 = set(var_verb_category1) & set(splited_small_question)
    matching_relative_pronoun = set(var_relational_pronoun) & set(splited_small_question)

    return matching_helping_verb

# Interface of the app

while True:
    inputed_question = input("Question: ")
    # inputed_question = 'Is part1 available in blue?'
    # print(manipulate_question(inputed_question))
