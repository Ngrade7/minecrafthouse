#minecrafthouse.py nrg

from mcpi import minecraft 
from mcpi import block 
import time as time 

# Hey Nick nice code! lookin good, if you have any extra time go watch attack on titan its super good :)
# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.15", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z,x+h,y+k,z+l,air)	

def clear_with_air_block(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l,air)	
	
def core(mc,x,y,z,m):
	pass

def engine(mc,x,y,z,m):
	pass

def posta(mc,x,y,z,m):
	pass

def postb(mc,x,y,z,m):
	pass

def layer (mc, x, y, z, s ,e,w, m):
	# s start , e end, m material  , w width, m material 
	w = int(w/2)
	print("w ",w)
	mc.setBlocks(x-w,y,z+s,x+w,y,z+e+1,m)
	

def body(mc,x, y, z):
	clear_with_air_up(mc, x, y-1, z+4, 5,5,5)
	savey = y
	s,e,w = 1,5,5; # -1
	layer(mc, x + 5,y - 1,z+5,s,e,w,5); # -1
	y  = y; s,e,w = 1,5,5 ; # -1 
	
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
	mc.setBlocks(me.x+3, me.y, me.z+2, me.x+3, me.y+1, me.z+2, 64)
	
	# Add glass windows
	mc.setBlock(me.x+5, me.y+1, me.z, 102)
	mc.setBlock(me.x+5, me.y+1, me.z+4, 102)
		
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	print("position ",x,y,z)
	body(mc, x,y,z)
	mc.player.setPos(x -10, y, z + 10)
	

main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
