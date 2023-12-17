# DuckieLiDarG2
Este repositorio fue creado para Duckietown Chile 2023 para el proyecto de mapeo de DuckieTown ocupando LiDar.

## Requerimientos
Paquetes que deben instalar/clonar para que funcione este paquete (dependencias)
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
export ROS_MASTER_URI=”http://duckiebot.local:11311/”
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
Aqui deben ir los links de los videos y fotos -Benja
