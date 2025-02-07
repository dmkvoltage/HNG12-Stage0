# Basic Information API

A simple API that returns basic information including my email, current datetime, and my GitHub URL in a JSON format.
I made use of FastAPI which is much easier, simple to use and too basic. Also, it is robust.
For testing, I made use of Postman as well as the browser, since it's a GET request

## Description

This API was developed on Render as part of the HNG12 internship program Stage0. It provides a single endpoint that returns some basic information in JSON format, including:
- My registered email address
- The current datetime (ISO 8601 format), and 
- My GitHub repository URL


### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Local Development

1. Clone the repository
```bash
git clone https://github.com/dmkvoltage/HNG12
cd HNG12
```

2. Create a virtual environment
```bash
python -m venv venv
source venv\Scripts\activate
```

3. Install dependencies
From the requirements.txt file, install the dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`



## API Documentation
### Endpoint

- URL: `GET /`
- Description: Returns basic information including email, current datetime, and GitHub URL

### Response Format
```json
{
    "email": "kingokingsleykaah@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
}
```

### Example Usage
On the command line, 
Using curl:
```bash
curl https://hng12-stage0-a4wh.onrender.com
```

Using JavaScript:
```javascript
fetch('https://hng12-stage0-a4wh.onrender.com')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Deployment
This API was hosted on:

1. Render
Which offers a free plan and relatively easy to use

## Performance
The API is designed to be lightweight and fast, with response times consistently under 500ms.
However, the speed also depends on your internet connection.