# AI Based Attendance Integrity System

Development repository for dataset handling, face model setup, and camera tests. The website remains in the original repository.

## Local dataset

Keep collected student records under `Dataset/<student-id>/` with an `images/` folder and optional `student_details.json`. This repository ignores `Dataset/`, `dataset/`, and `student_datasets/`; do not commit student photos or personal details. Add only synthetic or consent-cleared samples if a test fixture is needed.

## Scripts

- `dataset_test.py` lists the contents of the local `Dataset/` directory.
- `dataset_inspect.py` reports each local student's image count and JSON field names.
- `dataset_image_check.py` checks image readability and dimensions under `dataset/`.
- `face_model_test.py` initializes InsightFace on CPU.
- `camera_test/webcam_test.py` previews the default camera; press Q to close.

Install dependencies for the scripts you use, including OpenCV (`opencv-python`) and InsightFace. Camera access and InsightFace model downloads depend on the host device.
