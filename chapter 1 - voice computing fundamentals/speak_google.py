'''
speak_google.py

This is a short script that connects with
GCP to generate a text-to-speech sample using Google's
Wavenet model.

You customize the wavenet model 
'''
def speak_google(text, filename, model):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=model,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open(filename, 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file %s'%(filename))

# experiment with various voices
base='output'
models=['en-US-Wavenet-A','en-US-Wavenet-B','en-US-Wavenet-C','en-US-Wavenet-D',
        'en-US-Wavenet-E','en-US-Wavenet-F']
text='hey I am testing out google TTS'

# loop through various voices
# now all these files will be in the current directory 
for i in range(len(models)):
    speak_google(text, base+'_'+models[i]+'.mp3', models[i])


