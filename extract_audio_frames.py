import os
import cv2

# --- Step 1: Extract Audio using FFmpeg ---
video_path = "demo_video.mp4"  # Make sure this video exists in the project folder
audio_path = "audio.wav"

# This will extract the audio from video using ffmpeg
os.system(f"ffmpeg -i {video_path} -vn -acodec pcm_s16le -ar 44100 -ac 2 {audio_path}")

print("✅ Audio extracted successfully!")

# --- Step 2: Extract Frames using OpenCV ---
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

vidcap = cv2.VideoCapture(video_path)
fps = int(vidcap.get(cv2.CAP_PROP_FPS))  # Frames per second
frame_interval = fps  # Extract 1 frame per second
count = 0

while True:
    success, image = vidcap.read()
    if not success:
        break
    frame_id = int(vidcap.get(cv2.CAP_PROP_POS_FRAMES))
    if frame_id % frame_interval == 0:
        frame_file = os.path.join(output_dir, f"frame_{count}.jpg")
        cv2.imwrite(frame_file, image)
        count += 1

vidcap.release()
print(f"✅ {count} frames extracted successfully!")
