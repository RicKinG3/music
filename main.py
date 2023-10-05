import os

def split_file(input_file, lines_per_file=500):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    namef, s = extract_file_info(input_file)

    for i in range(0, len(lines), lines_per_file):
        chunk = lines[i:i + lines_per_file]
        output_file = f'{namef}_{i // lines_per_file + 1}.txt'

        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.writelines(chunk)


def extract_file_info(file_path):
    base_name = os.path.basename(file_path)  # Получить имя файла из пути
    file_name, file_extension = os.path.splitext(base_name)  # Разделить имя файла и расширение

    return file_name, file_extension


if __name__ == "__main__":
    input_file = "txt/spotify_like.txt"
    split_file(input_file)
    input_file = "txt/misha.txt"
    split_file(input_file)
    input_file = "txt/yandex.txt"
    split_file(input_file)