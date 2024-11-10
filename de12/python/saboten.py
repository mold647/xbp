import random
import sys
koukando=20#サボテンの好感度
death=0#サボテンが死んだかどうかの確認
kauki=0#サボテン購入拒否数の確認
sinkoukando=0#エンディングにかかわるサボテンの真好感度

print("あなたはふとした時に観葉植物が欲しくなりました。")
print("ガーデンに来たあなた。どの植物を買いますか？")


for i in range(1,11):
    sentaku1=int(input("数字を入力してください。１：踊っているサボテン　２：地味なサボテン　３：花の付いたサボテン\n"))
    if sentaku1==1:
        print("みて！　サボテンが踊ってるよ、かわいいね\n")
        break
    elif sentaku1==2:
        print("あなたが変な気を起こしたため１のサボテンは踊るのをやめてしまいました。お前のせいです。あ～あ\n")
        sinkoukando-=1
    elif sentaku1==3:
        print("あなたがえり好みをしたので１のサボテンは踊るのをやめてしまいました。お前のせいです。あ～あ\n")
        sinkoukando-=1
    else:
        print("あなたが選択肢以外の数字を入れたので１のサボテンは枯れてしまいました。お前のせいです。あ～あ\n")
        sinkoukando-=1
    kauki+=1
    print("あなたは改心して新たな観葉植物が欲しくなりました")
    print("どの植物を買いますか？")

if kauki==10:
    sys.exit("あなたのあまりの拒否具合にサボテンは耐えられずすべて爆発しました。おm(ry\n<GAME OVER>")
else:
    print("一日目")
    print("踊っているサボテンを購入したあなた。あなたはサボテンに何をしますか？")





for z in range(2,7):
    sentaku2=int(input("数字を入力してください。１：水をやる　２：日光に当てる　３：振り回す　４：愛をささやく　５：歌いかける\n"))
    if sentaku2==1:
        koukando+=10
        if koukando>=100:
            print("サボテンが爆発しました。お前のせいです。あ～あ\n")
            death=1
            sys.exit()
        else:
            print("サボテンがみずみずしくなりながら踊ってるよ。かわいいね\n")
            
            sinkoukando+=0
    elif sentaku2==2:
        koukando+=random.randint(10,30)
        if koukando>=100:
            print("サボテンが爆発しました。お前のせいです。あ～あ\n")
            death=1
            sys.exit()
        else:
            print("サボテンがテカっているよ。かわいいね\n")

            sinkoukando+=1
    elif sentaku2==3:
        koukando-=random.randint(30,70)
        if koukando>=100:
            print("サボテンが爆発しました。お前のせいです。あ～あ\n")  
            death=1
            sys.exit()
        else:
            print("さぼてんが振り回されてるよ。かわいそうだね\n")
            
            sinkoukando-=2
    if sentaku2==4:
        koukando+=random.randint(20,60)
        if koukando>=100:
            print("サボテンが照れ過ぎて爆発しました。お前のせいです。あ～あ\n")
            death=1
            sys.exit()
        else:
            print("サボテンが照れてるよ。かわいいね")
            
            sinkoukando+=3
    if sentaku2==5:
        koukando+=random.randint(-10,40)
        if koukando>=100:
            print("サボテンが爆発しました。お前のせいです。あ～あ\n")
            death=1
            sys.exit()
        else:
            print("サボテンがリズムに乗ってるよ。かわいいね")
            
            sinkoukando+=2
    print(z,"日目")
    print("今日のお世話の時間です")

if sinkoukando>=6:
    print("サボテンとの日々を送る中でサボテンと心を通じ合えたような気がした...\n<GAME CLEAR--good end>")
elif sinkoukando>=3 and sinkoukando<=5:
    print("サボテンとの日々で、サボテンのことを少しだけ知れた...気がする\n<GAME CLEAR--normal end>")
elif sinkoukando<=2 and sinkoukando>=1:
    print("サボテンとの日々を経たがこのサボテンがなぜ踊っているのかは理解できなかった...\n<GAME END--bad end>")
elif sinkoukando>=-100 and sinkoukando<=1:
    print("サボテンはどうやらあなたのことが気に食わないらしい...そう感じた時にはもう遅かった\n<GAME OVER>")