# SoftwareEngineering  
Django Application Tutorial  

---

### Build Status
[![Build Status](https://app.travis-ci.com/RajShivangi/SoftwareEngineering.svg?branch=main)](https://app.travis-ci.com/github/RajShivangi/SoftwareEngineering)

---

### Coverage
| Description | Badge |
|--------------|--------|
| With `&&service` | [![Coverage Status](https://coveralls.io/repos/github/RajShivangi/SoftwareEngineering/badge.svg?branch=main)](https://coveralls.io/github/RajShivangi/SoftwareEngineering?branch=main) |

| Without `&&service` | [![Coverage Status](https://coveralls.io/repos/github/RajShivangi/SoftwareEngineering/badge.svg?branch=main)](https://coveralls.io/github/RajShivangi/SoftwareEngineering?branch=main) |
| Without branch | [![Coverage Status](https://coveralls.io/repos/github/RajShivangi/SoftwareEngineering/badge.svg?branch=main)](https://coveralls.io/github/RajShivangi/SoftwareEngineering?branch=main) |

---

### Application URL  
[https://softwareengineering-env.eba-xxxxxxxx.us-east-1.elasticbeanstalk.com/polls/](http://softwareeng-env.eba-3nwuskmb.us-east-1.elasticbeanstalk.com/polls/)   

---

## About the Project
**SoftwareEngineering** is a Django-based web application built as part of the SWE1 course.  
It demonstrates automated testing, linting, and continuous deployment using **Travis CI**, **Coveralls**, and **AWS Elastic Beanstalk**.

---

## Technologies Used
- Python 3.10  
- Django 5.x  
- Travis CI  
- Coveralls  
- AWS Elastic Beanstalk  
- Black & Flake8  

---

## Running Tests Locally
```bash
source venv/bin/activate
pip install -r requirements.txt
coverage run manage.py test
coverage report -m
