#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import LaserScan
import math

anglemin=-3.14159274101
anglemax=3.14159274101
angle_increment=0.005482709966599941

def rad2grad(angle):
	return angle*360/2/math.pi

class Template(object):
	def __init__(self, args):
		super(Template, self).__init__()
		self.args = args
		self.scan_sub = rospy.Subscriber("/scan", LaserScan,self.callback)


	#def publicar(self):

	def callback(self,msg):
		cosos=[]
		print(msg.ranges[int(round(msg.angle_max/msg.angle_increment))])



def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
