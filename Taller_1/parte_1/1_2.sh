# Adquirimos el archivo CSV con la información
csv="indices_refraccion.csv"

# Creamos una carpeta para guardar los archivos yml
output_folder="archivos_yml"
mkdir -p "$output_folder"

# Leemos la información del CSV
while IFS=',' read -r categoria fabricante material enlace; do
    # Eliminar los retornos de carro de la URL y el material
    enlace=$(echo "$enlace" | tr -d '\r')
    material=$(echo "$material" | tr -d '\r')

    # Si la categoría no existe, creamos una nueva carpeta
    categoria_folder="$output_folder/$categoria"
    mkdir -p "$categoria_folder"

    # Descargamos el archivo yml y lo guardamos con el nombre del material
    nombre="$material.yml"
    wget -O "$categoria_folder/$nombre" "$enlace"

done < <(tail -n +2 "$csv")







