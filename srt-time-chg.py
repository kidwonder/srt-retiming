import sys
import re

def adjust_time(match, mins, secs):
    time_str = match.group()
    hours, minutes, seconds, milliseconds = map(int, re.split('[:,]', time_str))
    print(f"Orig: {match} -> {hours} {minutes} {seconds} {milliseconds}")
    
    # Adjust
    seconds += secs
    total_milliseconds = milliseconds + (seconds * 1000)  # Convert everything to milliseconds
    total_milliseconds += mins * 60 * 1000  # Convert mins to milliseconds and add

    # Compute hours, minutes, seconds, and milliseconds from total_milliseconds
    hours += total_milliseconds // (60 * 60 * 1000)
    total_milliseconds %= (60 * 60 * 1000)

    minutes += total_milliseconds // (60 * 1000)
    total_milliseconds %= (60 * 1000)

    seconds = total_milliseconds // 1000
    milliseconds = total_milliseconds % 1000

    print(f"Adjusted; {hours} {minutes} {seconds} {milliseconds}")
    return "{:02d}:{:02d}:{:02d},{:03d}".format(hours, minutes, seconds, milliseconds)

def adjust_srt_times(file_path, mins, secs):
    time_pattern = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()

    adjusted = time_pattern.sub(lambda m: adjust_time(m, mins, secs), contents)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(adjusted)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: srt_time_chg.py <path_to_srt_file> <minutes_offset> <seconds_offset>")
        sys.exit(1)

    file_path = sys.argv[1]
    mins = int(sys.argv[2])
    secs = int(sys.argv[3])

    adjust_srt_times(file_path, mins, secs)
    print(f"Adjusted times in {file_path} by {mins} minutes and {secs} seconds.")

