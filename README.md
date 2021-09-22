# SD-Tarea-1
# Configuración del proyecto

## Si se usa Windows:
Instalación de la extención "Ubuntu 18.04" o "Ubuntu 20.04"

## Para todo OS:

## Instalar redis:
```
sudo apt-get install redis-server
```

## Reiniciar servidor de redis
```
sudo service redis-server restart
```
## Iniciar cliente
```
redis-cli
```

## Configurar la politica de redis // Nota: Esto depende de la memoria que esté utilizando Redis en el pc, puede variar.
```
Config set maxmemory-policy allkeys-lru
config set maxmemory 1300000B
```

# Instrucciones de ejecución:

## Ejecutar código
```
python app.py
python searchserver.py
```
## Para visualizar las consultas se utiliza: "Postman" y "Another Redis Desktop Manager"
## En postman, la consulta en post se utilizará la dirección
```
127.0.0.1:5000/llenar
```
Esto permite visualizar el número de "keys" y cuales son

## Para consultar un producto se realiza un get  con la dirección 
```
127.0.0.1:5000/search?sol=Producto
```
