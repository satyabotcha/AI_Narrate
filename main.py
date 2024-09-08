from narration import video_to_narrate
from narration_styles import NARRATION_STYLES 
from webcam import record_video

def main():
    # Ask user if they want to use an existing file or record a new one
    choice = input("Do you want to use an existing video file or record a new one? (existing/record): ").lower()

    if choice == 'record':
        video_path = record_video()  # Call the record_video function from webcam.py
        print(f"Video recorded and saved at: {video_path}")
    else:
        video_path = input("Enter the path to your existing video file: ")
        
    # Display available narration styles
    print("\nAvailable narration styles:")
    for index, key in enumerate(NARRATION_STYLES, 1):
        print(f"{index}. {key.replace('_', ' ').title()}")
    
    # Get user's choice
    while True:
        try:
            choice = int(input("\nEnter the number of your preferred narration style: "))
            if 1 <= choice <= len(NARRATION_STYLES):
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get the chosen style
    chosen_style = list(NARRATION_STYLES.keys())[choice - 1]
    
    # Call video_to_narrate with the chosen style
    video_to_narrate(video_path, chosen_style)

if __name__ == "__main__":
    main()