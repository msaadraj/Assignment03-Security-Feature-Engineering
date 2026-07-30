# Assignment 03 – Log Aggregation, Feature Engineering & Security Telemetry

## ARZENS Engineering Internship Program

**Track 09 – AI, Automation & Security Engineering Advanced**

---

## Student Information

- **Name:** Muhammad Saad
- **Intern ID:** ARZ-2026-J4V9
- **Program:** AI, Automation & Security Engineering Advanced Intern

---

## Project Overview

This project demonstrates a professional Security Feature Engineering pipeline for processing raw security telemetry into machine learning-ready features.

The implementation includes:

- Log aggregation
- Security feature engineering
- Privacy-aware data processing
- CSV & JSON feature generation
- Data quality validation
- Feature drift analysis
- Feature documentation
- Basic exploratory data analysis (EDA)

---

## Project Structure

```
Assignment03/
│
├── feature_extractor.py
├── quality_validator.py
├── sample_raw_events.jsonl
├── sample_features.csv
├── sample_features.json
├── sample_reference_features.csv
├── feature_dictionary.md
├── sample_quality_report.html
├── drift_analysis.md
├── Feature_Engineering_Report.pdf
├── EDA.ipynb
├── README.md
└── AI_Assistance_Note.md
```

---

## Requirements

- Python 3.10+
- pandas

Install dependencies:

```bash
pip install pandas
```

---

## Execution

Generate security features:

```bash
python feature_extractor.py
```

Validate generated features:

```bash
python quality_validator.py
```

---

## Generated Output

- `sample_features.csv`
- `sample_features.json`
- `sample_quality_report.html`

---

## Technologies Used

- Python
- Pandas
- JSON
- CSV
- HTML
- Markdown

---

## Privacy Features

- Pseudonymization using SHA-256 hashing
- Privacy-aware feature engineering
- Feature documentation
- Data quality validation

---

## Disclaimer

This project was developed as part of the **ARZENS Engineering Internship Program** for educational purposes. The provided datasets are sample data intended solely for demonstrating security engineering concepts.

---

## Author

**Muhammad Saad**  
**ARZ-2026-J4V9**  
AI, Automation & Security Engineering Advanced Intern
