import configparser

# コンフィグファイルから読み込み
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

splitchar = config['DEFAULT']['splitChar']
lastchar = config['DEFAULT']['lastChar']

# ファイルパスを入力
filepath = input()

# 書き込み用配列
lswrite = []

# ファイルオープン
with open(filepath, 'r') as f:
    # ファイルの行数分
    for readitem in f:
        temp = readitem.strip().strip(lastchar).split(splitchar)
        # 分割数が2出ない場合は次の行を読み込む
        if len(temp) != 2:
            continue
        lswrite.append(temp[1] + splitchar + temp[0] + lastchar +'\n')

# 書き込むデータが存在すれば処理する
if len(lswrite) > 0:
    with open(filepath, 'w') as wr:
        for writeitem in lswrite:
            wr.write(writeitem)