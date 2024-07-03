import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, concatenate


# Function to merge videos
def merge_videos(input_folder, output_folder):
    try:
        # Get all video files from input folder
        video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov'))]

        if len(video_files) < 2:
            messagebox.showerror("Error", "Please select at least 2 video files.")
            return

        clips = [VideoFileClip(os.path.join(input_folder, file)) for file in video_files]

        # Concatenate clips
        final_clip = concatenate(clips)

        # Save final clip to output folder
        output_file = os.path.join(output_folder, 'merged_video.mp4')
        final_clip.write_videofile(output_file)

        messagebox.showinfo("Success", f"Videos merged successfully. Output saved to:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to handle selecting input folder
def select_input_folder():
    input_folder = filedialog.askdirectory()
    if input_folder:
        input_folder_entry.delete(0, tk.END)
        input_folder_entry.insert(0, input_folder)


# Function to handle selecting output folder
def select_output_folder():
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, output_folder)


# Function to initiate merging process
def merge_videos_gui():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select input and output folders.")
        return

    merge_videos(input_folder, output_folder)


# Create GUI
root = tk.Tk()
root.title("Video Merger")

# Input folder selection
tk.Label(root, text="Input Folder:").grid(row=0, column=0, padx=10, pady=5)
input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_input_folder).grid(row=0, column=2, padx=10, pady=5)

# Output folder selection
tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=5)
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=5)

# Merge button
tk.Button(root, text="Merge Videos", command=merge_videos_gui).grid(row=2, column=1, padx=10, pady=20)

root.mainloop()
