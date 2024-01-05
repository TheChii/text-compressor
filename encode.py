import zlib
import base64

def compress_file(file_path, output_path):
    with open(file_path, 'r') as file:
        text = file.read()

    compressed_data = zlib.compress(text.encode('utf-8'), 9)
    base64_encoded = base64.b64encode(compressed_data)

    with open(output_path, "wb") as f:
        f.write(base64_encoded)

if __name__ == "__main__":
    input_file = input("Input file path:")
    output_folder = input("Output folder path:")

    compress_file(input_file, output_folder)
