
from email import policy
from email.parser import BytesParser
from pathlib import Path
from urllib.parse import urlparse
import re
import json

# Locate the project folders
project_dir = Path(__file__).resolve().parent.parent
email_file = project_dir / "01-Email-Samples" / "phishing-sample.eml"
output_file = Path(__file__).resolve().parent / "automated-analysis.json"

# Check that the email sample exists
if not email_file.exists():
    raise FileNotFoundError(f"Email sample not found: {email_file}")

raw_email = email_file.read_bytes()
clean_email = raw_email.decode("utf-8-sig")
message = BytesParser(policy=policy.default).parsebytes(
    clean_email.encode("utf-8")
)

# Extract email content
email_body = message.get_body(preferencelist=("html", "plain"))
body_content = email_body.get_content() if email_body else ""

# Extract URLs
urls = list(set(re.findall(r'https?://[^\s"<>]+', body_content)))

# Extract domains from URLs
url_domains = sorted({
    urlparse(url).hostname
    for url in urls
    if urlparse(url).hostname
})

# Build the analysis report
report = {
    "incident_id": "GH-2026-001",
    "analysis_type": "Automated phishing email analysis",
    "email_details": {
        "sender": str(message.get("From", "")),
        "recipient": str(message.get("To", "")),
        "reply_to": str(message.get("Reply-To", "")),
        "return_path": str(message.get("Return-Path", "")),
        "subject": str(message.get("Subject", "")),
        "date": str(message.get("Date", "")),
        "message_id": str(message.get("Message-ID", "")),
        "authentication_results": str(
            message.get("Authentication-Results", "")
        )
    },
    "extracted_urls": urls,
    "url_domains": url_domains,
    "analyst_note": (
        "Automated extraction only. Indicators belong to a "
        "synthetic training scenario and have not been independently "
        "verified as malicious."
    )
}

# Save the report
with output_file.open("w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("Phishing email analysis completed successfully.")
print(f"Subject: {message.get('Subject', '')}")
print(f"URLs extracted: {len(urls)}")
print(f"Report saved to: {output_file}")
