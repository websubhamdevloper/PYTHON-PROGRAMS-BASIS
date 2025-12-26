# YouTube Manager

A command-line Python application for managing YouTube video information. This project allows users to store, view, update, and delete YouTube video details (name and duration) using a simple text-based menu system.

## Features

- **List Videos**: Display all stored YouTube videos with their names and durations
- **Add Video**: Add new YouTube videos to the collection
- **Update Video**: Modify existing video details (name and duration)
- **Delete Video**: Remove videos from the collection
- **Persistent Storage**: All data is saved in a JSON file (`youtube.txt`) and persists between sessions

## Requirements

- Python 3.10 or higher (requires `match` statement support)

## Installation

No additional packages are required. The application uses only Python's built-in `json` module.

## Usage

1. Run the application:
   ```bash
   python youtube_manager.py
   ```

2. Choose an option from the menu:
   - **1**: List all YouTube videos
   - **2**: Add a YouTube video
   - **3**: Update a YouTube video details
   - **4**: Delete a YouTube video
   - **5**: Exit the application

3. Follow the prompts to interact with the application.

## Project Structure

```
Youtube manager using Python/
├── youtube_manager.py    # Main application file
├── youtube.txt           # JSON data file storing video information
└── README.md             # Project documentation
```

## Functions Overview

### `load_data()`
- **Purpose**: Loads video data from the `youtube.txt` file
- **Returns**: A list of video dictionaries. Returns an empty list if the file doesn't exist
- **Behavior**: Handles `FileNotFoundError` gracefully, making it safe to run on first launch

### `save_data_helper(videos)`
- **Purpose**: Saves the current video list to `youtube.txt` in JSON format
- **Parameters**: `videos` - A list of video dictionaries
- **Behavior**: Overwrites the entire file with the current state of the video list

### `list_videos(videos)`
- **Purpose**: Displays all videos in a numbered list format
- **Parameters**: `videos` - A list of video dictionaries
- **Output**: Prints each video with its index, name, and duration

### `add_video(videos)`
- **Purpose**: Adds a new video to the collection
- **Parameters**: `videos` - A list of video dictionaries (modified in-place)
- **Behavior**: 
  - Prompts user for video name and duration
  - Appends new video dictionary to the list
  - Automatically saves data to file

### `update_video(videos)`
- **Purpose**: Updates an existing video's details
- **Parameters**: `videos` - A list of video dictionaries (modified in-place)
- **Behavior**:
  - Displays current video list
  - Prompts for video index to update
  - Validates index range (1 to length of list)
  - Prompts for new name and duration
  - Updates the video and saves to file
  - Displays error message for invalid indices

### `delete_video(videos)`
- **Purpose**: Removes a video from the collection
- **Parameters**: `videos` - A list of video dictionaries (modified in-place)
- **Behavior**:
  - Displays current video list
  - Prompts for video index to delete
  - Validates index range (1 to length of list)
  - Deletes the video and saves to file
  - Displays error message for invalid indices

### `main()`
- **Purpose**: Main application entry point and menu loop
- **Behavior**:
  - Loads existing data on startup
  - Displays menu options in a continuous loop
  - Uses `match` statement to handle user choices
  - Exits when user selects option 5

## Data Flow

This section explains how data moves through the application, from file storage to user interaction and back.

### 1. **Application Startup**
```
Start → main() → load_data() → Read youtube.txt → Parse JSON → Return video list
```
- When the application starts, `main()` calls `load_data()`
- `load_data()` attempts to read `youtube.txt`
- If the file exists, JSON data is parsed into a Python list of dictionaries
- If the file doesn't exist, an empty list is returned
- The video list is stored in the `videos` variable in `main()`

### 2. **Data Structure**
The data is stored as a JSON array of objects:
```json
[
  {"name": "chai aur python", "time": "50 mins"},
  {"name": "chai aur Django", "time": "1hrs"}
]
```
- Each video is represented as a dictionary with `name` and `time` keys
- The entire collection is stored as a list
- This structure is maintained both in memory and in the file

