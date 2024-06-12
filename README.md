# PathGuard

Secure Programming Challenge Against LFI Threats

## Scenario
In this challenge, participants are tasked with addressing a Local File Inclusion (LFI) vulnerability within a Python API built on FastAPI. The current code permits users to submit an image file name via a request body, subsequently returning the requested image through the API response. However, the absence of input validation exposes the API to potential exploitation, enabling users to use special characters to access files from different directories or even files with extensions beyond typical image formats like PNG and JPG.
\n\n
Participants are required to identify the location of the vulnerability and fix the issue(s) to fortify the application's defenses against LFI attacks. Successful resolution of the vulnerability demands that the API maintains its functionality while effectively neutralizing the identified security risk. 
\n\n
Submissions for this challenge must comprise solely of the amended code, confined within the **main.py** file.

## Requirements

- Python 3
- Git
- Quanchecker package

## Setup

### 1. Clone the Repository
   - Clone this repository to your local machine using the following command:
     ```
     git clone https://github.com/xhfmvls/PathGuard.git
     ```

### 2. Install Dependencies
   - Navigate to the project directory.
   - (Optional) Set up a virtual environment for the project:
     ```
     python -m venv venv
     source venv/bin/activate  # On Unix/Linux
     .\venv\Scripts\activate    # On Windows
     ```
   - Install the required dependencies using the following command:
     ```
     pip install -r requirements.txt
     ```

### 3. Run the Application
   - Run the FastAPI application using the following command:
     ```
     uvicorn main:app --host 0.0.0.0 --port 8080
     ```
   - The application will start running locally on `http://localhost:8080`.

## Testing and Submission

### 1. Testing Procedure
  - To run the test, execute the following command in your terminal:
    ```
    python checker.py
    ```
  - Before running the tests, ensure that you have installed the Quanchecker package. You can do so by executing:

    ```
    pip install quanchecker
    ```
  - Additionally, you can use the provided Postman sample (`PathGuard_Sample.postman_collection.json`) located in the project directory for testing.
  - Please note that the test cases executed (both in the `checker.py` file and Postman sample) are only examples provided for your reference. There are additional test cases that are kept confidential and will only be run when you submit your code.


#### Input Format:
- **Description**: The input consists of a string representing a file name.
- **Format**: 
  - The string has a length between 10 and 50 characters, inclusive.

#### Output Format:
- **Description**: The expected output can be one of the following:
  1. **Image**: An image file with the same name as the input, if the input is valid and the corresponding image file exists.
  2. **Error Message**: If the input is invalid or the corresponding image file does not exist, an appropriate error message should be produced.
  - **Unsupported file type**: If the image file name extension is not `.png` or `.jpg`.
  - **Image not found**: If the image file corresponding to the input file name does not exist.
  - **Invalid image name**: If the image file name contains characters that could enable a hacker to access files from different directories.

\n
Note: For the case where the expected value is hash, you do not need to hash the image. As long as the image is shown correctly in your testing tool (e.g., Postman), it is almost guaranteed to be correct. The hash values are provided for validation purposes by the system only.

### 2. Submission Guidelines
   - Once you have fixed the vulnerability, upload your solution to the web application.
   - The web application will validate whether the code is secure against the complete prepared payload.

## Resources

- [OWASP Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [OWASP Web Security Testing Guide: Testing for Local File Inclusion](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion)
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [File Inclusion Payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion)

## Credits
- **[xhfmvls](https://github.com/xhfmvls)** - Quan C Lead Developer
