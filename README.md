# Head-tracking-for-FlightSims
Overly simple face tracking using a script that controls the camera in the cockpit

video:
https://www.youtube.com/watch?v=bgiYi32nKEM


this very simple project allows camera control in cockpit view. so how does it do that? First of all, with the ready-made face recognition model in opencv, we detect the position of the face in the camera and take a reference point, then calculate how many pixels the face moves according to this reference point and create a mouse input accordingly, so we can control the camera.
