# IAM and Security Group Analyzer

## Overview
This project provides a tool to analyze AWS IAM users and security group rules. The purpose is to identify security group ingress rules that do not match any IAM user's name, helping to ensure that all security group descriptions are relevant and properly associated with actual IAM users.

## Features
- Fetches all IAM users from AWS.
- Fetches all security groups and their rules from AWS.
- Analyzes security group rule descriptions to find entries that do not match any IAM user's name.
- Utilizes fuzzy matching to determine similarities between security group rule descriptions and IAM usernames.

## Project Structure
- `iam_user_fetcher.py`: Contains the `IAMUserFetcher` class, which fetches all IAM users.
- `security_group_analyzer.py`: Contains the `SecurityGroupAnalyzer` class, which analyzes security group rules and filters out unmatched descriptions.
- `utils.py`: Contains utility functions for fuzzy matching.
- `main.py`: Main script to run the analysis.
- `requirements.txt`: Lists the required Python packages for the project.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/iam-sg-analyzer.git
    cd iam-sg-analyzer
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the necessary AWS credentials set up in your environment.

2. Run the main script:
    ```sh
    python main.py
    ```

3. The script will output security groups with IAM user unmatched ingress rules, indicating potential issues with your security group descriptions.

## Dependencies

- `boto3==1.34.117`
- `botocore==1.34.117`
- `fuzzywuzzy==0.18.0`
- `jmespath==1.0.1`
- `Levenshtein==0.25.1`
- `python-dateutil==2.9.0.post0`
- `python-Levenshtein==0.25.1`
- `rapidfuzz==3.9.3`
- `s3transfer==0.10.1`
- `six==1.16.0`
- `urllib3==2.2.1`

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any questions or issues, please contact [ruizsanchezroberto21@gmail.com].

---

Feel free to customize this `README.md` as per your project's specific details and needs.
