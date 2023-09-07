# Adquirimos el archivo CSV con la informacion
csv="indices_refraccion.csv"

# Creamos una carpeta para guardar los archivos yml
output_folder="archivos_yml"
mkdir -p "$output_folder"

# Leemos la informacion del CSV
while IFS=',' read -r categoria fabricante material enlace; do
    # Eliminar los retornos de carro de la URL
    enlace=$(echo "$enlace" | tr -d '\r')

    # Si la categoria no existe creamos una nueva carpeta

    categoria_folder="$output_folder/$categoria"
    mkdir -p "$categoria_folder"

    # Miramos el nombre del archivo yml
    nombre=$(basename "$enlace")

    # Descargamo el archivo yml y lo guardamos
    wget -O "$categoria_folder/$nombre" "$enlace"

done < <(tail -n +2 "$csv")