### 3. **Listing Videos (Read Operation)**
```
User selects option 1 → list_videos(videos) → Iterate through list → Display to console
```
- No file I/O occurs; data is already in memory
- The function simply formats and displays the current `videos` list
- Data flow is one-way: Memory → Console Output

### 4. **Adding a Video (Write Operation)**
```
User selects option 2 → add_video(videos) → Get user input → 
Append to videos list → save_data_helper(videos) → Convert to JSON → 
Write to youtube.txt → Return to main loop
```
- User input is captured for name and duration
- A new dictionary is created and appended to the `videos` list (in-memory modification)
- `save_data_helper()` is called, which:
  - Converts the Python list to JSON format
  - Opens `youtube.txt` in write mode (overwrites existing content)
  - Writes the entire updated list to the file
- Data flow: User Input → Memory (list append) → File (JSON write)

### 5. **Updating a Video (Read-Modify-Write Operation)**
```
User selects option 3 → update_video(videos) → list_videos() [display] → 
Get user input (index) → Validate index → Get new details → 
Modify videos[index-1] → save_data_helper(videos) → JSON conversion → 
Write to youtube.txt
```
- First, the current list is displayed for reference
- User provides the index (1-based, displayed to user) and new details
- The application converts to 0-based index for list access (`index - 1`)
- The specific dictionary in the list is replaced with new data
- The entire list is saved to maintain data consistency
- Data flow: Memory (read) → Console (display) → User Input → Memory (modify) → File (write)

### 6. **Deleting a Video (Read-Modify-Write Operation)**
```
User selects option 4 → delete_video(videos) → list_videos() [display] → 
Get user input (index) → Validate index → Delete videos[index-1] → 
save_data_helper(videos) → JSON conversion → Write to youtube.txt
```
- Similar to update operation, starts with displaying current list
- User provides index to delete
- The item is removed from the list using `del` statement
- List is immediately saved to persist the deletion
- Data flow: Memory (read) → Console (display) → User Input → Memory (delete) → File (write)

### 7. **Data Persistence Pattern**
The application follows a simple persistence model:
- **Load once**: Data is loaded at startup into memory
- **Modify in memory**: All operations modify the in-memory list
- **Save immediately**: Each modification operation immediately writes the entire list back to file
- **No incremental updates**: The file is completely overwritten on each save

### 8. **Data Flow Diagram Summary**
```
┌─────────────┐
│ youtube.txt │
└──────┬──────┘
       │ (Read JSON)
       ▼
┌─────────────┐
│ load_data() │
└──────┬──────┘
       │ (Return list)
       ▼
┌─────────────┐
│   main()    │◄──────┐
│   videos    │       │ (Loop back)
└──────┬──────┘       │
       │              │
       ▼              │
┌─────────────┐       │
│ User Choice │       │
└──────┬──────┘       │
       │              │
       ├─► List (Read only)
       ├─► Add (Write)
       ├─► Update (Read-Modify-Write)
       ├─► Delete (Read-Modify-Write)
       │              │
       ▼              │
┌─────────────┐       │
│ save_data() │       │
└──────┬──────┘       │
       │ (Write JSON) │
       ▼              │
┌─────────────┐       │
│ youtube.txt │───────┘
└─────────────┘
```

### Key Points about Data Flow:
1. **Single Source of Truth**: `youtube.txt` is the persistent storage; the `videos` variable in `main()` is the working copy
2. **Immediate Persistence**: Every modification is immediately saved, ensuring data isn't lost
3. **Complete File Rewrite**: Each save operation writes the entire list, not just changes
4. **No Concurrent Access Handling**: The application assumes single-user, single-instance usage
5. **Error Handling**: File read errors are handled, but write errors are not explicitly caught

## Example Data File

The `youtube.txt` file contains JSON-formatted data:
```json
[{"name": "chai aur python", "time": "50 mins"}, {"name": "chai aur Django", "time": "1hrs"}]
```

## Limitations

- No input validation for duplicate videos
- No input validation for time format
- No error handling for file write operations
- Single-user application (no concurrency handling)
- Complete file rewrite on each save (inefficient for large datasets)

## Future Enhancements

Potential improvements could include:
- Input validation and sanitization
- Search functionality
- Sorting options
- Export/import features
- Better error handling
- Database backend for scalability

