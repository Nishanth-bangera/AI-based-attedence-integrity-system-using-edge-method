from insightface.app import FaceAnalysis

# Initialize the face recognition model
app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"]
)

# Prepare the model for CPU execution
app.prepare(ctx_id=-1, det_size=(640, 640))

print("InsightFace model initialized successfully!")