# Character Name Frequency Analyzer

import os

character = 'Malfoy'

# get all txt file name in the path
txt_files = []
for filename in os.listdir('./src'):
    if filename.endswith('.txt'):
        txt_files.append(filename)
txt_files.sort()

count = 0
print(character)
for i, txt_file in enumerate(txt_files):
    with open(f'./src/{txt_file}', 'r') as f:
        tmp_cnt = 0
        line = f.readline()
        while line:
            if character in line:
                count += 1
                tmp_cnt += 1
            line = f.readline()
    print(f'{i+1} :: {tmp_cnt}')
print(f'total : {count}')



"""
TODO
1. (완료) src 폴더 내의 모든 txt 파일에 대해서 수행하기. (파일 이름이 바뀌어도 접근할 수 있도록)
2. 함수화. 캐릭터가 여러명 정의되면 각각의 캐릭터에 대해 여러번 사용해야 하기 때문에
"""