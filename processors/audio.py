import subprocess
import base64
import pydub #type:ignore
import io

def convert_encode_mp3(mp3audio):

    # Use ffmpeg to conver to wav, 44100Hz, mono, signed 16 bit PCM little endian
    process = subprocess.Popen(['ffmpeg', '-i', 'pipe:0', '-f', 'wav', '-ar', '44100', '-ac', '1', '-acodec', 'pcm_s16le', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdoutdata, stderrdata = process.communicate(input=mp3audio)
    if process.returncode != 0:
        print("Error converting audio:", stderrdata.decode())
        return None
    
    trimmed_audio = trim_audio(stdoutdata)
    
    return trimmed_audio


def trim_audio(mp3audio, duration=5000):
    audio_io = io.BytesIO(mp3audio)
    audio = pydub.AudioSegment.from_file(audio_io)
    
    trimmed_audio = audio[:duration] # Trim audio to 5 seconds (This should be enough for Shazam matching)

    buffer = io.BytesIO()
    trimmed_audio.export(buffer, format="wav") # Convert to ByteLike object

    buffer.seek(0) # Reset the buffer position to the beginning

    return buffer.read()