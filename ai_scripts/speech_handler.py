import base64

class SpeechToTextHandler:
    def encode_audio(self, audio_path):
        with open(audio_path, "rb") as audio_file:
            return base64.b64encode(audio_file.read()).decode("utf-8")

    def prepare_stt_payload(self, encoded_audio):
        return {"config": {"encoding": "LINEAR16", "sample_rate": 16000}, "audio": {"content": encoded_audio}}