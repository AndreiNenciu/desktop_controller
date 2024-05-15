import keyboard, math, subprocess, time, random, pyautogui, webbrowser, os, pygame, json, mouse, pyttsx3, mss, mss.tools
import pytesseract
from PIL import Image

current_dir = os.path.dirname(os.path.realpath(__file__))
exe_path = os.path.join(current_dir, "Tesseract\\tesseract.exe")
print(exe_path)


try:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    exe_path = os.path.join(current_dir, "Tesseract\\tesseract.exe")
    pytesseract.pytesseract.tesseract_cmd = exe_path
except:
    try:
        pytesseract.pytesseract.tesseract_cmd = 'W:\\python-GIGA-PROJECT\\Tesseract\\tesseract.exe'
    except:
        raise "Error. It's fucked"



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
listM = []
listME = []
listS = []
listQ = []

def CPU_check():
    i = 1
    engine.say("How good is your CPU?")
    engine.runAndWait()
    time.sleep(1)
    for i in range(5):
        webbrowser.open("https://youtu.be/7GMP6pPSjXM?si=eoWDHFSKK9LzBz5P")
        time.sleep(0.3)
        i += 1


def ad_viewer():
    engine.say("Running an ad. Please wait")
    engine.runAndWait()
    time.sleep(1)

    folder_name = 'ad'
    exe_name = 'ad.exe'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(current_dir, folder_name)
    exe_path = os.path.join(folder_path, exe_name)

    if os.path.exists(exe_path):
        if os.name == 'nt':
            subprocess.Popen(['start', '', exe_path], shell=True)
            subprocess.Popen(['start', '', exe_path], shell=True)
            subprocess.Popen(['start', '', exe_path], shell=True)
        else:
            print("Unsupported operating system. Please provide a specific method for your OS.")
    else:
        print(f"Executable '{exe_name}' not found in folder '{folder_name}'")
        print(exe_path)


def laios_test():
    folder_name = 'media'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(current_dir, folder_name)

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out non-video files (you may need to adjust the condition based on your file types)
    video_files = [file for file in files if file.endswith('.mp4')]

    if video_files:
        # Select a random video file from the list
        random_video = random.choice(video_files)
        video_path = os.path.join(folder_path, random_video)

        if os.name == 'nt':
            subprocess.Popen(['start', '', video_path], shell=True)
        else:
            print("Unsupported operating system. Please provide a specific method for your OS.")
    else:
        print(f"No video files found in folder '{folder_name}'")


def play_random_sound():
    folder_name = 'sounds'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(current_dir, folder_name)

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out non-sound files (you may need to adjust the condition based on your file types)
    sound_files = [file for file in files if file.endswith('.wav') or file.endswith('.mp3')]

    if sound_files:
        # Select a random sound file from the list
        random_sound = random.choice(sound_files)
        sound_path = os.path.join(folder_path, random_sound)

        pygame.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    else:
        print(f"No sound files found in folder '{folder_name}'")


def move_mouse():
    screenWidth, screenHeight = pyautogui.size()
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    pyautogui.mouseDown()
    pyautogui.moveTo(x, y, duration=3)
    pyautogui.mouseUp()


