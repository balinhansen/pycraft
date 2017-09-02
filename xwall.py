import mcpi.minecraft as minecraft;
import mcpi.block as block;
import math;
import sys;
import re;

mc = minecraft.Minecraft.create(); #address="localhost",port=4711)
playerPos=mc.player.getPos();
playerTile=mc.player.getTilePos();

entityIds=mc.getPlayerEntityIds();
FirstEntityId=entityIds[0];
#playerAngle=FirstEntityId.getRotation();
playerAngle=0;

mc.postToChat((playerPos.x,playerPos.y,playerPos.z));

def remove_wall(inp):
	walls = {
		0:lambda dir: mc.setBlocks(playerPos.x+1,playerPos.y,playerPos.z-14,playerPos.x+1,playerPos.y+10,playerPos.z+15,block.FIRE) if dir==0 else 'false',
		1:lambda dir: mc.setBlocks(playerPos.x-14,playerPos.y,playerPos.z+1,playerPos.x+15,playerPos.y+10,playerPos.z+1,block.FIRE) if dir==1 else 'false',
		2:lambda dir: mc.setBlocks(playerPos.x-1,playerPos.y,playerPos.z-14,playerPos.x-1,playerPos.y+10,playerPos.z+15,block.FIRE) if dir==2 else 'false',
		3:lambda dir: mc.setBlocks(playerPos.x-14,playerPos.y,playerPos.z-1,playerPos.x+15,playerPos.y+10,playerPos.z-1,block.FIRE) if dir==3 else 'false'
		}
	for wall in range(0,4):
		print walls[wall](inp);

args=str(sys.argv[1:]);
# print(args)

results = re.search("(d\=[0-3])",args,re.MULTILINE);
# print(str(results.group(0)));

if (results.group(0)):
#	print("hello world!")
	m=re.search("([0-3])",results.group(0))
	direction=m.group(0)[0];
	print(direction);
	remove_wall(int(direction));
	mc.postToChat("Removing "+direction+" Wall");


#remove_wall(0);
#remove_wall(1);
#remove_wall(2);
#remove_wall(3);
