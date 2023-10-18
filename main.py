import tkinter as tk
import pytube
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.scrolledtext
import tkinter.filedialog
import clipboard

def download_video():
    url = entry.get()
    try:
        youtube = pytube.YouTube(url)
        
        # Get available video streams
        streams = youtube.streams
        
        # Display available resolutions
        resolutions = [str(stream.resolution) for stream in streams]
        resolution = tkinter.simpledialog.askstring("Resolution", "Choose a resolution: {}".format(", ".join(resolutions)))
        
        # Get the selected video stream based on the chosen resolution
        video = streams.get_by_resolution(resolution)
        
        # Download the selected video
        video.download()
        
        tkinter.messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))

def paste_clipboard():
    url = clipboard.paste()
    entry.insert(tk.END, url)

# Create the main window
window = tk.Tk()
window.title("YouTube Downloader")

# Create a label and an entry for the URL
label = tk.Label(window, text="Enter the YouTube video URL:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to trigger the download
button = tk.Button(window, text="Download", command=download_video)
button.pack()

# Create a "paste" button to insert a link from the clipboard
paste_button = tk.Button(window, text="Paste", command=paste_clipboard)
paste_button.pack()

# Start the GUI event loop
window.mainloop()