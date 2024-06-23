import os,re,sys,time,webbrowser


folder_path = input('Full path of the folder you want to VIEW : ')+r'\\'
img_name = os.listdir(folder_path)
all_img = []
all_path = ''

for i in img_name:
  all_img.append(folder_path+i)

html_txt_one = ("<!DOCTYPE html><html lang='ja'>  <head>    <meta charset='utf-8' />    <title>IMAGE VIWER.html</title>    <link rel='stylesheet' href='style.css'>    <script type='text/javascript' src='script.js'></script>    <script type='text/javascript' src='zooming.min.js'></script>    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/luminous-lightbox/2.4.0/luminous-basic.min.css'>    <link rel='preconnect' href='https://fonts.googleapis.com'>    <link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>    <link href='https://fonts.googleapis.com/css2?family=Ubuntu:wght@700&display=swap' rel='stylesheet'>   </head>  <body>    <div id='loading'>      <h1 style='margin-top:100px'>NOW LOADING</h1>      <div class='sk-cube-grid'>        <div class='sk-cube sk-cube1'></div>        <div class='sk-cube sk-cube2'></div>        <div class='sk-cube sk-cube3'></div>        <div class='sk-cube sk-cube4'></div>        <div class='sk-cube sk-cube5'></div>        <div class='sk-cube sk-cube6'></div>        <div class='sk-cube sk-cube7'></div>        <div class='sk-cube sk-cube8'></div>        <div class='sk-cube sk-cube9'></div>      </div>      <p class='loading-text'>If there are too many images, the display will be very slow.(๑-_-๑)</p>      <a id='GOen' class='border_slide_btn' onclick='broke()'>Clear load screen</a>    </div>    <h1>IMAGE VIWER.html</h1>    <div class='grid' >")
html_txt_second = ("</div><script>document.addEventListener('DOMContentLoaded', function () {new Zooming({}).listen('.zoom ')})</script></body></html>")

for i in all_img:
  
  all_path+= '<img src="'+'file://'+i+'"'+' data-action="zoom" class="zoom"'+'alt="'+i+'">'+'\n'

file_name = os.path.dirname(__file__)+'\\html(Viewer)\\'+str(time.time())+r'-index.html'
with open(file_name,mode='w' ,encoding="utf-8") as f:
  f.write(html_txt_one+all_path+html_txt_second)
print('END')
webbrowser.open('file://' + file_name)
