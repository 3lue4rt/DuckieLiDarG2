# DuckieLiDarG2
Este repositorio fue creado para Duckietown Chile 2023 para el proyecto de mapeo de DuckieTown ocupando LiDar.

Uso del paquete:

Hacer el mapa
- Conectarse al robot.
```
ssh duckiebot@duckiebot.local
```
- Lanzar en terminal del robot:
```
roslaunch db_bringup odometry_complete.launch
```
- Lanzar en cada nueva terminal del computador
```
export ROS_MASTER_URI=”http://duckiebot.local:11311/”
``` 
- Lanzar en terminal del computador: roslaunch db_bringup duckiebot.launch
- Lanzar en terminal del computador: roslaunch db_bringup mapping.launch
- Lanzar en terminal del computador: rviz para visualizarlo.
- Si se quiere visualizar el mapa, hay que ir a Open config,rviz en db_bringup y buscar la configuración de mapa de rviz.
- Para guardar el mapa, se debe poner: rosrun map_server map_saver, el cual guardara el mapa. Luego, hay que guardar estos archivos en la carpeta maps de db_bringup.
Localizar el mapa:
- Recuerda hacer sudo apt get a amcl (al igual que robot localization y gmapping antes en el computador).
- Lanzar en terminal del robot: roslaunch db_bringup odometry_complete.launch
- Lanzar en cada nueva terminal del computador export MASTER URI.
- Lanzar en terminal del computador: roslaunch db_bringup duckiebot.launch
- Lanzar en terminal del computador: roslaunch db_bringup localization.launch
- Lanzar en terminal del computador: rviz para visualizarlo.
- Si se quiere visualizar el mapa con las configuraciones listas, hay que ir a Open config, rviz en db_bringup y buscar la configuración de localization de rviz en src de bringup.
