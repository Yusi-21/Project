# Практическое занятие №2. Менеджеры пакетов

## Задача 1

Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
```
pip install matplotlib
```

```
Requirement already satisfied: matplotlib in /usr/local/lib/python3.10/dist-packages (3.7.1)
Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.3.0)
Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (4.53.1)
Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.4.7)
Requirement already satisfied: numpy>=1.20 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.26.4)
Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (24.1)
Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (10.4.0)
Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (3.1.4)
Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (2.8.2)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
```

```
pip show matplotlib
```

```
Name: matplotlib
Version: 3.7.1
Summary: Python plotting package
Home-page: https://matplotlib.org
Author: John D. Hunter, Michael Droettboom
Author-email: matplotlib-users@python.org
License: PSF
Location: /usr/local/lib/python3.10/dist-packages
Requires: contourpy, cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, python-dateutil
Required-by: arviz, bigframes, datascience, fastai, geemap, imgaug, matplotlib-venn, missingno, mlxtend, music21, plotnine, prophet, pycocotools, seaborn, wordcloud, yellowbrick
```

```
# 1. Импорт и вывод информации о пакете matplotlib
import matplotlib

# Версия пакета
print("Версия matplotlib:", matplotlib.__version__)

# Служебная информация
print("Служебная информация о пакете matplotlib:")
print(matplotlib.__doc__)

# 2. Клонируем репозиторий matplotlib
!git clone https://github.com/matplotlib/matplotlib.git

# 3. Устанавливаем matplotlib из клонированного репозитория
%cd matplotlib
!pip install .
```

