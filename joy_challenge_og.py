#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 #importa mensajes de ROS tipo String y Int32
from sensor_msgs.msg import Joy # impor mensaje tipo Joy
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from duckietown_msgs.msg import WheelsCmdStamped 


class Template(object):
    def __init__(self, args):
        super(Template, self).__init__()
        self.args = args
        #sucribir a joy 
        self.sub = rospy.Subscriber("/duckiebot/joy" , Joy, self.callback)
        #publicar la intrucciones del control en possible_cmd
        self.twist = WheelsCmdStamped()
        self.publi = rospy.Publisher("/duckiebot/wheels_driver_node/wheels_cmd",WheelsCmdStamped, queue_size = 10) 


    #def publicar(self, msg):
        #self.publi.publish(msg)


    def callback(self,msg):
        a = msg.buttons[0]
	b = msg.buttons[1]
	x = msg.buttons[2]
	y = msg.buttons[3]

	lb, rb = msg.buttons[4], msg.buttons[5]
	lt = msg.axes[2]
	rt = msg.axes[5]

	leftjoy_x = -msg.axes[0]
	leftjoy_y = msg.axes[1]

	rightjoy_x = -msg.axes[3]
	rightjoy_y = msg.axes[4]

	deadzone = 0.2
	file=open("rat.txt","r")
	alfa=float(file.readline())
	beta=float(file.readline())
	ratio=alfa/beta
	file.close()

	if a==1:
		file=open("rat.txt","w")
		file.write(str(alfa+0.01)+"\n")
		file.write(str(beta)+"\n")
		file.close()
        if b==1:
                file=open("rat.txt","w")
                file.write(str(alfa-0.01)+"\n")
                file.write(str(beta)+"\n")
                file.close()
        if x==1:
                file=open("rat.txt","w")
                file.write(str(alfa)+"\n")
                file.write(str(beta+0.01)+"\n")
                file.close()
        if y==1:
                file=open("rat.txt","w")
                file.write(str(alfa)+"\n")
                file.write(str(beta-0.01)+"\n")
                file.close()


	if rb==1:
		print("ratio",ratio)
		print("alfa",alfa)
		print("beta",beta)

	maxspeed=0.75

	self.twist.vel_right=-leftjoy_y*maxspeed*beta
	self.twist.vel_left=-leftjoy_y*maxspeed*alfa

	if lb==1:
		self.twist.vel_right=0
		self.twist.vel_left=0
	"""if left_joy0:
		self.twist.vel_right=lt*maxspeed
		self.twist.vel_left=lt*maxspeed
	if lt<0:
		self.twist.vel_right=-rt*maxspeed
		self.twist.vel_left=-rt*maxspeed

	if rb==1 and lb==1:
		self.twist.vel_left=0
		self.twist.vel_right=0"""

        self.publi.publish(self.twist)
        




def main():
    rospy.init_node('test') #creacion y registro del nodo!

    obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

    #objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

    rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
    main()

