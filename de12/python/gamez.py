name=input("名前をつけてください。")
ookisa=int(input("大きさは？1-3(小さい⇔大きい)で答えてください。"))
kawaisa=int(input("かわいさは？1-3(かわいい⇔かっこいい）で答えてください。"))
seibetu=int(input("性別は？オス=１、メス=２で答えてください。"))
seikaku=int(input("性格は？１＝甘えん坊、２＝勇敢、３＝臆病、４＝狂暴、５＝ツンデレ"))
tokutyou=int(input("特徴は？１＝食いしん坊、２＝散歩好き、３＝眠たがり、４＝きれい好き、５＝哲学的"))

import random
sk=("ハムスター","モモンガ","フェレット")

import random
sh=("インコ","カメ","フェレット","チワワ")

import random
sc=("カブトムシ","トカゲ","カマキリ")

import random
mk=("ウサギ","ネコ","プードル","コアラ")

import random
mh=("ブタ","サル","アルマジロ")

import random
mc=("ヘビ","ワニ","ワシ","イグアナ")

import random
lk=("シロクマ","アザラシ")

import random
lh=("ゾウ","キリン","カンガルー")

import random
lc=("サメ","ゴリラ","ライオン","チーター")

if ookisa==1 and kawaisa==1:
    print(random.choice(sk),"の")

elif ookisa==1 and kawaisa==3:
    print(random.choice(sc),"の")

elif ookisa==2 and kawaisa==1:
    print(random.choice(mk),"の")

elif ookisa==2 and kawaisa==2:
    print(random.choice(mh),"の")

elif ookisa==2 and kawaisa==3:
    print(random.choice(mc),"の")

elif ookisa==3 and kawaisa==1:
    print(random.choice(lk),"の")

elif ookisa==3 and kawaisa==2:
    print(random.choice(lh),"の") 
    
elif ookisa==3 and kawaisa==3:
    print(random.choice(lc),"の")


print(name)

if seibetu==1:
    print("くん")
elif seibetu==2:
    print("ちゃん")

if seikaku==1 and tokutyou==1:
    print("「ごはんがほしいな♡」")

elif seikaku==1 and tokutyou==2:
    print("「おさんぽにつれてってほしいな♡」")

elif seikaku==1 and tokutyou==3:
    print("「ねんねしたいな♡」")

elif seikaku==1 and tokutyou==4:
   print("「シャンプーしてほしいな♡」")

elif seikaku==1 and tokutyou==5:
    print("「真の賢者は己の愚を知る者だよね♡」")

elif seikaku==2 and tokutyou==1:
    print("「ご飯を探しに行こう！」")

elif seikaku==2 and tokutyou==2:
    print("「ついてきて！外に行こう」")
 
elif seikaku==2 and tokutyou==3:
    print("「さあ、寝よう」")

elif seikaku==2 and tokutyou==4:
    print("「さあ、体を洗って！」")

elif seikaku==2 and tokutyou==5:
    print("「内容のない思考は空虚であり、概念のない直観は盲目なんだよ。」")

elif seikaku==3 and tokutyou==1:
    print("「ごはんがたべたいのだけど…」")

elif seikaku==3 and tokutyou==2:
    print("「すこしそとにいきたいな…」")

elif seikaku==3 and tokutyou==3:
    print("「ねむりたい…」")

elif seikaku==3 and tokutyou==4:
    print("「おふろにいれてほしいのだけど…」")

elif seikaku==3 and tokutyou==5:
    print("「真の賢者は己の愚を知る者だとおもうよ…」")

elif seikaku==4 and tokutyou==1:
    print("「ごはんをよこせ！」")

elif seikaku==4 and tokutyou==2:
    print("「さんぽにつれていけ！」")

elif seikaku==4 and tokutyou==3:
    print("「寝床を用意しろ！」")
elif seikaku==4 and tokutyou==4:
    print("「掃除をしろ！」")

elif seikaku==4 and tokutyou==5:
    print("「ねたみは魂の腐敗だぞ！」")

elif seikaku==5 and tokutyou==1:
    print("「お腹すいてるわけじゃないんだからね」")

elif seikaku==5 and tokutyou==2:
    print("「別に歩きたくなんかないんだからね」")

elif seikaku==5 and tokutyou==3:
    print("「眠くなんてないんだから！」")

elif seikaku==5 and tokutyou==4:
    print("「べつにお風呂なんか入らなくてもいいもん」")

elif seikaku==5 and tokutyou==5:
    print("「たくさん持っている人が豊かなのではなく、たくさん与える人が豊かなんだからね」")