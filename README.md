# codingD

> [!NOTE]
> Entorno de pruebas para Bootcamp

DevSecOps / Asignación lab 11 (Core) 


> [!CAUTION]
> Programa intencionalmente Vulnerable. Bajo tu propio riesgo

### Vulnerabilidades intencionales:
   - Uso de md5 para el hash de contraseñas: md5 no es seguro para almacenar contraseñas.
   
   - Inyección de comandos: La función run_system_command permite ejecutar comandos del sistema, exponiendo a posibles inyecciones de comandos.

Estas vulnerabilidades deben detectarse fácilmente en un entorno de análisis de seguridad como Jenkins o Bandit.
