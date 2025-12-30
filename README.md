# Bank Information API Service[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHZ7t7g5uCho3v4tDtcrHAYtU1XSJR9fviC5GVYqWbAfF1VR1xnQQU12CRI2wc2qk9kywstYKD_KB5fEDI-nVUrDn_MES4Y1RSKJXF3Bf2g9suFiaTjwiNiAnBGnww-b_9nnAfaBxBZZUhQ6WI1_g%3D%3D)]

A high-performance REST API built with FastAPI and SQLAlchemy to query bank and branch information from a relational database.

## Method & Tech Stack
- **Framework:** FastAPI (chosen for its speed, modern asynchronous support, and auto-generated Swagger documentation).
- **ORM:** SQLAlchemy (provides a clean abstraction for database queries and ensures the code is database-agnostic).[[2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGu1_rkHSAH6miGaZcQeen-M7fuVcm-8PEmOYDwVZoMz9Roh8jzbzXVGVdteTwgL-o84p-_oJ4c4MfYExNWdLgnOeAUXYVgtrYGr_5-LwDtpbqde9LI8xuNUeZfxozzdRD3X84Cm1SVd4PK2sNm-cWfow9hzEG-bY5vFpqWokksPJStGxGRYC5iv_Zotw6i1QbSyOYhJ8sUnVBGqwRHpDM0fWWBkta3YViHrPjMGp2SJAYW4lLP2r8%3D)]
- **Data Validation:** Pydantic (used for request validation and defining response schemas).
- **Database:** SQLite (lightweight and efficient for evaluation; the code is easily portable to PostgreSQL).
- **Testing:** Pytest & HTTPX (to ensure endpoint reliability and data integrity).

## Features
- **Get Bank List:** Retrieve all registered banks in the system.
- **Branch Details:** Fetch comprehensive branch information using a unique IFSC code, including nested bank details.
- **Data Integrity:** Automatic validation of IFSC codes and error handling for non-existent records.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd <repo-name>
