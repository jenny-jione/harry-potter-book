# Character Name Frequency Analyzer
import os

# get all txt file name in the path
def get_txt_files():
    txt_files = []
    for filename in os.listdir('./src'):
        if filename.endswith('.txt') and filename.startswith('Harry'):
            txt_files.append(filename)
    txt_files.sort()
    return txt_files

def get_character_name():
    with open('./src/character.txt', 'r') as f:
        characters = [line.strip() for line in f.readlines()]
        return characters

def find_character_frequency(txt_file: str, character: str):
    count = 0
    with open(f'./src/{txt_file}', 'r') as f:
        contents = f.read()
        count = contents.count(character)
    return count

if __name__ == "__main__":
    chars = get_character_name()

    txt_files = get_txt_files()

    for char in chars:
        count = 0
        for i, txt_file in enumerate(txt_files):
            cnt = find_character_frequency(txt_file, char)
            count += cnt
            print(f'{i+1}: {cnt}')
        print(f'{char}: {count}')
        print()



"""
TODO
1. (완료) src 폴더 내의 모든 txt 파일에 대해서 수행하기. (파일 이름이 바뀌어도 접근할 수 있도록)
2. (완료) 함수화. 캐릭터가 여러명 정의되면 각각의 캐릭터에 대해 여러번 사용해야 하기 때문에
"""