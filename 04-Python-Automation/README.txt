
PROJECT: Phishing Email Investigation and Incident Response
INCIDENT ID: GH-2026-001

PYTHON AUTOMATION MODULE
------------------------

Purpose:
Automates the initial analysis of a suspicious phishing email.

Script:
phishing_analyzer.py

Input:
01-Email-Samples/phishing-sample.eml

Output:
automated-analysis.json

FUNCTIONALITIES:
1. Parses email headers.
2. Extracts sender and recipient information.
3. Identifies Reply-To and Return-Path addresses.
4. Extracts the email subject and date.
5. Retrieves SPF, DKIM and DMARC authentication results.
6. Extracts URLs from the email body.
7. Identifies domains associated with extracted URLs.
8. Generates a structured JSON investigation report.

TECHNOLOGIES:
- Python 3.14.2
- email (standard library)
- re (regular expressions)
- json
- pathlib
- urllib.parse

EXECUTION:
python phishing_analyzer.py

RESULT:
Successfully parsed the synthetic phishing email and
generated an automated JSON analysis report.

LIMITATIONS:
- Does not determine whether a URL is malicious.
- Does not verify sender identity independently.
- Does not visit or interact with suspicious URLs.
- Findings are based on a synthetic training email.

All indicators used in this project are fictional.
