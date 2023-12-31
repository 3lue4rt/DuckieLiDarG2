#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32, Float32 #importa mensajes de ROS tipo String y Int32
from sensor_msgs.msg import Joy # impor mensaje tipo Joy
from geometry_msgs.msg import Twist, Point # importar mensajes de ROS tipo geometry / Twist
from duckietown_msgs.msg import Twist2DStamped
from duckietown_msgs.msg import WheelsCmdStamped 
from time import time

class Template(object):
    def __init__(self, args):
        super(Template, self).__init__()
        self.args = args
        #sucribir a joy 
        self.sub = rospy.Subscriber("/duckiebot/joy", Joy, self.callback)
        #publicar la intrucciones del control en possible_cmd
        self.publi = rospy.Publisher("/duckiebot/wheels_driver_node/wheels_cmd", WheelsCmdStamped, queue_size = 10)
	self.distanciaX = rospy.Publisher("/duckiebot/distancia_X", Float32, queue_size = 10)
        self.twist = WheelsCmdStamped()
	self.time = time()
	self.buttons = [0,0,0,0]
	self.tiempoactual = 0
        self.odomx = 0
    def callback(self,msg):
        self.buttons[0] = msg.buttons[2]
        self.buttons[1] = msg.buttons[0]
        self.buttons[2] = msg.buttons[1]
	self.buttons[3] = msg.buttons[3]
	self.RB = msg.buttons[12]
        self.LB = msg.buttons[11]
       # print(self.buttons[0], self.buttons[1], self.buttons[2], self.buttons[3])
       # self.twist.omega = 0
	#if z!=1 and p!=1:
	maxspeed=1
        self.twist.vel_right = maxspeed*(self.buttons[1]-0.05-self.buttons[0]+(self.RB-self.LB))
        self.twist.vel_left = maxspeed*(self.buttons[1] - self.buttons[0]+(-self.RB+self.LB))
	###if x!=1 and p!=1:
	#	self.twist.vel_right = z*0.7 - 0.05
	#	self.twist.vel_left = z*0.7
	#if x!=1 and z!=1:
	#	self.twist.vel_right = p*0.85 - 0.05
	#	self.twist.vel_left = p*0.85
	
        self.publi.publish(self.twist.header,self.twist.vel_left, self.twist.vel_right)
	
    def tiempo(self,tiempo_a=0):
	time_current = time()
	msg = Float32()
	t0 = 0
	while self.buttons[0]==1:
		t0=time() - time_current
		t=self.tiempoactual + t0
		#print(t)
		self.odomx= t*0.3468 + 0.0745
		odometria = t*0.3468 + 0.0745
		#if self.buttons[1] == 0:
		#	break
                msg.data = self.odomx
		self.distanciaX.publish(msg)
	self.tiempoactual += t0
	if self.buttons[2] ==1:
		self.tiempoactual = 0
        msg.data = self.odomx
        self.distanciaX.publish(msg)

def main():
    rospy.init_node('test') #creacion y registro del nodo!
    rospy.loginfo("ha empezado joy")
    obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba
    rate = rospy.Rate(20)
    #objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

    while not rospy.is_shutdown():
	obj.tiempo() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers
        rate.sleep()	

if __name__ =='__main__':
    main()




# t_current = time()

# cuando hagan update de el calculo usar
# t = time() - t_current 
# t_current = time()
