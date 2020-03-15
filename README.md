# Google Ttranslate_v3 Easy Module
 A module of official google translate_v3 api for Python
This module wrote for official Google Cloud API for Python. 
## Before using this module you must follow this three step;
1. You should be have a Google Cloud account and one project.
2. Your cloud project must be include Cloud Translation API!.
3. You must be did this arrangements for your pc https://cloud.google.com/docs/authentication/getting-started

An example using;

- We need firstly instance of Translater object with project name and location.
- You can find this parameters in the google cloud console
translate = TransLater('**project-name-id**', '**location**') 

- We must target and source language. This method checks languages for any exception.
translate.set_target_language("tr") #Turkish
translate.set_source_language("en") #English

- translate_text method takes a list and returns a list.
response = translate.translate_text(["Hello World!"])
print(response)
