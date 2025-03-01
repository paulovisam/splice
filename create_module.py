import os
import shutil
import sys


def merge_folders(source, destination):
    """
    Mescla recursivamente os arquivos e subpastas de 'source' para 'destination'.
    Se um arquivo já existir em 'destination', ele será sobrescrito.
    """
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        dest_item = os.path.join(destination, item)

        # Se for diretório, chama a função recursivamente
        if os.path.isdir(source_item):
            merge_folders(source_item, dest_item)
        else:
            # Se for arquivo, copia para o destino
            # (sobrescrevendo se necessário)
            shutil.copy2(source_item, dest_item)


if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("Uso: python merge_folders.py <pasta_fonte> <pasta_destino>")
    #     sys.exit(1)

    name_module = sys.argv[1]
    # dst = sys.argv[2]
    command = f"cookiecutter cookiecutter-splice --no-input -f module_name={name_module}"
    os.system(command)
    tmp_folder = f"./template-module"
    merge_folders(tmp_folder, './splice')
    os.system(f"rm -R {tmp_folder}")
    print("Mesclagem concluída com sucesso!")
