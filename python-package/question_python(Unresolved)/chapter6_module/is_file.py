# -*- coding: utf-8 -*-

import os
def is_file(file_path):
    """ 파일이름을 전달받아서 파일이 존재 하면 True를 반환하고, 
          존재하지 않으면(또는 파일이 아니면) False를 반환하는 함수를 작성하자
        hint: os.path.isfile
    """
    # 여기 작성

    return os.path.isfile(file_path)


if __name__ == "__main__":
    print is_file("C:\Users\student\Desktop\\namki_game.sh")
    pass

