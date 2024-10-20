import unittest
import os
import tarfile
import shutil
from core import Emulator
from generate_vfs import create_virtual_fs_structure, create_tar_archive

class TestVirtualFS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Создаем виртуальную файловую систему перед запуском всех тестов.
        """
        cls.virtual_fs_dir = 'test_virtual_fs'
        cls.tar_file = 'test_virtual_fs.tar'

        # Генерируем виртуальную файловую систему
        create_virtual_fs_structure(cls.virtual_fs_dir)
        create_tar_archive(cls.virtual_fs_dir, cls.tar_file)

        # Генерируем конфигурационный файл для эмулятора
        cls.config_file = 'test_config.xml'
        with open(cls.config_file, 'w') as f:
            f.write(f"""<config>
    <vfs_path>{cls.tar_file}</vfs_path>
    <username>test_user</username>
    <hostname>test_host</hostname>
</config>""")

    @classmethod
    def tearDownClass(cls):
        """
        Удаляем временные файлы после завершения всех тестов.
        """
        if os.path.exists(cls.virtual_fs_dir):
            shutil.rmtree(cls.virtual_fs_dir)
        if os.path.exists(cls.tar_file):
            os.remove(cls.tar_file)
        if os.path.exists(cls.config_file):
            os.remove(cls.config_file)

    def setUp(self):
        """
        Создаем экземпляр эмулятора перед каждым тестом.
        """
        self.emulator = Emulator(self.config_file)

    def test_ls_root(self):
        """
        Тест команды 'ls' в корневой директории.
        """
        result = self.emulator.ls()
        expected = "folder1\nfolder2"
        self.assertEqual(result.strip(), expected)

    def test_cd_and_ls_folder1(self):
        """
        Тест команды 'cd folder1' и 'ls' в директории folder1.
        """
        self.emulator.cd('folder1')
        result = self.emulator.ls()
        expected = "file1.txt"
        self.assertEqual(result.strip(), expected)

    def test_cd_nonexistent(self):
        """
        Тест команды 'cd' с несуществующей директорией.
        """
        result = self.emulator.cd('nonexistent_folder')
        expected = "cd: nonexistent_folder: No such file or directory"
        self.assertEqual(result, expected)

    def test_tail_file(self):
        """
        Тест команды 'tail' для чтения последних строк файла.
        """
        self.emulator.cd('folder1')
        result = self.emulator.tail('file1.txt', 5)
        expected = "This is file11 in folder1.\nThis is file12 in folder1.\nThis is file13 in folder1.\nThis is file14 in folder1.\nThis is file15 in folder1.\n"
        self.assertEqual(result, expected)

    def test_rmdir_nonempty(self):
        """
        Тест команды 'rmdir' на непустую директорию.
        """
        result = self.emulator.rmdir('folder1')
        expected = "rmdir: folder1: Directory not empty"
        self.assertEqual(result, expected)

    def test_rmdir_nonexistent(self):
        """
        Тест команды 'rmdir' с несуществующей директорией.
        """
        result = self.emulator.rmdir('nonexistent_folder')
        expected = "rmdir: nonexistent_folder: No such directory"
        self.assertEqual(result, expected)

    def test_run_unknown_command(self):
        """
        Тест попытки выполнения неизвестной команды.
        """
        result = self.emulator.run_command('unknowncmd')
        expected = "unknowncmd: command not found"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
