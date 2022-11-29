import os
import platform

class ExecuteDjango():

    def __init__(self) -> None:
        self.clean = os.system('cls')

        self.type_system = platform.system()
        self.version_system = platform.release()

       
    def create_venv_and_activate(self):
        if self.type_system.lower() == 'windows':
            install_virtualvenv = os.system('pip install virtualenv')
            update = os.system('python.exe -m pip install --upgrade pip')
            venv = os.system('python -m venv venv')
            activate = os.system('venv/scripts/activate')
            self.clean = os.system('cls')

        else:
            install_virtualvenv = os.system('pip3 install virtualenv')
            update = os.system('python.exe -m pip install --upgrade pip')
            venv = os.system('python -m venv venv')
            activate = os.system('venv/bin/activate')
            self.clean = os.system('clear')


    def _install_requirements(self, system:str):
        venv = self.create_venv_and_activate()

        if system == 'windows':
            requirements_txt = os.system('pip install -r requirements.txt')
            self.clean = os.system('cls')

        elif system == 'linux':
            requirements_txt = os.system('pip3 install -r requirements.txt')
            self.clean = os.system('clear')


    def _run_application(self, aplication:str) -> str:
        requirements = self._install_requirements(self.type_system.lower())

        if aplication.lower() == 'django':
            os.system('python manage.py runserver')

        elif aplication.lower() == 'flask':
            os.system('python main.py')

        elif aplication.lower() == 'fastapi':
            os.system('python main.py')


if __name__ == '__main__':
    execute = ExecuteDjango()
    execute._run_application('django')
    