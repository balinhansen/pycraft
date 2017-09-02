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

mc.postToChat((playerPos.x,playerPos.y,playerPos.z));

mc.setBlocks(playerPos.x-2,
            playerPos.y-1,
            playerPos.z-3,
            playerPos.x+3,
            playerPos.y+4,
            playerPos.z+5,
            block.AIR);

mc.setBlocks(playerPos.x-2,
            playerPos.y-1,
            playerPos.z-3,
            playerPos.x+3,
            playerPos.y-1,
            playerPos.z+5,
            block.COBBLESTONE);

mc.setBlocks(playerPos.x-1,
            playerPos.y,
            playerPos.z-3,
            playerPos.x+2,
            playerPos.y+4,
            playerPos.z-3,
            block.WOOD_PLANKS);

mc.setBlocks(playerPos.x-1,
            playerPos.y,
            playerPos.z+5,
            playerPos.x+2,
            playerPos.y+4,
            playerPos.z+5,
            block.WOOD_PLANKS);
    
mc.setBlocks(playerPos.x-2,
            playerPos.y,
            playerPos.z-2,
            playerPos.x-2,
            playerPos.y+4,
            playerPos.z+4,
            block.WOOD_PLANKS);

mc.setBlocks(playerPos.x+3,
            playerPos.y,
            playerPos.z-2,
            playerPos.x+3,
            playerPos.y+4,
            playerPos.z+4,
            block.WOOD_PLANKS);


mc.setBlocks(playerPos.x-2,
            playerPos.y,
            playerPos.z-3,
            playerPos.x-2,
            playerPos.y+4,
            playerPos.z-3,
            block.WOOD);

mc.setBlocks(playerPos.x+3,
            playerPos.y,
            playerPos.z-3,
            playerPos.x+3,
            playerPos.y+4,
            playerPos.z-3,
            block.WOOD);

mc.setBlocks(playerPos.x-2,
            playerPos.y,
            playerPos.z+5,
            playerPos.x-2,
            playerPos.y+4,
            playerPos.z+5,
            block.WOOD);

mc.setBlocks(playerPos.x+3,
            playerPos.y,
            playerPos.z+5,
            playerPos.x+3,
            playerPos.y+4,
            playerPos.z+5,
            block.WOOD);

