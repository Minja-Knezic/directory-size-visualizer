import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Function to get the size of a directory recursively (including all subdirectories)
def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

# Function to get the size of immediate subdirectories in a given directory
def get_subdirectory_sizes(directory):
    subdirectory_sizes = defaultdict(int)
    
    # Traverse the directory and get the size of each immediate subdirectory
    for dirpath, dirnames, _ in os.walk(directory):
        # We only process the first level of subdirectories
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdirectory_sizes[dirname] = get_directory_size(subdir_path)
        
        # Break after processing the first level of directories
        break
    
    return subdirectory_sizes

# Function to generate the pie chart
def plot_pie_chart(data, threshold, threshold_type):
    total_size = sum(data.values())
    if threshold_type == "MB":
        size_threshold = threshold * 1024 * 1024  # Convert MB to bytes
        filtered_data = {key: value for key, value in data.items() if value >= size_threshold}
        small_data = {key: value for key, value in data.items() if value < size_threshold}
    elif threshold_type == "%":
        size_threshold = (threshold / 100) * total_size
        filtered_data = {key: value for key, value in data.items() if value >= size_threshold}
        small_data = {key: value for key, value in data.items() if value < size_threshold}
    else:
        raise ValueError("Invalid threshold type. Use 'MB' or '%'.")

    if small_data:
        filtered_data["Other"] = sum(small_data.values())
    
    labels = list(filtered_data.keys())
    sizes = list(filtered_data.values())
    
    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
    plt.title('Directory Size Distribution')
    plt.show()

# Function to convert bytes into a human-readable format
def human_readable_size(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} TB"

# Main function to handle user input and start the process
def main():
    directory = input("Enter the directory path to analyze: ")
    
    if os.path.exists(directory):
        # Get the sizes of immediate subdirectories
        subdirectory_sizes = get_subdirectory_sizes(directory)
        
        if subdirectory_sizes:
            print("\nImmediate subdirectory sizes:")
            for subdir, size in subdirectory_sizes.items():
                print(f"{subdir}: {human_readable_size(size)}")
            
            # Get user input for threshold
            threshold_type = input("\nEnter the threshold type ('MB' for size in megabytes or '%' for percentage): ").strip()
            while threshold_type not in ["MB", "%"]:
                print("Invalid input. Please enter 'MB' or '%'.")
                threshold_type = input("Enter the threshold type ('MB' or '%'): ").strip()
            
            try:
                threshold = float(input(f"Enter the threshold value (in {threshold_type}): "))
                if threshold < 0:
                    raise ValueError
            except ValueError:
                print("Invalid threshold value. Please enter a non-negative number.")
                return
            
            # Plot the pie chart for the immediate subdirectories
            plot_pie_chart(subdirectory_sizes, threshold, threshold_type)
        else:
            print("No subdirectories found.")
    else:
        print("The provided directory does not exist.")

if __name__ == "__main__":
    main()
