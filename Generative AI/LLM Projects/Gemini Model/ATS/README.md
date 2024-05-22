# Resume Boost : Simplified Job Hunt

## Overview

Resume Boost is an application that leverages the powerful Gemini model to analyze job descriptions and resumes. It provides valuable insights into the alignment between the given job description and your resume. The application not only identifies missing key words in the resume but also calculates a matching percentage to help candidates tailor their resumes for specific job opportunities.

## Features

- **Gemini Model Integration:** Utilizes the advanced Gemini model for accurate analysis and insights.
- **Resume Analysis:** Reads your resume.pdf and extracts relevant information.
- **Missing Keywords Identification:** Highlights the keywords missing in the resume compared to the job description.
- **Matching Percentage:** Calculates the percentage of match between the resume and the job description.
- **User-Friendly Interface**

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Make sure you have the necessary API keys and environment variables set up (refer to the documentation of the respective APIs).
4. Run the `app.py` file using `streamlit run app.py`.
5. Paste the relevant job description.
6. Upload your resume in pdf format.
7. Click on "Tell me about the resume" button and the insights about your resume.
8. Click "Match Percentage" button to see the percentage and the missing key words.

## Requirements
- `pdf2image`
- `streamlit`
- `google-generativeai`
- `python-dotenv`

You can install these requirements using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Contact Information

- **Name**: Mohanababu Ranganathan
- **Email**: mohanababuranganathan@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/mohanababuranganathan-27/
