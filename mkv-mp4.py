import ffmpeg
import os

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))

input_file = r"D:\Projects\videos\boss.mkv"
output_file = r'D:\Projects\实训\视频\boss查看数据.mp4'

# stream = ffmpeg.input(input_file)
# stream = ffmpeg.output(stream, output_file)
# ffmpeg.run(stream)

convert_to_mp4(input_file)