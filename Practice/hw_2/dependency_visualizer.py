# dependency_visualizer.py

"""
Dependency Visualizer Tool

This script is a command-line tool for visualizing the dependency graph of an Ubuntu package,
including its transitive dependencies. It parses the package information from the repository
without using third-party tools and outputs the result as Graphviz code.

Usage:
    python dependency_visualizer.py -p <path_to_visualizer> -n <package_name> -o <output_file> -u <repo_url>

Example:
    python C:\Users\user\PycharmProjects\pythonProject\hw_2\dependency_visualizer.py -p C:\Users\user\Graphviz\bin\dot -n bash -o bash_dependencies.dot -u http://archive.ubuntu.com/ubuntu/dists/focal/main/binary-amd64/
    """

import argparse
import urllib.request
import gzip
import io
from collections import defaultdict
import sys

def download_packages_file(repo_url):
    """
    Download and decompress the Packages.gz file from the repository URL.

    Args:
        repo_url (str): The base URL of the repository.

    Returns:
        str: The decompressed content of the Packages file.

    Raises:
        Exception: If there is an error downloading or decompressing the file.
    """
    packages_url = repo_url.rstrip('/') + '/Packages.gz'
    try:
        with urllib.request.urlopen(packages_url) as response:
            compressed_data = response.read()
            with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as f:
                packages_data = f.read().decode('utf-8')
        return packages_data
    except Exception as e:
        raise Exception(f"Error downloading or decompressing Packages.gz: {e}")

def parse_packages_data(packages_data):
    """
    Parse the Packages data and extract package information.

    Args:
        packages_data (str): The content of the Packages file.

    Returns:
        dict: A dictionary mapping package names to their dependencies.
    """
    packages_info = {}
    current_package = {}
    for line in packages_data.split('\n'):
        if line.strip() == '':
            if 'Package' in current_package:
                package_name = current_package['Package']
                depends = current_package.get('Depends', '')
                depends = [dep.strip().split(' ')[0] for dep in depends.split(',')] if depends else []
                packages_info[package_name] = depends
            current_package = {}
        else:
            if ':' in line:
                key, value = line.split(':', 1)
                current_package[key.strip()] = value.strip()
    return packages_info

def build_dependency_graph(package_name, packages_info):
    """
    Build the dependency graph for the given package.

    Args:
        package_name (str): The name of the package to analyze.
        packages_info (dict): A dictionary mapping package names to their dependencies.

    Returns:
        dict: A dictionary representing the dependency graph.

    Raises:
        Exception: If the package is not found in the packages_info.
    """
    if package_name not in packages_info:
        raise Exception(f"Package {package_name} not found in repository.")

    graph = defaultdict(set)
    visited = set()

    def dfs(pkg):
        if pkg in visited:
            return
        visited.add(pkg)
        graph[pkg]  # Ensure the package is added to the graph even if it has no dependencies
        dependencies = packages_info.get(pkg, [])
        for dep in dependencies:
            graph[pkg].add(dep)
            dfs(dep)

    dfs(package_name)
    return graph


def generate_graphviz_code(graph):
    """
    Generate Graphviz code from the dependency graph.

    Args:
        graph (dict): The dependency graph.

    Returns:
        str: The Graphviz code representing the dependency graph.
    """
    lines = ['digraph G {']
    for pkg, deps in graph.items():
        for dep in deps:
            lines.append(f'    "{pkg}" -> "{dep}";')
    lines.append('}')
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description='Visualize package dependencies.')
    parser.add_argument('-p', '--path', help='Path to the program for visualizing graphs.', required=True)
    parser.add_argument('-n', '--name', help='Name of the package to analyze.', required=True)
    parser.add_argument('-o', '--output', help='Path to the output file.', required=True)
    parser.add_argument('-u', '--url', help='URL of the repository.', required=True)
    args = parser.parse_args()

    try:
        packages_data = download_packages_file(args.url)
        packages_info = parse_packages_data(packages_data)
        graph = build_dependency_graph(args.name, packages_info)
        graphviz_code = generate_graphviz_code(graph)
        # Output the code to the screen
        print(graphviz_code)
        # Write the code to the output file
        with open(args.output, 'w') as f:
            f.write(graphviz_code)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
