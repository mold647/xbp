name=input("名前を入れてください--")
waist=float(input("腹囲を入れてください（小数点も可）--"))
age=int(input("年齢を入れてください（整数）--"))

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")