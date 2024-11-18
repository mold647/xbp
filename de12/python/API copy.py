from vosk import Model, KaldiRecognizer
import wave
import json
from googletrans import Translator

def transcribe_audio(audio_file):
    # Voskモデルのロード
    model = Model("model")  # "model" フォルダにVoskの言語モデルを配置してください
    recognizer = KaldiRecognizer(model, 16000)
    
    # WAVファイルの読み込み
    with wave.open(audio_file, "rb") as wf:
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
            raise ValueError("音声ファイルは16kHz、モノラル、16ビット形式である必要があります。")
        
        recognizer_text = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                recognizer_text += result.get("text", "") + " "
        
        # 最後の部分を取得
        final_result = json.loads(recognizer.FinalResult())
        recognizer_text += final_result.get("text", "")
        
    return recognizer_text

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

# メイン処理
def main(audio_file, target_language):
    try:
        print("音声ファイルを文字起こし中...")
        transcribed_text = transcribe_audio(audio_file)
        print("文字起こし結果:", transcribed_text)
        
        print("翻訳中...")
        translated_text = translate_text(transcribed_text, target_language)
        print("翻訳結果:", translated_text)
    except Exception as e:
        print("エラー:", e)

# 実行例
if __name__ == "__main__":
    AUDIO_FILE = "path/to/audio.wav"  # 音声ファイルのパスを指定
    TARGET_LANGUAGE = "en"  # 翻訳先言語（例: 英語は "en"）
    
    main(AUDIO_FILE, TARGET_LANGUAGE)
