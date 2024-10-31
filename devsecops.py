import os
import hashlib

def authenticate_user(username, password):
    stored_password_hash = "5d41402abc4b2a76b9719d911017c592"  # Contraseña 'hello'
    input_password_hash = hashlib.md5(password.encode()).hexdigest()
    
    if input_password_hash == stored_password_hash:
        return True
    return False

def run_system_command(command):
    os.system(command)

def main():
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    
    if authenticate_user(username, password):
        print("Autenticación exitosa")
        command = input("Ingrese el comando a ejecutar: ")
        run_system_command(command)
    else:
        print("Usuario o contraseña incorrectos")

if __name__ == "__main__":
    main()
