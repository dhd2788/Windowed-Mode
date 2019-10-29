# Windowed-Mode
We are looking to simulate the computer screen as if it were a “window” into a world containing 3D objects. The program will utilize head tracking via a webcam to allow the user to interact with the objects in the world. By changing the angle or distance from the computer screen, the angle or field of view which you see the world would change as well. We are also looking to have different potential ways of interacting with the objects, such as moving them, throwing them, or causing them to break/wiggle.

We are considering having a "flashlight system" where the user is looking around in the 3D world with a flashlight (so the corners of the screen would be dark). The flashlight has the ability to magically interact with the objects it's pointed at (through user input from pressing space bar) and objects may interact differently. As a potential feature depending on time constraints, we'd like to have objects that change what they do depending on what the user has in their flashlight, such as roaches running away or the Stanford bunny whose head will follow the location of the user's eye as though it was watching the user.

For now we are expecting the user to have their webcam at the top and center of their screen, but we may add a calibration option for those with webcams in different locations (or just to improve the accuracy in general).

## Weekly Plan
| Week Numbers | Objectives |
| --- | --- |
| 4 | Project planning |
| 5 - 7 | Find a library/online resource for implementation of head tracking and rasterization/ray tracing |
| 10 | Combine Dara's and Caleb's implementation into a single working project |
| 11 | Implement basic object interaction (press spacebar to pick up/drop) |
| 12 - 13 | Implement "cool stuff" (magic flashlight, animals following the user's head position as though the user is being watched, roaches) |
| 14 - 15 | Port project to website & any additional features we'd like to implement |
| 16 | Project presentation/wrap up |

## Splitting up duties
Caleb and Dara will be meeting every Tuesday and Thursday at 3:30pm throughout the semester to accomplish these goals. Research for resources will be done independently (both will be responsible for finding potential useable sources), and the first few weeks will be separate implementations (Dara will do the ray tracer and Caleb will do the head tracking) and at that point, we may opt to do paired programming for the more challenging aspects.

## References
* [Head Tracking for Desktop VR Displays using the Wii Remote](johnnylee.net/projects/wii/)
* Joe Geigel's notes from Global Illuminations (CSCI71101.2175)
* [Head tracking software for MS Windows, Linux, and Apple OSX](https://github.com/opentrack/opentrack)
* [Object Tracking using OpenCV (C++/Python)](https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/)
