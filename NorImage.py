from PIL import Image

def resize_to_match(input_image_path, target_image_path, output_image_path):
    # Open the images
    input_image = Image.open(input_image_path)
    target_image = Image.open(target_image_path)

    # Get the dimensions of the input image
    input_width, input_height = input_image.size

    # Resize the target image to match the dimensions of the input image
    resized_target_image = target_image.resize((input_width, input_height), Image.Resampling.LANCZOS)

    # Save the resized target image
    resized_target_image.save(output_image_path)
    print(f"Resized image saved as {output_image_path}")

# Specify the image paths
input_image_path = 'raw.png'
target_image_path = 'target.png'
output_image_path = 'resized_target.png'

# Perform the resizing
resize_to_match(input_image_path, target_image_path, output_image_path)