# Excel Row Encryption Tool 🛡️📊
This Python script is a security tool designed to automate the encryption of individual rows from an Excel file. It uses OpenSSL with AES-256-CBC encryption to secure each row as a separate file, making it ideal for demonstrating row-level data protection. A log file is automatically generated to map each encrypted file to its unique password.

### 💡 Key Features
+ Row-Level Encryption: Encrypts each row of a spreadsheet individually.

+ AES-256-CBC Encryption: Uses a strong, modern encryption standard via the OpenSSL command-line tool.

+ Unique Passwords: Generates a unique, random password for each row to enhance security.

+ Password Logging: Creates an encryption_log.csv file that securely stores the filenames and their corresponding passwords.

+ Temporary File Cleanup: Manages temporary files, ensuring only the encrypted output and log file remain.

### 🎯 Why This Project Matters
This project serves as an excellent demonstration of practical data security principles. It highlights the importance of protecting data at a granular level and showcases a workflow for securing structured data. It also provides a hands-on example of how to integrate Python scripting with powerful command-line tools like OpenSSL for cryptographic tasks.

### 🛠️ Prerequisites

To run this script, you need to have Python 3.x and OpenSSL installed on your system.

You also need the pandas library, which can be installed with pip:

    pip install pandas

### 🚀 Usage
Place your Excel file (.xlsx or .xls) in the same directory as the main.py script.

Update the excel_file variable in the main.py script with the name of your file.

Run the script from your terminal:

    python main.py

**Output**
Upon successful execution, the script will create a new directory named encrypted_rows/. This directory will contain:

Encrypted files: Individual files for each row (e.g., encrypted_row_0.enc, encrypted_row_1.enc).

Log file: A CSV file named encryption_log.csv containing the decryption passwords.

### ⚠️ Security Considerations & Limitations
Weak Passwords: The script is configured to generate short, 3-character passwords for educational purposes. These are not secure for sensitive data. For real-world use, you should increase the password length.

Log File Security: The encryption_log.csv file contains all the passwords, so it must be protected and stored securely.

No Decryption Script: The current version of the script does not include a decryption function. Decryption must be performed manually using OpenSSL.

Missing Data Integrity: The script focuses on confidentiality but does not include measures for data integrity. In production, you would need to implement an authenticated encryption scheme.
