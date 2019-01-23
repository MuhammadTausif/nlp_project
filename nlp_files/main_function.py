import sqlite3
from sqlite3 import Error

def create_connection():
    db_file = "D:\\Data\\Dev\\Python\\github\\chatterbot\\sqlite\\db\\pythonsqlitechatbot.db"
    db_file = "pythonsqlitechatbot.db"
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def get_distinct_items():
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        sql ="SELECT DISTINCT parameter1 from corpus"
        cur.execute(sql)
        rows = cur.fetchall()
        items = ["%s" % x for x in rows]
        items.append('partnumber123')
        items.append('product123')
        items.append('product456')

    return items

var_questoin = 'What is the right cap for SeriesC_pn 001?'
var_questoin = 'What is the right cap for SeriesC_pn 002?'
var_questoin = 'Share 3D drawing Series D part number 157?'
# var_questoin = 'What is the right cap for SeriesA_pn 007?'
# var_questoin = 'What is the right cap for SeriesA_pn 001?'
# var_questoin= 'What is the right cap for Series D part number 1?'
# var_questoin = 'SeriesC_pn 001 and SeriesC_pn 002 can be combined?'
# var_questoin = 'What is the correct protection cap for SeriesC_pn 001?'
# var_questoin ="Send	the	datasheet	of	product123?"
# var_questoin= 'What is the right cap for SeriesC_pn 001?'
var_questoin = 'Is	partnumber123	available	in	blue?'
var_questoin = 'What is the right cap for SeriesC_pn 004?'
var_questoin = 'What is the right cap for Series D part number 54?'
var_questoin = 'Can	product123	and	product456	be	combined?'
var_questoin = 'Do SeriesA_pn 006 and SeriesC_pn 080 mate together?'
var_questoin = 'Do SeriesC_pn 004 and Series D part number 92 mate together?'
var_questoin = 'Is	partnumber123	available	in	blue?'
var_questoin = 'Is	there	accessories	for	partnumber123?'
var_questoin = 'Send	the	datasheet	of	product123'
var_questoin = 'Can	product123	and	product456	be	combined?'
var_questoin = 'Do	product123	and	product456	fit	together?'

def get_answer(var_question):

    var_items = get_distinct_items()

    var_questoin = var_question.lower()

    selected_items = []
    selected_keyword = []

    keywords_category1 = ['cap','protection', 'tool','available','there','blue','accessories']
    keywords_category2_1 = ['stp','3D', 'drawing','datasheet']
    keywords_category2_2 = ['drawing','2D', 'send','share']
    keywords_category2 = keywords_category2_1 + keywords_category2_2
    keywords_category3_1 = ['mate', 'used', 'use', 'can', 'do']
    keywords_category3_2 = ['together','with', 'togather', 'combined','fit' ]
    keywords_category3 = keywords_category3_1 + keywords_category3_2

    all_keywords = set(keywords_category1) | set(keywords_category2_1) | set(keywords_category2_2)  | set(keywords_category3_1)  | set(keywords_category3_2)  | set(keywords_category2_1)

    for x in var_items:
        if(x.lower() in var_questoin.lower()):
            selected_items.append(x.lower())
            for y in selected_items:
                if y.lower() in x.lower():
                    if y.lower() != x.lower():
                        selected_items.remove(y.lower())
                if x.lower() in y.lower():
                    if y.lower() != x.lower():
                        selected_items.remove(x.lower())


    for x in all_keywords:
        if(x.lower() in var_questoin.lower()):
            selected_keyword.append(x.lower())

    if len(selected_items)==1:
        if(  len(set(keywords_category1) & set(selected_keyword)) > 0):
            if(set(selected_keyword) & {'available','there'}):
                return selected_items[0] + ' ' + selected_keyword[1]+ ' is available.'
            else:
                return selected_items[0] + ' ' +selected_keyword[0]+ ' is available.'
        elif(  len(set(keywords_category2) & set(selected_keyword)) > 0):
            if(set(selected_keyword) & {'send','share'}):
                return 'Please download it from following <a>link</a>.'
    elif len(selected_items) == 2:
        if( len(set(keywords_category3) & set(selected_keyword)) > 0):
            return selected_items[0] + ' and ' + selected_items[1] + ' can be ' + selected_keyword[1]

while True:
    print(get_answer(input('Question: ')))
