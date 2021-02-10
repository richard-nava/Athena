# Athena
A personal assistant and drone


---

## Installation

Once cloned or downloaded, run the `virtual_assistant.py` file, then say "Hello, Athena" followed by your query. 


---

## Usage

You can ask things like "Whats the weather today?" or "Who is Bruce Lee?". 

### Drone Features

In order to use Athena's drone features, you must be using a **DJI Tello** drone. *Athena does not currently work with any other type of drone.* 

Turn on your DJI Tello drone and connect your computer to your drone using Wi-Fi, then run the `virtual_assistant.py` file. You can now say things like "Hey Athena, Fly" which will launch the drone and move forward, or "Hey Athena, follow me!" which will launch the drone then follow the first face that appears in front of it.

### Remote control over drone using Keyboard

To use your machine as a controller for your DJI Tello drone, run the `KeyboardControl.py` file. Controls are as follows: 

| Key press      | Drone Action  |
| -------------- | ------------- |
| "t"      | Takeoff      |
| "y"      | Land      |
| "q"      | Shut down (for emergencies)  |
| "v"      | Disconnect drone from computer      |
| UP or "w"      | Pitch forward        |
| DOWN or "s"      | Pitch backward      |
| LEFT or "a"         | Yaw left       |
| RIGHT or "d"      | Yaw right        |



---

## API 


### recordAudio

Takes in audio spoken into microphone and converts it into string. Returns a string. 

### athenaResp

Creates an mp3 file from converted text named `athena_response.mp3` and plays the mp3. 

### wakeWords

Defines the wake words for Athena and returns True if the wake words are found in recordAudio.

### getDate 

Returns a string that includes the weekday, month, and year.

### greeting

Returns a random response based on a greeting input.

### getToKnow

Returns an introductory response if the user asks Athena to introduce itself.

### getPerson

Returns a first and last name based on the Athena query "Who is ___ ". This is used in the while loop in the `virtual_assistant.py` file that handles all user queries.

### trackFace 

Draws a square around faces and a small circle in the square's center. This uses the front face haar cascade file. 

### findFace 

The size of the square is used to determine the distance between the drone and the face, and drone speed and yaw orientation are adjusted accordingly to make sure the square is in the center of camera and a safe distance away. 

### getKeyboardInput 

Returns updated drone speed based on keyboard input. 

### getKey 

Returns a boolean. Used in getKeyboardInput to read specific keybaord inputs.


---

## Contact

richard.ig.nava@gmail.com
