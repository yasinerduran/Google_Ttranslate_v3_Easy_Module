from google.cloud import translate_v3
from google.cloud.translate_v3 import types

"""
This module wrote for official Google Cloud API for Python. 
# Before using this module you must follow this three step;
# 1. You should be have a Google Cloud account and one project.
# 2. Your cloud project must be include Cloud Translation API!.
# 3. You must be did this arrangements for your pc https://cloud.google.com/docs/authentication/getting-started

An example using;

# We need firstly instance of Translater object with project name and location.
# You can find this parameters in the google cloud console
translate = TransLater('**project-name-id**', '**location**') 

# We must target and source language. This method checks languages for any exception.
translate.set_target_language("tr") #Turkish
translate.set_source_language("en") #English

# translate_text method takes a list and returns a list.
response = translate.translate_text(["Hello World!"])
print(response)

"""


class TransLater:
    client = translate_v3.TranslationServiceClient()
    parent = None
    __target_language = ""
    __source_language = ""
    __input_configs = []
    __output_configs = []

    def callback(operation_future):
        # Handle result.
        result = operation_future.result()

    def __init__(self, _project, _location):
        self.parent = self.client.location_path(_project, _location)

    def set_target_language(self, target_language):
        try:
            if target_language in self.get_supported_languages():
                self.__target_language = target_language
            else:
                raise Exception('spam', 'eggs')
        except Exception:
            print("This target language doesn't support!")
            sys.exit()

    def set_source_language(self, source_language):
        try:
            if source_language in self.get_supported_languages():
                self.__source_language = source_language
            else:
                raise Exception('spam', 'eggs')
        except Exception:
            print("This source language doesn't support!")
            sys.exit()

    def get_supported_languages(self):
        dump = str(self.client.get_supported_languages(self.parent))
        return re.findall('language_code: "(.+?)"', dump)

    def translate_text(self, text):
        response = self.client.translate_text(text, self.__target_language, self.parent, "text/html", self.__source_language)
        response_texts = []
        for translation in response.translations:
           response_texts.append("{}".format(translation.translated_text))

        return response_texts