```
Версия matplotlib: 3.7.1
Служебная информация о пакете matplotlib:

An object-oriented plotting library.

A procedural interface is provided by the companion pyplot module,
which may be imported directly, e.g.::

    import matplotlib.pyplot as plt

or using ipython::

    ipython

at your terminal, followed by::

    In [1]: %matplotlib
    In [2]: import matplotlib.pyplot as plt

at the ipython shell prompt.

For the most part, direct use of the explicit object-oriented library is
encouraged when programming; the implicit pyplot interface is primarily for
working interactively. The exceptions to this suggestion are the pyplot
functions `.pyplot.figure`, `.pyplot.subplot`, `.pyplot.subplots`, and
`.pyplot.savefig`, which can greatly simplify scripting.  See
:ref:`api_interfaces` for an explanation of the tradeoffs between the implicit
and explicit interfaces.

Modules include:

    :mod:`matplotlib.axes`
        The `~.axes.Axes` class.  Most pyplot functions are wrappers for
        `~.axes.Axes` methods.  The axes module is the highest level of OO
        access to the library.

    :mod:`matplotlib.figure`
        The `.Figure` class.

    :mod:`matplotlib.artist`
        The `.Artist` base class for all classes that draw things.

    :mod:`matplotlib.lines`
        The `.Line2D` class for drawing lines and markers.

    :mod:`matplotlib.patches`
        Classes for drawing polygons.

    :mod:`matplotlib.text`
        The `.Text` and `.Annotation` classes.

    :mod:`matplotlib.image`
        The `.AxesImage` and `.FigureImage` classes.

    :mod:`matplotlib.collections`
        Classes for efficient drawing of groups of lines or polygons.

    :mod:`matplotlib.colors`
        Color specifications and making colormaps.

    :mod:`matplotlib.cm`
        Colormaps, and the `.ScalarMappable` mixin class for providing color
        mapping functionality to other classes.

    :mod:`matplotlib.ticker`
        Calculation of tick mark locations and formatting of tick labels.

    :mod:`matplotlib.backends`
        A subpackage with modules for various GUI libraries and output formats.

The base matplotlib namespace includes:

    `~matplotlib.rcParams`
        Default configuration settings; their defaults may be overridden using
        a :file:`matplotlibrc` file.

    `~matplotlib.use`
        Setting the Matplotlib backend.  This should be called before any
        figure is created, because it is not possible to switch between
        different GUI backends after that.

The following environment variables can be used to customize the behavior::

    .. envvar:: MPLBACKEND

      This optional variable can be set to choose the Matplotlib backend. See
      :ref:`what-is-a-backend`.

    .. envvar:: MPLCONFIGDIR

      This is the directory used to store user customizations to
      Matplotlib, as well as some caches to improve performance. If
      :envvar:`MPLCONFIGDIR` is not defined, :file:`{HOME}/.config/matplotlib`
      and :file:`{HOME}/.cache/matplotlib` are used on Linux, and
      :file:`{HOME}/.matplotlib` on other platforms, if they are
      writable. Otherwise, the Python standard library's `tempfile.gettempdir`
      is used to find a base directory in which the :file:`matplotlib`
      subdirectory is created.

Matplotlib was initially written by John D. Hunter (1968-2012) and is now
developed and maintained by a host of others.

Occasionally the internal documentation (python docstrings) will refer
to MATLAB®, a registered trademark of The MathWorks, Inc.


Cloning into 'matplotlib'...
remote: Enumerating objects: 330379, done.
remote: Counting objects: 100% (57/57), done.
remote: Compressing objects: 100% (45/45), done.
remote: Total 330379 (delta 20), reused 36 (delta 12), pack-reused 330322 (from 1)
Receiving objects: 100% (330379/330379), 444.25 MiB | 24.54 MiB/s, done.
Resolving deltas: 100% (229335/229335), done.
/content/matplotlib
Processing /content/matplotlib
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (1.3.0)
Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (4.53.1)
Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (1.4.7)
Requirement already satisfied: numpy>=1.23 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (1.26.4)
Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (24.1)
Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (10.4.0)
Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (3.1.4)
Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib==3.10.0.dev737+g0988fdaeca) (2.8.2)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.7->matplotlib==3.10.0.dev737+g0988fdaeca) (1.16.0)
Building wheels for collected packages: matplotlib
  Building wheel for matplotlib (pyproject.toml) ... done
  Created wheel for matplotlib: filename=matplotlib-3.10.0.dev737+g0988fdaeca-cp310-cp310-linux_x86_64.whl size=8393645 sha256=31adc139b4e0dd8119821b05e5fa9f2b9765915b5465d0ad89ffe1f3d70af460
  Stored in directory: /tmp/pip-ephem-wheel-cache-axetvmbj/wheels/e3/c6/ba/12604b5e54fb221042954e8cd7c062e550f8bfa87810175fd7
Successfully built matplotlib
Installing collected packages: matplotlib
  Attempting uninstall: matplotlib
    Found existing installation: matplotlib 3.7.1
    Uninstalling matplotlib-3.7.1:
      Successfully uninstalled matplotlib-3.7.1
Successfully installed matplotlib-3.10.0.dev737+g0988fdaeca
```
## Задача 2

Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

## Задача 3

Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

## Задача 4

**Следующие задачи можно решать с помощью инструментов на выбор:**

* Решатель задачи удовлетворения ограничениям (MiniZinc).
* SAT-решатель (MiniSAT).
* SMT-решатель (Z3).

Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

## Задача 5

Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![](images/pubgrub.png)

## Задача 6

Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```

## Задача 7

Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

## Полезные ссылки

Semver: https://devhints.io/semver

Удовлетворение ограничений и программирование в ограничениях: http://intsys.msu.ru/magazine/archive/v15(1-4)/shcherbina-053-170.pdf

Скачать MiniZinc: https://www.minizinc.org/software.html

Документация на MiniZinc: https://www.minizinc.org/doc-2.5.5/en/part_2_tutorial.html

Задача о счастливых билетах: https://ru.wikipedia.org/wiki/%D0%A1%D1%87%D0%B0%D1%81%D1%82%D0%BB%D0%B8%D0%B2%D1%8B%D0%B9_%D0%B1%D0%B8%D0%BB%D0%B5%D1%82
