'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    # Stream data in fixed-size chunks to achieve O(1) memory usage
    # rather than reading entire file into memory
    while True:
        chunk = file.read(8192)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
