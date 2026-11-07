# Splunk Detection Queries – GH-2026-001

## Project Overview

This document contains the SPL (Splunk Processing Language) queries developed during the simulated phishing email investigation.

The queries were used to identify suspicious URL access, simulated credential submission, review incident activity and summarise phishing-related events.

Data source: `simulated-web-activity.csv`

Incident ID: `GH-2026-001`

Note: All events are synthetic and used for educational demonstration.

## 1. Detect Suspicious URL Access

Purpose: Identify simulated phishing URL access events.

```spl
index=* source="simulated-web-activity.csv" event_type="url_accessed"
```

## 2. Detect Simulated Credential Submission

Purpose: Identify events where test credentials were assumed to have been submitted during the simulation.

```spl
index=* source="simulated-web-activity.csv" event_type="credential_submission"
| table timestamp incident_id employee source_ip destination_domain event_type result notes
```

## 3. Review Incident Activity Timeline

Purpose: Retrieve and review the sequence of events associated with the simulated phishing incident.

```spl
index=* source="simulated-web-activity.csv" incident_id="GH-2026-001"
| sort 0 timestamp
| table timestamp employee event_type destination_domain result
```

## 4. Summarise Phishing Incident Events

Purpose: Count events by activity type and result to understand the distribution of simulated incident activity.

```spl
index=* source="simulated-web-activity.csv" incident_id="GH-2026-001"
| stats count by event_type result
| sort -count
```

## 5. Identify Suspicious Phishing Activity for Alerting

Purpose: Identify suspicious URL access and simulated credential submission events for alert evaluation.

```spl
index=* source="simulated-web-activity.csv"
incident_id="GH-2026-001"
(event_type="url_accessed" OR event_type="credential_submission")
| table timestamp incident_id employee source_ip destination_domain event_type result
```

## Detection Summary

The queries demonstrate how Splunk can be used to:

- Identify suspicious URL access.
- Detect simulated credential submission activity.
- Reconstruct an incident timeline.
- Summarise event distributions.
- Identify events that meet configured alert conditions.

## Important Limitations

- The dataset contains synthetic activity records.
- Detection was demonstrated using a static CSV file.
- These queries were not tested against live production telemetry.
- The configured alert demonstrated alert creation and trigger conditions; an actual alert notification was not demonstrated.

These queries form part of the GH-2026-001 phishing investigation portfolio simulation.