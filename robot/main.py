import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("csi://0")
display = jetson.utils.videoOutput("rtp://127.0.0.1:1234", argv=["--headless"])

while True:
    img = camera.Capture()
    detections = net.Detect(img)
    display.Render(img)
    display.SetStatus("Flat Fuck | Network {:.0f} FPS".format(net.GetNetworkFPS()))
    print("{:.0f} FPS".format(net.GetNetworkFPS()))
