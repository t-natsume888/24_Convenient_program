import os
import re
from bs4 import BeautifulSoup

# 保存先ディレクトリ　＆　ファイル名
SaveFileName_Dir = "./bootstrap_elements_list.txt"

def extract_b_elements(directory_path, output_file):

    # <b- で始まるタグを収集するための正規表現
    b_tag_pattern = re.compile(r"<(b-[\w\-]+)")

    b_elements = set()  # 重複を避けるためにセットを使用

    # 指定のフォルダを再帰的に探索
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.vue'):  # .vueファイルのみ対象
                file_path = os.path.join(root, file)

                # ファイル内容を読み込む
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # ファイルをパースして<b-で始まるタグを抽出
                matches = b_tag_pattern.findall(content)
                b_elements.update(matches)  # セットに追加

    # 結果をテキストファイルに出力
    with open(output_file, 'w', encoding='utf-8') as f:
        for element in sorted(b_elements):  # 要素の名前順にソート
            f.write(f"{element}\n")

    print(f"結果：：： saved in: {output_file}")


# 実行する際の設定
if __name__ == "__main__":
    # 検索したいディレクトリを指定
    target_directory = r"C:\Users\USER\saison_24_001\workflow_frontend\pages"  # Nuxtプロジェクトのルートディレクトリ

    # 取得した、値を格納したファイルの保存先
    output_filename = SaveFileName_Dir

    # 関数を実行
    extract_b_elements(target_directory, output_filename)