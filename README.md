# Alter timestamps in a subtitle (srt) file
Usage: srt_time_chg.py <path_to_srt_file> <minutes_offset> <seconds_offset>

This will adjust all timestamps in the subtitle file by the provided number of minutes and seconds.

* alters the file in place
	- make a backup file for safety
* offsets can be positive or negative values

## TODO
1. add option for total seconds or milliseconds offsets
2. check different subtitle file types for regex differences, toggle on the file extension
3. option to backup original file prior to modification

## Possible additions
* Ability to add "watermark" entries
	- search for "gaps" in times to insert advertisements or promotional text
	- maximum number of inserts to perform
	- minimum time between inserts
	- possible "scrolling" message options
	- possible location and removal of existing "watermarks" entries
