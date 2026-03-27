python -m venv venv
    #Si sale error de permisos en la ejecución de scripts:
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
pip install -r requirements.txt

python insertar_recetas_temp.py
uvicorn main:app --host 0.0.0.0 --port 8050 --reload

# BLOQUEO POR MYSQL
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

# ORDEN DE INICIO
1. API BDD
2. OPC
3. API LECTURA GENERAL
4. API CICLOS
5. API CORRECCIONES
6. API ALARMAS
7. API MAIL
8. API AUTH