#!/bin/bash
#


output_directory="/media/bigdisk/converted/"
script_working_dir="/media/bigdisk/movies/"

function mainfunction {
	current_working_dir=$1
	output_structured_directory="$output_directory${current_working_dir//"$script_working_dir"/""}"
	echo $output_structured_directory
	#mkdir $output_structured_directory
	directory="$current_working_dir*"
	for file in $directory; do
		outputfile="$output_directory${file//"$script_working_dir"/""}"
		echo $outputfile
		if [ -d "$file" ]; then
			echo "$file is directory"
		else
			HandBrakeCLI --preset-import-gui customOne -i $file -o $outputfile --audio-lang-list deu,eng --all-audio
		fi
	done
}

mainfunction $1