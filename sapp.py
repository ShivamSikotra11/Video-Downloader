# import os
# import time
# import streamlit as st
# from pytube import Playlist, YouTube
# from pytube.exceptions import RegexMatchError, VideoUnavailable

# # Global variables to track the progress and speed
# last_time = time.time()
# last_downloaded = 0

# def on_progress_callback(stream, chunk, bytes_remaining):
#     global last_time, last_downloaded
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining

#     # Calculate the percentage completed
#     percentage = (bytes_downloaded / total_size) * 100

#     # Calculate the download speed
#     current_time = time.time()
#     time_diff = current_time - last_time
#     bytes_diff = bytes_downloaded - last_downloaded

#     if time_diff > 0:
#         speed = bytes_diff / time_diff  # Speed in bytes per second
#         speed_kbps = speed / 1024  # Speed in kilobytes per second

#         # Display the progress and speed using Streamlit
#         st.write(f'Progress: {percentage:.2f}% - Speed: {speed_kbps:.2f} KB/s')

#     # Update the last known values
#     last_time = current_time
#     last_downloaded = bytes_downloaded

# def download_youtube_video(url, video_index, output_path='.'):
#     try:
#         # Create a YouTube object with progress callback
#         yt = YouTube(url, on_progress_callback=on_progress_callback)

#         # Get the highest resolution stream
#         stream = yt.streams.get_highest_resolution()

#         # Define the filename with index and video title
#         sanitized_title = ''.join(c if c.isalnum() or c in (' ', '-') else '_' for c in yt.title)
#         filename = f"{video_index + 1}_{sanitized_title}.mp4"
#         file_path = os.path.join(output_path, filename)

#         # Download the video with the specified filename
#         st.write(f"\nDownloading '{yt.title}' as '{filename}'...")
#         stream.download(output_path, filename=filename)
#         st.write(f"\nDownloaded '{yt.title}' successfully as '{filename}'!")
#     except RegexMatchError:
#         st.error("Regex match error: YouTube URL format is incorrect.")
#     except VideoUnavailable:
#         st.error("Video unavailable: This video may be private or deleted.")
#     except Exception as e:
#         st.error(f"Error: {e}")

# def download_playlist_videos(playlist_url, start_video, end_video, output_path='.'):
#     try:
#         # Create a Playlist object
#         playlist = Playlist(playlist_url)

#         # Get all the video URLs in the playlist
#         videos = playlist.video_urls

#         # Ensure start_video and end_video are within bounds
#         start_video = max(0, start_video - 1)
#         end_video = min(len(videos), end_video)

#         # Download videos in the specified range
#         for idx, video_url in enumerate(videos[start_video:end_video], start=start_video):
#             st.write(f"\nDownloading video {idx + 1 - start_video} of {end_video - start_video}: {video_url}")
#             download_youtube_video(video_url, idx, output_path)

#     except RegexMatchError:
#         st.error("Regex match error: YouTube URL format is incorrect.")
#     except VideoUnavailable:
#         st.error("Video unavailable: This video may be private or deleted.")
#     except Exception as e:
#         st.error(f"Error: {e}")

# # Streamlit UI
# st.title('YouTube Video Downloader')

# # Input fields for user to enter playlist URL, start video index, and end video index
# playlist_url = st.text_input('Enter the YouTube Playlist URL:')
# start_video = st.number_input('Enter the start video index (starting from 1):', min_value=1, value=1)
# end_video = st.number_input('Enter the end video index (starting from 1):', min_value=1, value=1)

# # Text input for choosing the directory to save the videos
# save_path = st.text_input('Enter or paste the full directory path to save the videos:', '.')

# if st.button('Download Videos'):
#     if playlist_url and os.path.isdir(save_path):
#         download_playlist_videos(playlist_url, int(start_video), int(end_video), save_path)
#     elif not playlist_url:
#         st.warning('Please enter a valid Playlist URL.')
#     elif not os.path.isdir(save_path):
#         st.warning('Please enter a valid directory path to save the videos.')







# import os
# import time
# import streamlit as st
# from pytube import Playlist, YouTube
# from pytube.exceptions import RegexMatchError, VideoUnavailable

# # Global variables to track the progress and speed
# last_time = time.time()
# last_downloaded = 0

# def on_progress_callback(stream, chunk, bytes_remaining):
#     global last_time, last_downloaded
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining

#     # Calculate the percentage completed
#     percentage = (bytes_downloaded / total_size) * 100

#     # Calculate the download speed
#     current_time = time.time()
#     time_diff = current_time - last_time
#     bytes_diff = bytes_downloaded - last_downloaded

#     if time_diff > 0:
#         speed = bytes_diff / time_diff  # Speed in bytes per second
#         speed_kbps = speed / 1024  # Speed in kilobytes per second

#         # Display the progress and speed using Streamlit
#         st.write(f'Progress: {percentage:.2f}% - Speed: {speed_kbps:.2f} KB/s')

#     # Update the last known values
#     last_time = current_time
#     last_downloaded = bytes_downloaded

# def download_youtube_video(url, video_index):
#     try:
#         # Create a YouTube object with progress callback
#         yt = YouTube(url, on_progress_callback=on_progress_callback)

#         # Get the highest resolution stream
#         stream = yt.streams.get_highest_resolution()

#         # Get the path to the Downloads folder
#         download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

