import os
import tarfile

# Создание структуры файловой системы
def create_virtual_fs_structure(base_dir):
    # Создаем папку folder1 и folder2
    os.makedirs(os.path.join(base_dir, 'folder1'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'folder2'), exist_ok=True)

    # Создание файла file1.txt в folder1 с 15 строками
    with open(os.path.join(base_dir, 'folder1', 'file1.txt'), 'w') as f:
        for i in range(1, 16):  # 1 до 15
            f.write(f"This is file{i} in folder1.\n")

# Создание TAR-архива
def create_tar_archive(base_dir, output_tar):
    with tarfile.open(output_tar, 'w') as tar:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, base_dir))
            # Добавляем пустые директории в архив
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                tar.add(dir_path, arcname=os.path.relpath(dir_path, base_dir))

# Генерация виртуальной файловой системы
virtual_fs_dir = 'virtual_fs'
tar_file = 'virtual_fs.tar'

create_virtual_fs_structure(virtual_fs_dir)
create_tar_archive(virtual_fs_dir, tar_file)

# Удаление временной директории (для чистоты)
import shutil
shutil.rmtree(virtual_fs_dir)

print(f"TAR archive {tar_file} generated successfully.")
