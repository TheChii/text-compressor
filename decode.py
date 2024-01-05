import zlib
import base64

def decompress_file(input_path, output_path):
    try:
        with open(input_path, 'r') as file:
            code = file.read()

        # Decode base64
        decoded_code = base64.b64decode(code)

        # Decompress zlib
        decompressed_text = zlib.decompress(decoded_code).decode('utf-8')

        # Write the decompressed text to the output file
        with open(output_path, 'w') as output_file:
            output_file.write(decompressed_text)

        
    except Exception as e:
        print(f"Error decoding and decompressing: {e}")

if __name__ == "__main__":
    input_file = input("Input file path:")
    output_file = input("Output file path:")

    decompress_file(input_file, output_file)
