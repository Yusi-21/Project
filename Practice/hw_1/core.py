import os
import tarfile
import time
import logging
import xml.etree.ElementTree as ET

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Emulator:
    def __init__(self, config_path):
        self.config = self.read_config(config_path)
        self.vfs_path = self.config['vfs_path']
        self.username = self.config['username']
        self.hostname = self.config['hostname']

        self.current_dir = ''
        self.init_vfs()

        self.start_time = time.time()
        logger.debug('Emulator started')

    def read_config(self, config_path):
        tree = ET.parse(config_path)
        root = tree.getroot()
        vfs_path = root.find('vfs_path').text
        username = root.find('username').text
        hostname = root.find('hostname').text
        logger.debug('Config read: vfs_path=%s, username=%s, hostname=%s', vfs_path, username, hostname)
        return {'vfs_path': vfs_path, 'username': username, 'hostname': hostname}

    def init_vfs(self):
        self.tar_ref = tarfile.open(self.vfs_path, 'r')
        logger.debug('VFS initialized: vfs_path=%s', self.vfs_path)

    def ls(self):
        logger.debug('Listing files in current directory: %s', self.current_dir)
        files = [f for f in self.tar_ref.getnames() if f.startswith(self.current_dir)]
        current_dir_files = set()

        for f in files:
            relative_path = f.replace(self.current_dir, '', 1).lstrip('/')
            if '/' not in relative_path:
                current_dir_files.add(relative_path)
            else:
                dir_name = relative_path.split('/')[0]
                current_dir_files.add(dir_name)

        return "\n".join(sorted(current_dir_files))

    def cd(self, path):
        logger.debug('Changing directory: %s', path)

        if path == '..':
            if self.current_dir:
                self.current_dir = os.path.normpath(os.path.join(self.current_dir, '..'))
                if self.current_dir == '.':
                    self.current_dir = ''
            return f"Changed directory to {self.current_dir}"

        new_path = os.path.join(self.current_dir, path)
        if not new_path.endswith('/'):
            new_path += '/'

        if any(name.startswith(new_path) for name in self.tar_ref.getnames()):
            self.current_dir = new_path
            return f"Changed directory to {self.current_dir}"
        else:
            return f"cd: {path}: No such file or directory"

    def tail(self, file_path, n=10):
        full_file_path = os.path.join(self.current_dir, file_path).lstrip('/')
        logger.debug('Getting last %d lines from %s', n, full_file_path)

        # Проверяем, существует ли файл
        if full_file_path not in self.tar_ref.getnames():
            return f"tail: {file_path}: No such file"

        # Извлекаем файл из архива
        with self.tar_ref.extractfile(full_file_path) as file:
            lines = file.readlines()
            # Декодируем байтовые строки в обычные строки
            decoded_lines = [line.decode('utf-8') for line in lines]
            return ''.join(decoded_lines[-n:])

    def rmdir(self, dir_path):
        full_dir_path = os.path.join(self.current_dir, dir_path).rstrip('/') + '/'
        logger.debug('Removing directory: %s', full_dir_path)

        # Проверяем, существует ли директория и пустая ли она
        directory_content = [f for f in self.tar_ref.getnames() if f.startswith(full_dir_path)]
        
        if not directory_content:
            return f"rmdir: {dir_path}: No such directory"
        elif len(directory_content) > 1:
            return f"rmdir: {dir_path}: Directory not empty"
        else:
            # Здесь мы не можем удалить файл из архива напрямую, так как архив "read-only"
            return f"rmdir: {dir_path}: Directory removed (simulation)"

    def exit(self):
        logger.debug('Exiting emulator...')
        self.tar_ref.close()
        exit()
        return "Exiting emulator..."

    def run_command(self, command):
        parts = command.split()
        if not parts:
            return

        cmd = parts[0]
        args = parts[1:]

        if cmd == 'ls':
            result = self.ls()
        elif cmd == 'cd':
            if args:
                result = self.cd(args[0])
            else:
                result = "cd: missing path"
        elif cmd == 'exit':
            result = self.exit()
        elif cmd == 'tail':
            if args:
                result = self.tail(args[0])  # Передаем файл
            else:
                result = "tail: missing file"
        elif cmd == 'rmdir':
            if args:
                result = self.rmdir(args[0])  # Передаем директорию
            else:
                result = "rmdir: missing directory"
        else:
            result = f"{cmd}: command not found"

        return result


if __name__ == '__main__':
    config_path = 'config.xml'  # Путь к конфигурационному файлу
    emulator = Emulator(config_path)
    while True:
        command = input(f"{emulator.username}@{emulator.hostname}:~$ ")
        output = emulator.run_command(command)
        print(output)