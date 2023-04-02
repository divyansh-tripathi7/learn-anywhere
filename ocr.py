import os
import cv2
import openai
import easyocr
import matplotlib.pyplot as plt
from torch.cuda import is_available
from dotenv import load_dotenv , find_dotenv
import time

class Reader:
    def __init__(self, is_cuda=False):
        self.reader = easyocr.Reader(['en'], gpu=is_cuda, model_storage_directory=os.path.join('models'), download_enabled=True)

    def __call__(self, img):
        return self.extract_text(img)

    def extract_text(self, img, show_text=False, show_confidence=False):
        result = self.reader.readtext(img)

        extracted_text = []

        for text in filter(lambda x: x[-1] > .15, result):
            box, acc_text, confidence = text

            # box[0] and box[2] - upper left and lower right corners of the box
            img = cv2.rectangle(img, [int(i) for i in box[0]], [int(i) for i in box[2]], (0, 255, 0), 2) # each coordinate is a list has to be int

            if show_text and show_confidence:
                img_text = f'{acc_text} - ({"{:.3f}".format(confidence)}%)'

            elif show_text:
                img_text = acc_text

            elif show_confidence:
                img_text = f'CONF: ({"{:.3f}".format(confidence)}%)'

            if show_text or show_confidence:
                img = cv2.putText(
                    img, 
                    img_text, 
                    (int(box[0][0]), int(box[0][1] - 3)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    fontScale=.5, 
                    color=(168, 90, 50),
                    thickness=2
                )

            extracted_text.append(acc_text)

        return extracted_text, img

class GPT_3:
    def __init__(self, api_key):
        openai.api_key = api_key

        self.completion = openai.Completion
        self.options = {
            'engine': 'text-davinci-002',
            'temperature': 0.25,
            'top_p': 1,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'max_tokens': 512
        }

    def __call__(self, prompt, options=None):
        return self.prediction(prompt, options)

    def prediction(self, prompt, options=None):
        if not options:
            options = self.options

        return self.completion.create(prompt=prompt, **options)['choices'][0]['text']
    
    def teach(self, text):
        prompt = f'Tell me what you all know about !\n\n{text}'

        return self.prediction(prompt=prompt)
    
    def resources(self, text):
        prompt = f'Tell me resources to learn about !\n\n{text} in the form of a list of one yt video , 1 book , 1 article , 1 podcast'

        return self.prediction(prompt=prompt)

    def summarize(self, text):
        prompt = f'Try to summarize the following text as best you can!\n\n{text}'

        return self.prediction(prompt=prompt)
    
    def topics(self, text):
        prompt = f'Tell me the topics which are related to the following text as best you can!\n\n{text}'
        # time.sleep(1)
        return self.prediction(prompt=prompt)
    # in the form of a dictionary like ["question": "Question 1","options": ["Option 1", "Option 2", "Option 3", "Option 4"], "correct_answer": "Option 1" ]" and return a dictionary not a string 
    def QuizMe(self, text):
        prompt = f'please make a MCQ quiz of 5 question related to the following text with correct options in the end !\n\n{text}'
        # time.sleep(1)
        return self.prediction(prompt=prompt)

def read_img(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img

if __name__ == '__main__':
    load_dotenv() # Load secrets

    print(os.getenv("OPENAI_API_KEY"))
    reader = Reader(is_cuda=is_available())
    gpt_3 = GPT_3(os.getenv('OPENAI_API_KEY'))
    
    img = read_img('Text-of-the-preamble.jpg')
    text, extracted_image = reader(img)
    
    text = ' '.join(text)

    text = text.lower()
    print('Extracted_text')
    print(text)

    # time.sleep(3)
    summarization_result = gpt_3.summarize(text)

    print('Summarized text:')
    print(summarization_result)

    
    print('Topics Covered:')
    topics_covered = gpt_3.topics(text)
    print(topics_covered )

    print('quesn from summary:')
    quizQs = gpt_3.QuizMe(summarization_result)
    print(quizQs )
    print('Quesns from topic :')
    quizQs2 = gpt_3.QuizMe(topics_covered)
    print(quizQs2)

    # plt.imshow(extracted_image)
    # plt.show()