# Installation
- Clone this Repository

  ```git clone https://github.com/darrenleeleelee1/Fastapi_Practice.git ```
- Requirment
  - Python=3.8
  - Anaconda=4.8.5
# Getting Started
**Create Virtual Environment**
  
  ```conda create --name fastapi_env python==3.8```

**Activate Virtual Enviroment**
  
  ```activate fastapi_env```

**Install Dependency**
  
  ```pip install -r requirement.txt ```

**Start App**
  
  ```uvicorn main:app --reload```
# HTTP Verbs
## HTTP.GET
* go to 127.0.0.1:8000 to get the image
## HTTP.POST
* Open cmd
  ```
  curl -X POST "http://127.0.0.1:8000/uploadfile/" -H  "Content-Type: multipart/form-data" -F "file=@your_file_name;type=image/jpeg"
  ```
