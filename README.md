# DuckieLiDarG2
Este repositorio fue creado para Duckietown Chile 2023 para el proyecto de mapeo de DuckieTown ocupando LiDar.

## Requerimientos
Paquetes que deben instalar/clonar en el robot y el computador para que funcione este paquete (dependencias). Los primeros 3 van en el robot y los ultimos 3 en el compu.
- imu_tools: https://github.com/CCNYRoboticsLab/imu_tools.git
- mpu6050_driver: https://github.com/Brazilian-Institute-of-Robotics/mpu6050_driver.git
- rplidar_ros: https://github.com/Slamtec/rplidar_ros.git
- robot_localization: https://github.com/ros-perception/slam_gmapping.git
- gmapping: https://github.com/cra-ros-pkg/robot_localization.git
- map_server y amcl: https://github.com/ros-planning/navigation.git

## Primeros pasos
- Conectarse al robot.
```
ssh duckiebot@duckiebot.local
```
- Lanzar en terminal del **_robot_**: 
```
roslaunch db_bringup odometry_complete.launch
```
- Cuando se abra un terminal del **_computador_** correr:
```
export ROS_MASTER_URI=http://duckiebot.local:11311/
``` 
- Lanzar en terminal del **_computador_**:
```
roslaunch db_bringup duckiebot.launch
```

## Odometría

- Lanzar en terminal del **_computador_**:
```
rviz
```
Se debe añadir el tópico `odometry` que está en "by topic", en /odom/filtered

se tiene que eliminar la covarianza en las opciones del topico y disminuir el tamaño de las flechas.

## Mapping
- Cerrar rviz si lo tienen abierto
- Lanzar en terminal del **_computador_**:
```
roslaunch db_bringup mapping.launch
```
- Lanzar en terminal del **_computador_**:
```
rviz
```
- Si se quiere visualizar el mapa hay 2 opciones:
1. Hay que ir dentro de rviz a Open config,rviz en db_bringup y buscar la configuración de mapa de rviz.
2. Alternativamente pueden añadir los topicos manualmente con `Add` en la esquina inferior izquierda:
<img width="113" alt="Captura de pantalla 2023-12-17 175657" src="https://github.com/3lue4rt/DuckieLiDarG2/assets/142761701/b605cd04-1046-4c1d-a631-956a94081bdb">

Se deben añadir los topicos `Map` que está en "by topic", `TF` que esta en la pestaña principal y adicionalmente se puede agregar `odometry` que está en "by topic", en /odom/filtered

Si agregan `odometry` eliminen la covarianza en las opciones del topico y disminuyan el tamaño de las flechas.

- Para guardar el mapa, se debe poner en una terminal del **_computador_** en un directorio donde lo quieres guardar:
```
rosrun map_server map_saver
```
## Localizar el mapa:
**Importante:** Haber hecho el mapeo antes de ocupar la localizacion.
- Cerrar rviz si lo tienen abierto
- Lanzar en terminal del **_computador_**:
```
roslaunch db_bringup localization.launch
```
- Si se quiere visualizar el mapa con las configuraciones listas, hay que ir a Open config, rviz en db_bringup y buscar la configuración de localization de rviz en src de bringup.

### Videos y fotos de uso
[Video 1](https://youtube.com/shorts/5gO4KQgr8Hc?feature=share)

Foto 1:

<img src="https://github.com/3lue4rt/DuckieLiDarG2/assets/142761701/d7d34ac4-3286-41e4-880a-f19c0fc2b09d" data-canonical-src="https://github.com/3lue4rt/DuckieLiDarG2/assets/142761701/d7d34ac4-3286-41e4-880a-f19c0fc2b09d" width="400" height="400" />

### Background del proyecto 

En la ejecución de este proyecto, inicialmente procedimos a instalar la Unidad de Medición Inercial (IMU) junto con el LIDAR en el duckiebot. Posteriormente, nos dedicamos a comprender el funcionamiento del LIDAR y su manejo, creando el archivo lidar_direc.py para experimentar con sus operaciones. Acto seguido, desarrollamos el paquete "db_description," que incluye en la carpeta urdf el modelo del duckiebot. Para ajustar los parámetros necesarios, realizamos mediciones precisas de las distintas partes del robot.

Simultáneamente, abordamos la obtención de información de la IMU en dos duckiebots diferentes para obtener la orientación de la IMU y la distancia recorrida del robot utilizando la velocidad de los motores. Para la IMU, clonamos el paquete MPU6050_driver (modelo de nuestro robot) en el duckiebot, aunque nos enfrentamos a un desafío al intentar obtener la orientación en tiempo real. Para resolver esto, clonamos el paquete imu_tools y creamos nuestro propio lanzamiento para el filtro de la IMU Madgwick. Sin embargo, surgieron problemas durante la instalación debido a archivos incompatibles con catkin_make, lo que nos obligó a emplear catkin_make_isolated y abordar problemas adicionales de compilación hasta lograr un funcionamiento correcto.

En paralelo, al intentar obtener la distancia recorrida, creamos un nodo personalizado basado en la modificación del archivo joy_challenge para permitir que el duckiebot se moviera en línea recta, superando problemas con las ruedas. Posteriormente, adaptamos un nodo de odometría proporcionado por otro grupo para obtener la información necesaria.

Luego, fusionamos ambos duckiebots y procedimos a instalar los paquetes gmapping y robot localization, aunque enfrentamos complicaciones de compilación. Para resolver este problema, reinstalamos los paquetes imu_tools y rp_lidar, identificando errores relacionados con versiones incorrectas de ROS y cambios en los archivos de rp_lidar.

Continuamos ajustando el archivo ekf.yaml de robot localization para obtener una odometría precisa, y creamos un lanzamiento que incluyera todos los nodos y parámetros necesarios. Este proceso requirió ajustes iterativos de parámetros para refinar la odometría. Finalmente, aplicamos el paquete gmapping para generar el mapa, aprendiendo a sincronizar los lanzamientos de manera efectiva, y utilizamos el paquete amcl para obtener la localización del duckiebot.

Nota: Para mejorar el mapeo y la localización, empleamos cartones decorados en el mapa para alcanzar la altura del LIDAR.

<!--- Renuncia Monica Soler --->
