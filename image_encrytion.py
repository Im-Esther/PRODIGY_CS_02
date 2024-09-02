from PIL import Image
import random

def encrypt_image(image_path, output_path, key):
    try:
        # Open the image
        image = Image.open(image_path)
        pixels = list(image.getdata())

        # Seed the random number generator with the key and shuffle the pixels
        random.seed(key)
        random.shuffle(pixels)

        # next create a new image and put the shuffled pixels in it
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(pixels)
        encrypted_image.save(output_path)
        print(f"Your Encrypted image is saved as {output_path}")
    except FileNotFoundError:
        print("Error: The specified image file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(image_path, output_path, key):
    try:
        # Open the encrypted image
        image = Image.open(image_path)
        encrypted_pixels = list(image.getdata())

        # Seed the random number generator with the same key
        random.seed(key)

        # Create a list of indices and shuffle them using the same seed
        indices = list(range(len(encrypted_pixels)))
        random.shuffle(indices)

        # Create a list to hold the decrypted pixels in their original order
        decrypted_pixels = [None] * len(encrypted_pixels)

        # Place each pixel back to its original position based on shuffled indices
        for i, index in enumerate(indices):
            decrypted_pixels[index] = encrypted_pixels[i]

        # Create a new image with the decrypted pixels
        decrypted_image = Image.new(image.mode, image.size)
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save(output_path)
        print(f"Your Decrypted image is saved as {output_path}")
    except FileNotFoundError:
        print("Error: The specified image file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def main():
    choice = input("Do you intend to encrypt or decrypt an image? (enter 'encrypt' or 'decrypt'): ").lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice! Please enter 'encrypt' for encryption or 'decrypt' for decryption.")
        return

    # Get user input for image path, output path, and key
    image_path = input("Enter the path to your image file (e.g., C:\\path\\to\\image.jpg): ")
    output_path = input("Enter the path to save your output image (e.g., C:\\path\\to\\output.jpg): ")

    try:
        # Ensure the key is an integer
        key = int(input("Enter the key (integer): "))
    except ValueError:
        print("Invalid key! Please enter a valid integer for the key.")
        return

    # Perform encryption or decryption based on user choice
    if choice == 'encrypt':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
