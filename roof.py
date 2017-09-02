import mcpi.minecraft as minecraft;
import mcpi.block as block;
import math;

mc = minecraft.Minecraft.create(); #address="localhost",port=4711)
playerPos=mc.player.getPos();
playerTile=mc.player.getTilePos();

mc.postToChat("API Test!");

entityIds=mc.getPlayerEntityIds();
FirstEntityId=entityIds[0];
#playerAngle=mc.player.getRotation();

playerAngle=0;

mc.player.setPos(playerPos.x,playerPos.y+2,playerPos.z);

roof_length=9
roof_width=6

#mc.setBlocks(playerPos.x,playerPos.y,playerPos.z,playerPos.x+roof_width-1,playerPos.y+5,playerPos.z+roof_length-1,block.AIR);

#mc.setBlocks(playerPos.x,playerPos.y,playerPos.z,playerPos.x+roof_width-1,playerPos.y,playerPos.z+roof_length-1,block.WOOD_PLANKS);

for y in range(0,roof_length):
	for x in range(0,roof_width):
		mc.setBlock(playerPos.x+x,playerPos.y+x,playerPos.z+y,block.Block(block.STAIRS_WOOD.id,0));

mc.setBlocks(playerPos.x+roof_width-1,playerPos.y,playerPos.z,playerPos.x+roof_width-1,playerPos.y+roof_width-2,playerPos.z+roof_length-1,block.WOOD_PLANKS);
# LOG mc.setBlocks(playerPos.x+roof_width-1,playerPos.y,playerPos.z,playerPos.x+roof_width-1,playerPos.y,playerPos.z+roof_length-1,block.Block(block.WOOD.id,1));

for i in range(0,roof_width-1):
	mc.setBlocks(playerPos.x+roof_width-1,playerPos.y+i,playerPos.z,playerPos.x+1+i,playerPos.y+i,playerPos.z,block.WOOD_PLANKS);
	mc.setBlocks(playerPos.x+roof_width-1,playerPos.y+i,playerPos.z+roof_length-1,playerPos.x+1+i,playerPos.y+i,playerPos.z+roof_length-1,block.WOOD_PLANKS);
