# API Practice in FastAPI

## Create Project

Solo se genero una carpeta con un archivo main.py, despues en vscode
se agrego la siguiente configuracion al archivo `.vscode/launch.json`:

```json
{
    // Use IntelliSense para saber los atributos posibles.
    // Mantenga el puntero para ver las descripciones de los existentes atributos.
    // Para más información, visite: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                // main se refiere al nombre de archivo sin la extension
                // app se refiere a la variable generada en la linea app = FastAPI()
                "main:app",
                "--reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

Despues se instalaron las dependencias para FastAPI y conexion a MySQL:

```shell
pip install "fastapi[all]"
# esto para linux
sudo apt-get update && sudo apt-get install -y gcc default-libmysqlclient-dev pkg-config && sudo rm -rf /var/lib/apt/lists/*
pip install mysqlclient
```

Se genero archivo requirements.txt:

```shell
pip freeze > requirements.txt
```

Para poder conectarse a la base de datos se requiere un archivo `.env` en la
raiz del proyecto con la variable `DATABASE_URL`.
