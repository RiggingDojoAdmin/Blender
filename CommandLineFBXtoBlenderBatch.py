# 2020
# alphaBuild
# Rigging Dojo
# help@riggingdojo.com
# Batch convert fbx with aligned armature bones to individual blender files.
# Script help staring point https://blender.stackexchange.com/questions/34537/how-to-batch-convert-between-file-formats

#How to use
# Edit the convert directory to the path where your source files live (the blender files will also be saved here)
# Must run from comand prompt on windows put blender in your env. path 
# Open a command prompt and change to directory where this script lives
# From the cmd prompt blender -b -P CommandLineFBXtoBlenderBatch.py
# Once it runs you should now have a blender file that matches your source FBX in name.

#Path to FBX files, using r to do raw string and not care about file path slash
CONVERT_DIR = r"path to source FBX files"
import os

def file_iter(path, ext):
	for dirpath, dirnames, filenames in os.walk(path):
		for filename in filenames:
			ext = os.path.splitext(filename)[1]
			if ext.lower().endswith(ext):
				if ext == ".fbx":
					yield os.path.join(dirpath, filename)
					
import bpy

def reset_blend():
	bpy.ops.wm.read_factory_settings(use_empty=True)
	
def convert_recursive(base_path):
	for filepath_src in file_iter(base_path, ".fbx"):
		filepath_dst = os.path.splitext(filepath_src)[0] + ".blend"
		
		print("Converting %r -> %r" % (filepath_src, filepath_dst))
		
		#reset blender to default state
		reset_blend()
		
		#import the fbx file and set settings like bone orientation
		result = bpy.ops.import_scene.fbx (filepath=filepath_src, automatic_bone_orientation=True, global_scale=100) 
		
		#make sure file is loaded before saving.
		if not "FINISHED" in result:
			print(f"-- unable to process file {filepath_src}" )
			continue
			
		#save the blender file
		bpy.ops.wm.save_as_mainfile(filepath=filepath_dst)
		
if __name__ == "__main__":
	convert_recursive(CONVERT_DIR)
