import warnings
import unittest
import os
import tarfile
from core import Emulator
import tempfile
import shutil
import gc
import logging

logging.captureWarnings(True)  # Перенаправляет варнинги в логгер
logging.basicConfig(level=logging.ERROR)  # Показывает только ошибки

class TestEmulator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Создаем временный конфигурационный файл и виртуальную файловую систему
        cls.config_path = 'test_config.xml'
        with open(cls.config_path, 'w') as config_file:
            config_file.write("""
            <config>
                <vfs_path>virtual_fs.tar</vfs_path>
                <username>user</username>
                <hostname>mycomputer</hostname>
            </config>
            """)
        cls.tar_file = 'virtual_fs.tar'
        cls._generate_virtual_fs_tar(cls.tar_file)

    def test_ls_command(self):
        self.emulator = Emulator(self.config_path)
        result = self.emulator.ls()
        self.assertIn("folder1", result)
        self.assertIn("folder2", result)

    def test_cd_command(self):
        self.emulator = Emulator(self.config_path)
        result = self.emulator.cd('folder1')
        self.assertIn("Changed directory", result)
        self.assertTrue(self.emulator.current_dir.endswith('folder1/'))

        # Проверка несуществующей директории
        result = self.emulator.cd('nonexistent_folder')
        self.assertEqual(result, "cd: nonexistent_folder: No such file or directory")

    def test_tail_command(self):
        self.emulator = Emulator(self.config_path)
        result = self.emulator.tail('folder1/file1.txt', n=5)
        self.assertEqual(len(result.splitlines()), 5)
        self.assertIn("file15", result)

        # Проверка несуществующего файла
        result = self.emulator.tail('nonexistent_file.txt')
        self.assertEqual(result, "tail: nonexistent_file.txt: No such file")

    def test_rmdir_command(self):
        self.emulator = Emulator(self.config_path)
        # Удаление существующей директории
        result = self.emulator.rmdir('folder2')
        self.assertEqual(result, "rmdir: folder2: Directory removed successfully")
        ls_result = self.emulator.ls()
        self.assertNotIn("folder2", ls_result)

        # Удаление несуществующей директории
        result = self.emulator.rmdir('nonexistent_folder')
        self.assertEqual(result, "rmdir: nonexistent_folder: No such directory on filesystem")

    @classmethod
    def _generate_virtual_fs_tar(cls, tar_file):
        # Создание тестового tar архива с виртуальной файловой системой
        base_dir = tempfile.mkdtemp()
        folder1 = os.path.join(base_dir, 'folder1')
        folder2 = os.path.join(base_dir, 'folder2')
        os.makedirs(folder1)
        os.makedirs(folder2)

        # Заполнение файла для тестов
        with open(os.path.join(folder1, 'file1.txt'), 'w') as f:
            for i in range(1, 16):
                f.write(f"This is file{i} in folder1.\n")

        # Используем контекстный менеджер для открытия архива
        with tarfile.open(tar_file, 'w') as tar:
            tar.add(folder1, arcname='folder1')
            tar.add(folder2, arcname='folder2')
            tar.close()

    @classmethod
    def tearDownClass(cls):
        # Удаляем временные файлы после всех тестов
        os.remove(cls.config_path)
        os.remove(cls.tar_file)
        gc.collect()

if __name__ == '__main__':
    unittest.main()
