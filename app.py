from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            filename = download_tiktok_video(url)
            return render_template('result.html', filename=filename)
    return render_template('index.html')

def download_tiktok_video(url):
    if not os.path.exists('static'):
        os.makedirs('static')
    filename = 'static/video.mp4'
    if os.path.exists(filename):
        os.remove(filename)
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': filename,
        'merge_output_format': 'mp4',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return filename

if __name__ == '__main__':
    app.run()