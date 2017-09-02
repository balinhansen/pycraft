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


mc.postToChat((playerPos.x,playerPos.y,playerPos.z));
mc.setBlocks(playerPos.x-10,playerPos.y,playerPos.z-10,playerPos.x+10,playerPos.y+10,playerPos.z+10,block.FIRE);
