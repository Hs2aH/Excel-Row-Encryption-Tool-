
import pandas as pd
import os
import random
import string
import subprocess

def generate_random_password(length=8):
    """Generates a random 5-digit password."""
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choices(characters, k=length))

def encrypt_file(input_filename, output_filename, password):
    """Encrypts a file using OpenSSL with AES."""
    command = f"openssl enc -aes-256-cbc -salt -in {input_filename} -out {output_filename} -k {password} -pbkdf2"
    subprocess.run(command, shell=True)

def main():
    # Load Excel file
    excel_file = './Book1.xlsx'  # Change to your Excel file's name
    df = pd.read_excel(excel_file)

    # Prepare directory to store files
    output_dir = 'encrypted_rows'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open a log file to store file names and encryption keys
    log_filename = os.path.join(output_dir, 'encryption_log.csv')
    with open(log_filename, 'w') as log_file:
        log_file.write('filename,password\n')

        # Process each row in the DataFrame
        for index, row in df.iterrows():
            row_data = row.to_csv(index=False).encode('utf-8')
            temp_filename = os.path.join(output_dir, f'temp_row_{index}.csv')
            encrypted_filename = os.path.join(output_dir, f'encrypted_row_{index}.enc')

            # Write the row data to a temporary file
            with open(temp_filename, 'wb') as temp_file:
                temp_file.write(row_data)

            # Generate a random 3-digit password
            password = generate_random_password()

            # Encrypt the file
            encrypt_file(temp_filename, encrypted_filename, password)

            # Write the log entry
            log_file.write(f'{encrypted_filename},{password}\n')

            # Clean up the temporary file
            os.remove(temp_filename)

if __name__ == "__main__":
    main()
