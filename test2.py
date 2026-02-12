def otsukare_machine(name):
    # 1. 結合した文字を一度「箱」に入れるか、直接リターンするか選んでください
    # 2. 最後に必ず return を使って結果を出してください
    otsukare = name + "さん、お疲れ様！"
    return otsukare    
# --- 動作確認 ---
if __name__ == "__main__":
    print(otsukare_machine("佐藤")) 
    # 「佐藤さん、お疲れ様！」と出れば完璧です