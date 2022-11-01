import random
light=("#FFFFFF","#FFFAFA","#F0F8FF","#F5FFFA")
#白、白桃、白青、白緑

import random
vivid=("#FF4500","#7B68EE","#DC143C")
#オレンジ、薄紫、赤

import random
dark=("#000000","","#2f4f4f","#191970")
#黒、暗緑、暗紺

print(random.choice(light))

print(random.choice(vivid))

print(random.choice(dark))
c=random.choice(dark)

f = open('C:\\Users\\a\\mygit\\xbp\\de12\\python\\randomweb.html', 'w') #HTMLファイルを開く f=でhtmlに埋め込み
f.write('<!DOCTYPE html>')
f.write('<html lang="jp">')
f.write('\n')  #改行
f.write('<body>')
f.write('\n')
f.write('<font color="' +c+'">')  #色指定
f.write('\n')
f.write('<font color="' +c+'">')
f.write('\n')
f.write('</body>')


# <head>
#     <link rel="stylesheet" href="./css/style.css">   
#     <!-- ⑥↓タイトルを変えてみよう -->
#     <title>〇〇のテストページ</title>
#     <!-- ⑤スタイルシートの設定をしよう -->
#     <!-- h1.htmlからある行をコピペしてくればOK -->
# </head>
# <body bgcolorc:\Users\a\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\code\electron-sandbox\workbench\workbench.html="#008080" text="#ffffff"></body>
# <body>
f.close()
