from flask import Flask, Response, render_template, request
from src.stream import gen_frames, set_channel, get_channel

app = Flask(__name__, template_folder='web/templates', static_folder='web/static', static_url_path='/static')
app.config.from_pyfile('config.py')

@app.route('/video')
def video_feed():
    set_channel(get_channel(), int(app.config.get('STREAM_TIME')))
    return Response(gen_frames(app.config), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/change_channel')
def change_channel():
    index = int(request.args.get("index"))
    set_channel(index, int(app.config.get('STREAM_TIME')))
    return Response("thanks", 200)

@app.route('/metrics')
def metrics():
    return Response("hello metrics", 200)

@app.route('/')
def home():
    context = { "areas": app.config.get("CAMERA_AREAS"), "index": get_channel() }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run()