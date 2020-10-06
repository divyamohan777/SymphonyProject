# SymphonyProject
## python requirements

pytest==6.1.0
pytest-html==2.1.1
pytest-json-report==1.2.1
pytz==2020.1
PyYAML==5.3.1
selenium==3.141.0
twilio==6.45.4

## Run pytest 

```bash
python -m pytest --html=SymphonyTest_report.html --json-report  SymphonyTest/Main.py
```

## IDE 
PyCharm

## Areas of Improvement

Convert all xpath elements to css elements

## Captcha Validation 

Google Captcha is preventing the validation since its detecting the automated browser session for both audio and image captcha.


