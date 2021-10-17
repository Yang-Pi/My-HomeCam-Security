# My-HomeCam-Security
My-HomeCam-Security - entrance control system for smart home with Raspberry Pi.

### General work schema
<img src = "https://user-images.githubusercontent.com/55200686/99937212-2b40f400-2d76-11eb-84b2-21b46d074307.png" width = "700">
When a guest comes to the entrance door and push the call button (1), face recognition is activated (2) and guest photo with information about him is sent to the apartment owner phone (3). Next, the owner decides whether invited or extraneous guest stands at his door by pressing the corresponding button in the application (4), and the door, depending on this decision, opens or remains closed (5). The owner also can turn on a live broadcast from system camera and observes the entrance in real time.

### Демонстрация (видео)

| New guest registration | Opening the door |
| ------------- | ------------- |
| [<img src="https://user-images.githubusercontent.com/55200686/99917137-72e86100-2d1f-11eb-9bf9-a548b8d7a699.jpg" width="550">](https://drive.google.com/file/d/1A2cUUTbxGFeNGI3LN1ukyz4THrzo9D6J/view?usp=sharing) | [<img src="https://user-images.githubusercontent.com/55200686/99936928-668ef300-2d75-11eb-89c7-18b69ef0015f.jpg" width="550">](https://drive.google.com/file/d/1H5ayyIAoAmhwgudwDymaXe8MtvTAsokQ/view?usp=sharing)  |

### Cloning the repository
In *parts-for-training\\* catalog there are separate program modules which can be researched and tested: 
  - `01_face_dataset.py` - data capture (adding new object in database),
  - `02_face_training.py` - training a neural network based on updated data,
  - `03_face_recognition.py` - recognition (percentage prediction),
  - `rpi_camera_surveillance_system.py` - enable live broadcast,
    - before starting tunnel should be forwarded e.g. through ngrok; if localhost is used, broadcasting will be enable only for devices are in the same network as Raspberry Pi.
  - `buttonAndLED.py` - button pushing handler and Light-emitting diode work.
    
Create *dataset\\* catalog in the main program catalog before starting, images to neural network trainig with `haarcascade_frontalface_default.xml` are collected here, result file is named `trainer.yml`. Training can take some time.

### Don't forget build a hardware!

**Read more about the system in [Report.pdf](https://github.com/Yang-Pi/My-HomeCam-Security/blob/main/report/report.pdf)**
