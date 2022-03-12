import pathlib as pl
import re


def verificador_de_formato(entrada):
    pattern = re.compile(r'\d{4}[-]\d{2}[-]\d{2}[_]\d{2}[.]\d{2}\[(\w+)]')
    matches = pattern.finditer(str(entrada))
    for match in matches:
        return match

    return 'PADRÃO INCORRETO'


def corretor_de_diretorio(entrada):
    parents = str(entrada.parent)
    entrada = str(entrada)

    parents = parents + "\\"
    folder = entrada.replace(parents, "")

    return folder


file_directory = r'C:\Users\Sávio Miranda\Downloads'
file_directory = pl.Path(file_directory)

for file_obj in file_directory.iterdir():
    if file_obj.is_dir():
        folder_verified = corretor_de_diretorio(file_obj)
        correct_pattern = verificador_de_formato(folder_verified)

        if correct_pattern == 'PADRÃO INCORRETO':
            print(f'A pasta < {folder_verified} > está FORA DO PADRÃO.')

        else:
            print(f'A pasta < {folder_verified} > está no PADRÃO.')
