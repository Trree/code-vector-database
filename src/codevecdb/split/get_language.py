import os


def get_language(file_path):
    file_extension = os.path.splitext(file_path)[1]

    if file_extension == '.py':
        return 'Python'
    elif file_extension == '.java':
        return 'Java'
    elif file_extension == '.cpp' or file_extension == ".cc" or file_extension == '.h':
        return 'Cpp'
    # 添加其他语言的判断条件
    else:
        return 'Unknown'
