import googletrans #翻訳
import vosk        #音声起こし部分
import wave        #おそらくwaveファイルを扱うためのモジュール　pythonに元から存在するやつ
from vosk import Model,KaldiRecognizer 

#mp4形式の動画から音声を抽出して文字起こしをしたかったが、時間的にも技術的にもきついので断念
#voskはwavを使うためwav方式の音声ファイルを認識して文字起こしをできるようにしていきたい
#voskに関するコマンドなのかpythonに元からあるコマンドなのかの判断が難しい
#おそらくmodelはpythonのものでフィールド？を作る？っぽい
#kaldirecognizerがおそらく音声認識部分っぽい
#作らなければならないのは選択するファイル・フォルダの設定　文字起こしの設定　翻訳の設定

#基本的にネットにあったコード丸写しになってしまうがそれは仕方なしと割り切って意味が理解できそうな部分をコメントして理解に徹する

def moziokosi(wave_file,model_path,textfile):#文字起こし部分
    model=Model(model_path)#なにこれ
    wf=wave.open(wave_file,"rb")#waveファイルの読み込みを行っている　ここでのwave_fileは開くファイルのこと　rbがwbになると書き出しを行うっポイ
    rec=KaldiRecognizer(model,wf.getframerate)#voskのモジュール？クラス？のやつでおそらくここで音の解析を行うっポイ
    #getframerateはwaveの付属オブジェクト　サンプリングレートを返す

    #ここで変数の宣言をしているんだと思われる


    with open(textfile,'w',encoding='utf-8') as A:#pythonのopen関数でファイルに対して書き込み、読み込みができる
        while True:
            date =wf.readframes(400000)#オーディオフレーム（ここでは400000フレーム読み込む）を読み込んでbytesオブジェクトにする waveの付属オブジェクト
            if len(date)==0:#dateの中の変数の長さが０ならば
                break
            if rec.AcceptWaveform(date):
                result =rec.Result()
                A.write(result+'\n')
            A.write(rec.FinalResult()+'\n')
        
    wf.close

