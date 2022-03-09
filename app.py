from crypt import methods
from typing import Dict
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import logging
import random


import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/add/topic', methods=['GET','POST'])
def addTopic():
    if request.method == 'GET':
        return render_template('add-topic.html')
    
    if request.method == 'POST':
        newTopic = request.form
        topicName = newTopic['topicName']
        cur = mysql.connection.cursor()
        topic_insert_query = """INSERT INTO topic (topicName) VALUES (%s) """
        cur.execute(topic_insert_query, [topicName])
        mysql.connection.commit()

        topic_select_query = """SELECT id FROM topic WHERE topicName LIKE %s"""
        topicIdResult = cur.execute(topic_select_query, [topicName])
        if topicIdResult == 1:
            topicId= cur.fetchone()
            articles_select_query = """SELECT * FROM article """
            articlesResult= cur.execute(articles_select_query)
            randomArticleId = random.randint(1,articlesResult)
            article_topic_insert_query = """INSERT INTO articleTopic (articleId,topicId) VALUES (%s,%s) """
            cur.execute(article_topic_insert_query, [randomArticleId,topicId[0]])
            mysql.connection.commit()

        cur.close()
        return 'A new topic is added successfully in the Database'

@app.route('/api/fetch', methods=['GET'])
def getAllArticlesForCertainTopic():
    if 'topic' in request.args:
        topicName = request.args['topic']
        cur = mysql.connection.cursor()
        topic_select_query = """SELECT id FROM topic WHERE topicName LIKE %s"""
        topicIdResult = cur.execute(topic_select_query, [topicName])
        if topicIdResult == 1:
            topicId= cur.fetchone()
            topic_article_select_query = """SELECT articleId FROM articleTopic WHERE topicId LIKE %s"""
            topicArticleResults = cur.execute(topic_article_select_query, [topicId[0]])
            if topicArticleResults >0:
                articles = list()
                topicArticleDetails = cur.fetchall()
                for article in topicArticleDetails:
                    article_select_query = """SELECT articleName FROM article WHERE id LIKE %s"""
                    articleNameResult = cur.execute(article_select_query, [article[0]])
                    if articleNameResult == 1:
                        articleName= cur.fetchone()
                        articles.append(articleName[0])
                return render_template('articles.html', articles=articles)

    else:
        return "Error: No topic field provided. Please specify an id."

@app.route('/api/topics', methods=['GET'])
def viewAllTopics():
    cur = mysql.connection.cursor()
    topics_select_query = """SELECT * FROM topic """
    topicsResults= cur.execute(topics_select_query)
    if topicsResults > 0:
        topicsDetails = cur.fetchall()
        topicArticleDict = dict()
        print(topicsDetails)
        for topicDetails in topicsDetails:
            topic_article_select_query = """SELECT * FROM articleTopic WHERE topicId LIKE %s"""
            topicArticleResults = cur.execute(topic_article_select_query, [topicDetails[0]])
            topicArticleDict[topicDetails[1]] = topicArticleResults
            print(topicArticleDict)
        return render_template('all-topics.html', topicArticleDict=topicArticleDict)
        
if __name__ == "__main__":
    app.run(debug=True)