# Небольшой проект по автоматизации тестирования UI.
В данном проекте реализована автоматизация тестирования UI с использованием GitHub Actions и генерацией Allure-отчетов в GitHub Pages.

# ![example workflow](https://github.com/IlyaYaP/UI-test-automation/actions/workflows/python-package-conda.yml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/-pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/stable/contents.html/)
[![Allure](https://img.shields.io/badge/-Allure-464646?style=flat-square&logo=Allure)](http://allure.qatools.ru/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions/)
[![GitHub%20Pages](https://img.shields.io/badge/-GitHub%20Pages-464646?style=flat-square&logo=GitHub%20Pages)](https://pages.github.com/)
[![GitHub%20Pages](https://img.shields.io/badge/-Selenium-464646?logo=selenium)](https://www.selenium.dev/)
### Стек технологий:
Стек: Python, Pytest, Selenium, Allure.
- Автоматизация тестирования UI с использованием GitHub Actions и генерацией Allure-отчетов в GitHub Pages.

# Локальный запуск:
- Клонируем данный репозиторий:
```
git clone https://github.com/IlyaYaP/UI-test-automation.git
```
- В папке с проектом создаем и активируем виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
```
- Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Устанавливаем allure на Windows(если у вас данная ОС) через scoop.
```
scoop install allure 
```
- Запускаем тесты (Chrome):
```
pytest -s -v --alluredir result_allure --tb=long
```
- Формируем отчет allure.
```
allure serve result_allure
```
