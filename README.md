# XSS Scan Script

Este repositorio contiene un script en Python llamado `xss_scan.py`, diseñado para detectar vulnerabilidades de XSS (Cross-Site Scripting) en aplicaciones web. Este script automatiza el proceso de búsqueda de posibles inyecciones de código en los parámetros de las URL de una web, ayudando a identificar riesgos de seguridad.

## Características

- **Detección automática de vulnerabilidades XSS:** El script escanea páginas web en busca de puntos vulnerables a inyección de código.
- **Análisis de URL individual:** El script escanea una URL individual proporcionada como argumento en la línea de comandos.
- **Resultados en consola:** El script muestra los resultados del escaneo, indicando posibles vulnerabilidades, directamente en la consola.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instalado:

- Python 3.x
- Módulos necesarios que pueden ser instalados con `pip`:

  ```bash
  pip install requests

### Ejecución del Script

1. Clona este repositorio:

   git clone https://github.com/tu-usuario/xss-scan.git
   cd xss-scan

2. Ejecuta el script de la siguiente manera:

   python xss_scan.py --url 'URL' [--cookies 'COOKIES_JSON_STRING_OR_FILE_PATH']

   - `URL`: La dirección web que deseas escanear en busca de vulnerabilidades XSS (obligatorio).
   - `COOKIES_JSON_STRING_OR_FILE_PATH`: (Opcional) Cookies para la sesión HTTP. Puede ser una cadena JSON o la ruta a un archivo JSON.

### Ejemplo

   python xss_scan.py --url 'https://ejemplo.com'

   Ejemplo con cookies proporcionadas como cadena JSON:
   python xss_scan.py --url 'https://ejemplo.com' --cookies '{"session_id": "12345", "token": "abc"}'

   Ejemplo con cookies proporcionadas desde un archivo JSON:
   python xss_scan.py --url 'https://ejemplo.com' --cookies /ruta/a/tus_cookies.json

El script realizará un análisis en busca de vulnerabilidades XSS en la URL proporcionada. Los resultados se mostrarán en la consola, indicando cualquier punto de la aplicación donde se hayan encontrado posibles problemas.

### Parámetros adicionales

Además del parámetro `--url`, el script ahora incluye opciones para el manejo de cookies:

- **`--cookies`**: Permite especificar las cookies que se utilizarán en las solicitudes HTTP. Este parámetro es opcional.
    - **Como cadena JSON**: Puedes pasar las cookies directamente como una cadena JSON en la línea de comandos.
      Ejemplo: `--cookies '{"nombre_cookie1": "valor1", "nombre_cookie2": "valor2"}'`
    - **Como ruta a un archivo JSON**: Alternativamente, puedes proporcionar la ruta a un archivo que contenga las cookies en formato JSON.
      Ejemplo: `--cookies /ruta/a/cookies.json`
    - **Formato JSON esperado**: El contenido del JSON (ya sea como cadena o en un archivo) debe ser un objeto simple de pares clave-valor, donde cada clave es el nombre de la cookie y cada valor es el valor de la cookie.
      Ejemplo de contenido para `cookies.json`:
      ```json
      {
        "PHPSESSID": "2acijd30vevs4hvhmbdefq42t7",
        "security": "low"
      }
      ```

El script puede aceptar otras configuraciones dependiendo de su implementación (e.g. scan de múltiples URLs, opciones de salida, etc.), ajusta las opciones según el código.