#         # Define the filename with index and video title
#         sanitized_title = ''.join(c if c.isalnum() or c in (' ', '-') else '_' for c in yt.title)
#         filename = f"{video_index + 1}_{sanitized_title}.mp4"
#         file_path = os.path.join(download_folder, filename)

#         # Download the video with the specified filename
#         st.write(f"\nDownloading '{yt.title}' as '{filename}' to Downloads folder...")
#         stream.download(download_folder, filename=filename)
#         st.write(f"\nDownloaded '{yt.title}' successfully as '{filename}' in Downloads folder!")
#     except RegexMatchError:
#         st.error("Regex match error: YouTube URL format is incorrect.")
#     except VideoUnavailable:
#         st.error("Video unavailable: This video may be private or deleted.")
#     except Exception as e:
#         st.error(f"Error: {e}")

# def download_playlist_videos(playlist_url, start_video, end_video):
#     try:
#         # Create a Playlist object
#         playlist = Playlist(playlist_url)

#         # Get all the video URLs in the playlist
#         videos = playlist.video_urls

#         # Ensure start_video and end_video are within bounds
#         start_video = max(0, start_video - 1)
#         end_video = min(len(videos), end_video)

#         # Get the path to the Downloads folder
#         download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

#         # Download videos in the specified range
#         for idx, video_url in enumerate(videos[start_video:end_video], start=start_video):
#             st.write(f"\nDownloading video {idx + 1 - start_video} of {end_video - start_video}: {video_url}")
#             download_youtube_video(video_url, idx)

#     except RegexMatchError:
#         st.error("Regex match error: YouTube URL format is incorrect.")
#     except VideoUnavailable:
#         st.error("Video unavailable: This video may be private or deleted.")
#     except Exception as e:
#         st.error(f"Error: {e}")

# # Streamlit UI
# st.title('YouTube Video Downloader')

# # Input fields for user to enter playlist URL, start video index, and end video index
# playlist_url = st.text_input('Enter the YouTube Playlist URL:')
# start_video = st.number_input('Enter the start video index (starting from 1):', min_value=1, value=1)
# end_video = st.number_input('Enter the end video index (starting from 1):', min_value=1, value=1)

# # Button to trigger video download
# if st.button('Download Videos'):
#     if playlist_url:
#         download_playlist_videos(playlist_url, int(start_video), int(end_video))
#     else:
#         st.warning('Please enter a valid Playlist URL.')








import os
import time
import streamlit as st
from pytube import Playlist, YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

# Global variables to track the progress and speed
last_time = time.time()
last_downloaded = 0

def on_progress_callback(stream, chunk, bytes_remaining):
    global last_time, last_downloaded
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    # Calculate the percentage completed
    percentage = (bytes_downloaded / total_size) * 100

    # Calculate the download speed
    current_time = time.time()
    time_diff = current_time - last_time
    bytes_diff = bytes_downloaded - last_downloaded

    if time_diff > 0:
        speed = bytes_diff / time_diff  # Speed in bytes per second
        speed_kbps = speed / 1024  # Speed in kilobytes per second

        # Display the progress and speed using Streamlit
        st.write(f'Progress: {percentage:.2f}% - Speed: {speed_kbps:.2f} KB/s')

    # Update the last known values
    last_time = current_time
    last_downloaded = bytes_downloaded

def download_youtube_video(url, video_index, download_folder):
    try:
        # Create a YouTube object with progress callback
        yt = YouTube(url, on_progress_callback=on_progress_callback)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Define the filename with index and video title
        sanitized_title = ''.join(c if c.isalnum() or c in (' ', '-') else '_' for c in yt.title)
        filename = f"{video_index + 1}_{sanitized_title}.mp4"
        file_path = os.path.join(download_folder, filename)

        # Download the video with the specified filename
        st.write(f"\nDownloading '{yt.title}' as '{filename}' to Downloads folder...")
        stream.download(download_folder, filename=filename)
        st.write(f"\nDownloaded '{yt.title}' successfully as '{filename}' in Downloads folder!")
    except RegexMatchError:
        st.error("Regex match error: YouTube URL format is incorrect.")
    except VideoUnavailable:
        st.error("Video unavailable: This video may be private or deleted.")
    except Exception as e:
        st.error(f"Error: {e}")

def download_playlist_videos(playlist_url, start_video, end_video):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Get all the video URLs in the playlist
        videos = playlist.video_urls

        # Ensure start_video and end_video are within bounds
        start_video = max(0, start_video - 1)
        end_video = min(len(videos), end_video)

        # Get the path to the Downloads folder
        download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Download videos in the specified range
        for idx, video_url in enumerate(videos[start_video:end_video], start=start_video):
            st.write(f"\nDownloading video {idx + 1 - start_video} of {end_video - start_video}: {video_url}")
            download_youtube_video(video_url, idx, download_folder)

    except RegexMatchError:
        st.error("Regex match error: YouTube URL format is incorrect.")
    except VideoUnavailable:
        st.error("Video unavailable: This video may be private or deleted.")
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit UI
st.title('YouTube Video Downloader')

# Input fields for user to enter playlist URL, start video index, and end video index
playlist_url = st.text_input('Enter the YouTube Playlist URL:')
start_video = st.number_input('Enter the start video index (starting from 1):', min_value=1, value=1)
end_video = st.number_input('Enter the end video index (starting from 1):', min_value=1, value=1)

# Button to trigger video download
if st.button('Download Videos'):
    if playlist_url:
        download_playlist_videos(playlist_url, int(start_video), int(end_video))
    else:
        st.warning('Please enter a valid Playlist URL.')
