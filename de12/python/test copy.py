for i in range(1,4): #コロンが入っていることに注意
    print(i,"人目") #タブでずらしていることに注意！
    name=input("名前を入れてください--")
    waist=float(input("腹囲を入れてください（小数点も可）--"))
    age=int(input("年齢を入れてください（整数）--"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>=85:
        print(name,"さん、内臓脂肪蓄積注意です")
    elif waist<=40:
        print(name,"さん、内臓脂肪蓄積がなさすぎます")
    else:
        print(name,"さん、腹囲は問題ありません")

# 出力結果
# 0 人目
# 1 人目
# 2 人目