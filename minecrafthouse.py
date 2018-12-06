#minecrafthouse.py nrg

# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep
from random import randint
import math

def init():
    #mc = Minecraft.create("127.0.0.1", 4711)
    mc = Minecraft.create("10.183.3.25", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z-l,x+h,y+k,z+l,air)	

def house(mc,x,y,z):
	me = mc.player.getTilePos()
	# Build a block of blocks to make the building here wood is no. 5
	mc.setBlocks(me.x+3, me.y, me.z, me.x+7, me.y+2, me.z+4, 45)

	# Remove interior by adding a block of air 0 slightly smaller than previous block
	mc.setBlocks(me.x+4, me.y, me.z+1, me.x+6, me.y+1, me.z+3, 0)

	# Adding a two blocks of air for door
	mc.setBlocks(me.x+3, me.y, me.z+2, me.x+3, me.y+1, me.z+2, 0)

	# Add first window of air, notice the setBlock not setBlocks command.
	mc.setBlock(me.x+5, me.y+1, me.z, 0)

	# Add second window of air on opposite wall
	mc.setBlock(me.x+5, me.y+1, me.z+4, 0)
		
	# Add a door
	mc.setBlocks(me.x+3, me.y, me.z+2,	 me.x+3, me.y+1, me.z+2, 64)

	# Add a bed
	mc.setBlocks(me.x+3, me.y, me.z+4, 26)

		
	# Add glass windows
	mc.setBlock(me.x+5, me.y+1, me.z, 102)
	mc.setBlock(me.x+5, me.y+1, me.z+4, 102)
		
def main():
	mc = init()
	x, y, z = mc.player.getPos()	
	clear_with_air_up(mc,x,y,z,20,20,20)
	house(mc,x,y,z)


main()
