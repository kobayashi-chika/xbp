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

f = open('C:\\Users\\a\\mygit\\xbp\\de12\\python\\randomweb.html', 'w') #HTMLファイルを開く f.writeでhtmlに埋め込み
f.write('\n')

f.write('<!DOCTYPE html>')
f.write('\n')
f.write('<html lang="jp">')
f.write('\n')
f.write('<head>')
f.write('\n')
f.write('<title>"〇〇のテストページ"</title>')
f.write('\n')  #改行
f.write('</head>')
f.write('あ')
f.write('\n')
f.write('<body>')
f.write('\n')

f.write('\n')
f.write('<font color="' +c+'">')  #色指定
f.write('\n')
f.write('<font color="' +c+'">')
f.write('\n')
f.write('</body>')
f.write('\n')
f.write('<html>')
f.close