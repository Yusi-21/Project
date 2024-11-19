# test_dependency_visualizer.py

import pytest
from dependency_visualizer import (
    download_packages_file,
    parse_packages_data,
    build_dependency_graph,
    generate_graphviz_code
)
import urllib.request
from unittest.mock import patch, Mock
import io
import gzip

def test_parse_packages_data():
    packages_data = """
Package: package1
Depends: package2, package3

Package: package2
Depends: package4

Package: package3

Package: package4
"""
    packages_info = parse_packages_data(packages_data)
    expected_info = {
        'package1': ['package2', 'package3'],
        'package2': ['package4'],
        'package3': [],
        'package4': []
    }
    assert packages_info == expected_info

def test_build_dependency_graph():
    packages_info = {
        'package1': ['package2', 'package3'],
        'package2': ['package4'],
        'package3': [],
        'package4': []
    }
    graph = build_dependency_graph('package1', packages_info)
    expected_graph = {
        'package1': {'package2', 'package3'},
        'package2': {'package4'},
        'package3': set(),
        'package4': set()
    }
    assert graph == expected_graph

def test_generate_graphviz_code():
    graph = {
        'package1': {'package2', 'package3'},
        'package2': {'package4'},
        'package3': set(),
        'package4': set()
    }
    code = generate_graphviz_code(graph)
    expected_lines = {
        'digraph G {',
        '    "package1" -> "package2";',
        '    "package1" -> "package3";',
        '    "package2" -> "package4";',
        '}'
    }
    code_lines = set(code.strip().split('\n'))
    assert code_lines == expected_lines

def test_download_packages_file():
    # Mock the urllib.request.urlopen to return a fake Packages.gz content
    fake_packages_content = b"""
Package: package1
Depends: package2, package3

Package: package2
Depends: package4

Package: package3

Package: package4
"""
    fake_compressed_data = io.BytesIO()
    with gzip.GzipFile(fileobj=fake_compressed_data, mode='wb') as f:
        f.write(fake_packages_content)
    fake_compressed_data.seek(0)
    mock_response = Mock()
    mock_response.read.return_value = fake_compressed_data.getvalue()
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = Mock()

    with patch('urllib.request.urlopen', return_value=mock_response):
        packages_data = download_packages_file('http://fake-repo.com')
        assert packages_data.strip() == fake_packages_content.decode('utf-8').strip()

def test_build_dependency_graph_package_not_found():
    packages_info = {
        'package1': ['package2', 'package3'],
        'package2': ['package4'],
        'package3': [],
        'package4': []
    }
    with pytest.raises(Exception) as excinfo:
        build_dependency_graph('nonexistent-package', packages_info)
    assert "Package nonexistent-package not found in repository." in str(excinfo.value)
