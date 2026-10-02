from PIL import Image
from rembg import remove

def remove_background(input_path, output_path):
    """Removes the background from an image and saves the result."""
    try:
        # Open the input image
        input_image = Image.open(input_path)
        
        # Remove the background
        output_image = remove(input_image)
        
        # Save the result as a PNG to preserve transparency
        output_image.save(output_path)
        print(f"Success! Background removed and saved as: {output_path}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found. Please check the file name.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Change these filenames to match your input image
    INPUT_IMAGE = "input.jpg" 
    OUTPUT_IMAGE = "output.png"
    
    remove_background(INPUT_IMAGE, OUTPUT_IMAGE)