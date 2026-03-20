python -m venv venv
    #Si sale error de permisos en la ejecución de scripts:
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
pip install -r requirements.txt

python insertar_recetas_temp.py
uvicorn main:app --host 0.0.0.0 --port 8050 --reload