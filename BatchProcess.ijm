/*
 * Macro template to process multiple images in a folder
 */

#@ File (label = "Input directory", style = "directory") input
#@ File (label = "Output directory", style = "directory") output
#@ String (label = "File suffix", value = ".tif") suffix

// See also Process_Folder.py for a version of this code
// in the Python scripting language.






processFolder(input);

// function to scan folders/subfolders/files to find files with correct suffix
function processFolder(input) {
	list = getFileList(input);
	for (i=0; i<list.length; i++) {
 		filename = input + "\\" + list[i];
 		if (endsWith(filename, ".tif")) {
 		open(filename);
		run("AVI... ", "compression=None frame=7 save=" + output + "\\" + list[i] +".avi");
		close();

		}
	}
}