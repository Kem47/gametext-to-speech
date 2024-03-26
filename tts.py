import yaml
import azure.cognitiveservices.speech as speechsdk


class TTS:

    def __init__(self) -> None:
        with open('configs/secrets.yaml', 'r') as file:
            secrets = yaml.safe_load(file)
        speech_key = secrets['azure']['subscription_key']
        service_region = secrets['azure']['service_region']
        self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        self.speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
        self.audio_config = speechsdk.audio.AudioOutputConfig(filename="audio_output/temp.wav")

    def synthesize(self, text):
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)
        result = speech_synthesizer.speak_text_async(text).get()
        # Check result
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
