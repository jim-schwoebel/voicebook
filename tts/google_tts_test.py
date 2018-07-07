def synthesize_text(text, voicetype):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    print(client.list_voices())

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE,
        name=voicetype)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('sorry'+voicetype+'.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

synthesize_text("Sorry, I didn't get that. How can I help?", 'en-US-Wavenet-A')
synthesize_text("Sorry, I didn't get that. How can I help?", 'en-US-Wavenet-B')
synthesize_text("Sorry, I didn't get that. How can I help?", 'en-US-Wavenet-C')
synthesize_text("Sorry, I didn't get that. How can I help?", 'en-US-Wavenet-D')
synthesize_text("Sorry, I didn't get that. How can I help?", 'en-US-Wavenet-E')
synthesize_text("Sorry, I didn't get that. How can I help?", 'en-US-Wavenet-F')
