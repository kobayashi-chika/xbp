import  random #（）内からランダム、print(random.choice())で表示
light=("#FFFFFF","#FFFAFA","#F0F8FF","#F5FFFA")
#白、白桃、白青、白緑

import random
vivid=("#FF4500","#7B68EE","#DC143C")
#オレンジ、薄紫、赤

import random
dark=("#000000","","#2f4f4f","#191970")
#黒、暗緑、暗紺

print(random.choice(light))
l=random.choice(light)

print(random.choice(vivid))
v=random.choice(vivid)

print(random.choice(dark))
d=random.choice(dark)

f = open('C:\\Users\\a\\mygit\\xbp\\de12\\python\\randomweb.html', 'w') #HTMLファイルを開く f.writeでhtmlに埋め込み
f.write('\n')

f.write('<!DOCTYPE html>')
f.write('\n') #改行
f.write('<html lang="jp">')
f.write('\n')
f.write('<head>')
f.write('\n')
f.write('<title>"タイトル"</title>')
f.write('\n')
f.write('</head>')
f.write('\n')

f.write('<body bgcolor="' +d+'" text="#cccccc">') #ランダムリストの中から背景色を貼り付け
f.write('\n')
f.write('<div style="border: ' +v+' solid 1px; border-left:  ' +v+' solid 10px; padding: 20px; background:  ' +l+'; font-size: 100%;">"タイトル"</div>')#ランダムリストの中から枠の色、枠内の色を貼り付け
f.write('\n')
f.write('本文')
f.write('\n')
f.write('</body>')
f.write('\n')
f.write('<html>')
f.close
