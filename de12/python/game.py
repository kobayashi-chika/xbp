from unicodedata import east_asian_width
from numpy import size
#あなたが飼いたいペットを生成します。

name=int(input("名前をつけてください。"))
ookisa=int(input("大きさは？1-3(小さい⇔大きい)で答えてください。"))
kawaisa=int(input("かわいさは？1-3(かわいい⇔かっこいい）で答えてください。"))
seibetu=int(input("性別は？オス=１、メス=２で答えてください。"))
seikaku=int(input("性格は？１＝甘えん坊、２＝勇敢、３＝臆病、４＝狂暴、５＝ツンデレ"))
tokutyou=int(input("特徴は？１＝食いしん坊、２＝散歩好き、３＝眠たがり、４＝、５＝"))
print(ookisa,"の",name,seibetu,"「」")

if seibetu==1:
    print(name"くん")
elif seibetu==2:
    print(name"ちゃん")


 and age>=40:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")