def predict_threat(score: float):
    if score > 0.7:
        return "Likely Attack"
    return "Normal"