from flask import Flask, request, jsonify, Response
from flask_cors import CORS;
app = Flask(__name__)
from DB import connect, insertPost, getPosts, likepost,dislikepost

conn = connect()
CORS(app)

@app.route('/like')
def like_post():
    id = request.args.get('id', default = -1, type = int)
    if(id<0):
        return Response(status=400)
    likepost(conn,id)
    return "ok"

@app.route('/dislike')
def dislike_post():
    id = request.args.get('id', default = -1, type = int)
    if(id<0):
        return Response(status=400)
    dislikepost(conn,id)
    return "ok"
    

@app.route('/getposts')
def get_posts():
    return jsonify(getPosts(conn))

@app.route('/newpost', methods=['POST'])
def new_post():
    data = request.get_json()
    insertPost(conn,data.get('name',''),data.get('imgsrc',''),data.get('about',''),data.get('tags',''))
    return "ok"