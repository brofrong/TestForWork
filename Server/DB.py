import psycopg2
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def connect():
    conn = None
    try:
        params = config()

        print('Connecting to the postgreSQL')
        conn = psycopg2.connect(**params)
        print('Connection is Ok')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn

def insertPost(conn,name,src,about,tags):
    cur = conn.cursor()
    cur.execute("INSERT INTO post (languagename,imgsrc,about,tags) Values(%s,%s,%s,%s)",
        (name,src,about,tags))
    conn.commit()
    cur.close
    return conn

def getPosts(conn):
    ret = {}
    cur = conn.cursor()
    cur.execute("SELECT * from post")
    ret = cur.fetchall()
    cur.close
    return ret

def likepost(conn,id):
    countLikes = 0
    cur = conn.cursor()
    cur.execute("SELECT likes FROM post WHERE id=%s",(id,))
    countLikes = cur.fetchall()[0][0]
    if(countLikes is None):
        countLikes =0
    
    cur.execute("UPDATE post set likes=%s where id=%s",(countLikes+1,id))
    conn.commit()
    cur.close

def dislikepost(conn,id):
    countLikes = 0
    cur = conn.cursor()
    cur.execute("SELECT dislikes FROM post WHERE id=%s",(id,))
    countLikes = cur.fetchall()[0][0]
    if(countLikes is None):
        countLikes =0
    
    cur.execute("UPDATE post set dislikes=%s where id=%s",(countLikes+1,id))
    conn.commit()
    cur.close


if __name__ == '__main__':
    connect()