#!/bin/bash

# Archivo para almacenar los resultados de las solicitudes
output_file="curl_results.txt"

# Función para realizar una solicitud HTTP y guardar la salida en el archivo
make_request() {
    echo "Haciendo solicitud a $1"
    echo "------------------------------------------" >> "$output_file"
    echo "Solicitud a $1:" >> "$output_file"
    curl -s -X "$2" -H "Content-Type: application/json" -d "$3" "$1" >> "$output_file"
    echo "" >> "$output_file"
}

# Limpiar el archivo de salida antes de realizar nuevas solicitudes
> "$output_file"

# Realizar solicitudes HTTP y guardar la salida en el archivo
make_request "http://localhost:8000/" GET
make_request "http://localhost:8000/users/" GET
make_request "http://localhost:8000/user/1" GET
make_request "http://localhost:8000/user/" POST '{"username": "john_doe", "email": "john.doe@example.com"}'
make_request "http://localhost:8000/user/1" PUT '{"username": "updated_username", "email": "updated.email@example.com"}'
make_request "http://localhost:8000/user/1" DELETE

echo "Solicitudes completadas. Verifica '$output_file' para ver los resultados."
