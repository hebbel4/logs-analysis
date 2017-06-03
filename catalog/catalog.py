#! /usr/bin/env python
import psycopg2

DBNAME = "news"


def popular_articles():
    """print articles with views and sort in descending order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT title, count(path) AS num FROM articles, log \
    WHERE articles.slug = substring(path from 10 for 100) \
    GROUP BY title ORDER BY num DESC;")
    print("Most popular articles:")
    for (title, num) in c.fetchall():
        print("    {} - {} views".format(title, num))
    print("-" * 70)
    db.close()


def popular_authors():
    """print the most popular authors of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, sum(num) as views from authors, temp_author \
    where authors.id = temp_author.author group by name order by views DESC;")
    print("Most popular authors:")
    for (name, views) in c.fetchall():
        print("    {} - {} views".format(name, views))
    print("-" * 70)
    db.close()


def find_error():
    """find the day more than 1% of requests lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select to_char (date, 'FMMonth FMDD, YYYY'), err/total as ratio \
    from (select time::date as date, \
    count(*) as total, \
    sum((status != '200 OK'):: int):: float as err \
    from log \
    group by date) as errors \
    where err/total > 0.01;")
    print("Days of error more than 1%:")
    for (date, ratio) in c.fetchall():
        print("    {} - {}% errors".format(date, ratio * 100))
    print("-" * 70)
    db.close()

popular_articles()
popular_authors()
find_error()
