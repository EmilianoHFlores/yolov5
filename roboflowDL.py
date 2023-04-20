from roboflow import Roboflow

rf = Roboflow(api_key="HwAAWQCtj7ydsOAVDb9I")
project = rf.workspace("yolov5testhome2023").project("testsalt")
dataset = project.version(1).download("yolov5")