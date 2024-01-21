import acoustics as ac
import numpy as np


def generate_sample(
        sec : int = 10, 
        sample_rate : int = 44100, 
        color: str = 'white', 
        weight: str = 'A',
    ) -> ac.Signal:
  
    samples = ac.generator.noise(sec * sample_rate, color = color)
    return ac.Signal(samples, sample_rate).weigh(weight)

def bandpass_filter(
        samples : ac.Signal, 
        lowcut : int = 20, 
        highcut : int = 20000,
    ) -> ac.Signal:
    return samples.bandpass(lowcut=lowcut, highcut=highcut)

def save_sample(
        samples: ac.Signal, 
        db : int = 60, 
        file_name: str = 'sample',
      ):
    current_db = samples.leq()
    gain_db = db - current_db
    samples = samples.gain(gain_db)
    samples.to_wav(file_name + '.wav')

def run():
    sample = generate_sample()
    sample = bandpass_filter(sample)
    save_sample(sample)

if __name__ == '__main__':
    run()