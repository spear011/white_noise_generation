# White Noise Generation

## Program Features

- A program that generates 5 different types of noise.
- Composed of 3 functions for noise sample generation, applying a bandpass filter, and saving the generated samples.
- The generated noise is saved in WAV file format.

## Key Features

- Configure the sampling rate and length of generated samples.
- Choose from 3 weighting filters.
- Specify the sound volume when saving samples (in dB).

## How to Use

Each function can be used step by step. You can test all the processes by running the `noise_generator.ipynb` file.

### 1) main.py

#### a) generate_sample

- Generate noise samples.
  - `sec`: Duration of the noise to be generated.
  - `sample_rate`: Sampling rate.
  - `color`: Type of noise.
  - `weight`: Type of weighting filter.

#### b) bandpass_filter

- Apply bandpass filtering on frequency domain.
  - `samples`: Generated samples.
  - `lowcut`: Lower frequency for filtering.
  - `highcut`: Upper frequency for filtering.

#### c) save_sample

- Save the samples as WAV files.
  - `samples`: Generated samples.
  - `db`: Sound volume level.
  - `file_name`: Name of the file to be saved.

