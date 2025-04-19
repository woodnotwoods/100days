import os

# Base directory for the 100days project
base_dir = "100days"

# Create folders for each day
for day in range(1, 101):
    folder_name = f"day_{day:02}"  # Format as day_01, day_02, etc.
    folder_path = os.path.join(base_dir, folder_name)

    # Create the folder
    os.makedirs(folder_path, exist_ok=True)

    # Create the README.md file
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(
            f"# Day {day:02}\n\nThis folder contains the work, projects, and exercises for **Day {day:02}** of the 100 Days of Code: The Complete Python Bootcamp course.\n")