def test_process():
    app_path = 'mspaint.exe'
    subprocess.Popen(app_path)
    time.sleep(0.5)
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(100, 300, duration=0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(100, 500, duration=0.1)
    pyautogui.mouseUp()
    pyautogui.moveTo(300, 300, duration=0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(300, 500, duration=0.1)
    pyautogui.mouseUp()
    time.sleep(0.3)
    pyautogui.mouseUp()

    try:
        center_x = 200  # Adjusted initial x coordinate
        center_y = 600  # Adjusted initial y coordinate
        radius = 200  # Adjust as needed

        # Loop through x coordinates to draw the flipped semicircle
        x = 200  # Adjusted initial x coordinate
        while x < 400:  # Adjusted loop condition
            # Calculate the discriminant to check if the point is within the semicircle
            discriminant = radius ** 2 - (x - center_x) ** 2

            # Check if the point is within the semicircle
            if discriminant >= 0:
                # Calculate y coordinate for the current x coordinate and flip it vertically
                y = center_y + math.sqrt(discriminant)  # Negate the square root

                # Move the mouse cursor to the current point
                pyautogui.moveTo(400 - x, y)
                pyautogui.mouseDown()

            # Increment x coordinate
            x += 10  # Adjusted x increment
    finally:
        pyautogui.mouseUp()

    try:
        center_x = 200  # Adjusted initial x coordinate
        center_y = 600  # Adjusted initial y coordinate
        radius = 200  # Adjust as needed

        # Loop through x coordinates to draw the flipped semicircle
        x = 200  # Adjusted initial x coordinate
        while x < 400:  # Adjusted loop condition
            # Calculate the discriminant to check if the point is within the semicircle
            discriminant = radius ** 2 - (x - center_x) ** 2

            # Check if the point is within the semicircle
            if discriminant >= 0:
                # Calculate y coordinate for the current x coordinate and flip it vertically
                y = center_y + math.sqrt(discriminant)  # Negate the square root

                # Move the mouse cursor to the current point
                pyautogui.moveTo(x, y)
                pyautogui.mouseDown()

            # Increment x coordinate
            x += 10  # Adjusted x increment
    finally:
        pyautogui.mouseUp()


def joycon(bonus=1):
    t_bonus = float(bonus / 33)
    engine.say("Japanese accent: What drift? Joycons have no issues.")
    engine.runAndWait()
    time.sleep(2)
    for i in range(0, 500):
        KILL_SWITCH()
        print("Time left: ", 500 - i)
        x = random.randint(0,3) +t_bonus
        y = random.randint(0,3) +t_bonus
        pyautogui.move(x,y)


def lag(bonus=0):
    engine.say("Connecting to Turkish server. Please wait")
    engine.runAndWait()
    time.sleep(random.randint(0, 5))

    for i in range(0, 100 + bonus):
        KILL_SWITCH()
        print("Time left: ", 100 - i)
        if random.randint(0, 10) == 3:
            pyautogui.moveTo(None, None, 0.3)
        else:
            time.sleep(0.3)


def KILL_SWITCH():
    if keyboard.is_pressed('='):
        exit(-1)


# TODO: finish this
def punish_mode(bonus=0):
    score = random.randint(0, 10) + bonus
    if score <= 0:
        engine.say("You pass. This time.")
        engine.runAndWait()
    else:
        pass


def speech_test():
    rate = engine.getProperty('rate')

    engine.setProperty('rate', 100)
    engine.say("TIE")
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engine.runAndWait()


def rock_paper_scissors():
    list = ["rock", "paper", "scissors", "Rock", "Paper", "Scissors"]
    if not pyautogui.prompt(text="Rock, paper, scissors. Please choose:", title="Game :)", default="fill me.") in list:
        rate = engine.getProperty('rate')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 50)
        engine.say("cheater.")
        engine.runAndWait()
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 100)
        punish_mode(5)
    else:

        numer = random.randint(0, 2)
        if numer == 0:
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 50)
            engine.say("TIE.")
            engine.runAndWait()
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 100)
            punish_mode(-3)
        elif numer == 1:
            rate = engine.getProperty('rate')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 3)
            engine.say("lose.")
            engine.runAndWait()
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 100)
            punish_mode(3)
        else:
            engine.say("You win, I guess.")
            engine.runAndWait()


def recording_test():
    time.sleep(3)
    engine.say("start")
    engine.runAndWait()
    my_list = mouse.record(button='right')
    engine.say("done")
    engine.runAndWait()
    with open('new.json', 'w') as f:
        json.dump(my_list, f)


def deserialize_mouse_event(x, y, z):
    return mouse._mouse_event.MoveEvent(x, y, z)


def penis_drawer(f):
    time.sleep(3)
    test = json.load(f)
    new_list = []
    for i in test:
        if type(i[0]) == int:
            new_list.append(deserialize_mouse_event(i[0],i[1],i[2]))
    mouse.move((test[0])[0], (test[0])[1])
    pyautogui.mouseDown()
    mouse.play(new_list)
    time.sleep(0.3)
    pyautogui.mouseUp()

def let_him_cook():
    folder_name = 'scripts'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(current_dir, folder_name)

    files = os.listdir(folder_path)
    script_files = [file for file in files if file.endswith('.json')]

    if script_files:

        random_script = random.choice(script_files)
        script_path = os.path.join(folder_path, random_script)
        with open(script_path, 'r') as f:
            penis_drawer(f)

    else:
        print(f"No sound files found in folder '{folder_name}'")


def writing_hell_load():
    folder_name = 'scripts'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(current_dir, folder_name)

    files = os.listdir(folder_path)
    script_files = [file for file in files if file.endswith('.txt')]

    if script_files:
        random_script = random.choice(script_files)
        script_path = os.path.join(folder_path, random_script)
        with open(script_path, 'r') as f:
            test = f.read()
            writing_hell(test)
    else:
        print(f"No text files found in folder '{folder_name}'")

def writing_hell (f):
    x = random.randint(10, 50)
    engine.say("Hope you don't need to type")
    engine.runAndWait()
    time.sleep(3)
    while x > 0:
        x = x - 1
        time.sleep(random.randint(0,3))
        keyboard.write(f[x])


def screenshot_test():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)


def image_recognision():
    print(pytesseract.image_to_string('guess this.png'))


def mouse_pointer():
    while True:
        print(pyautogui.position())


def main():
    if pyautogui.confirm(text='What to start', title='Hi!', buttons=['Test', 'App']) == "Test":
        image_recognision()
        time.sleep(30)
    else:
        while True:
            list = [joycon, lag, CPU_check, laios_test, ad_viewer, play_random_sound, rock_paper_scissors]
            random_function = random.choice(list)
            random_function()
            print(time.sleep(random.randint(0, 20)))


if __name__ == '__main__':
    main()
