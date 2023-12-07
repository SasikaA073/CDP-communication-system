# Communication System Design 

## 1. Requirements 
- Implement a point-to-point digital wireless communication system
using software defined radios
- Communications must be secure and reliable

- Transmitter Design 
    - [ ] Send key strokes
    - [ ] Read Numlock/Capslock/Scrolllock state
    - [ ] Encoding
    - [ ] Security Implementation
    - [ ] Reliability Enhancement 
    - [ ] Jamming Protection
    - [ ] Modulation 

- Receiver Design 
    - [ ] Reliability Enhancement
    - [ ] Demodulation
    - [ ] Decoding

- Communications to occur in the 2.4 GHz ISM band
    Adhere to maximum power limitations

- User interface 

- Performance evaluation 
    - [ ] with distance 
    - [ ] End-to-end delay

- Optional Features 
    - [ ] Channel estimation 
    - [ ] Adaptive transmission
    - [ ] Closed-loop system
    - [ ] Noise Cancellation

## 2. GNU Radio 

GNU Radio is a ...


## 3. Evaluation Criteria with evaluation metrics

- 1. Image Transmission 
    - [x] Simulation 
    - [ ] Physically
 - Mean Squared Error (_MSE_) between the transmitted Image(_T_) and Received Image(_R_) 
 - MSE for Monochrome image of size _MxN_ is defined as

_MSE_ $= \sum_{i=1}^{M}$ $ \sum_{j=1}^{N} [T(i,j) - R(i,j)]^{2} $

- 2. Binary Data Stream Transmission 
    - [x] Simulation 
    - [ ] Physically
 - Bit Error Rate (_BER_)

- 3. Voice Transmission (Real Time voice captured from MIC / Recorded voice clip)
    - [x] Simulation 
    - [ ] Physically
 - Based on the Quality of the Received Voice (Evaluated by Hearing it)

___

## Setup Instructions

### Python Virtual Environment

1. Clone the repository:

    ```bash
    git clone https://github.com/SasikaA073/CDP-communication-system
    cd CDP-communication-system
    cd ST_Webapp
    ```
2. Install venv 

    ```bash
    sudo apt-get update
    sudo apt-get install python3-venv
    ```
3. Create a Python virtual environment named "gnu":

    
    ```bash
    python3 -m venv gnu
    ```

4. Activate the virtual environment:

    ```bash
    source gnu/bin/activate
    ```

### Install Dependencies

5. Install the required Python packages from the `requirements.txt` file:

    ```bash
    pip3 install -r requirements.txt
    ```

### Run the Interface

6. Run the following.

    ```bash
    streamlit run Home.py
    ```
## Contributors of the Project (Team RadioHeads)

- [Thisara Gunawardana](https://lk.linkedin.com/in/thisara-gunawardana-3a1774264)
- [Sasika Amarasinghe](https://lk.linkedin.com/in/sasika-amarasinghe)
- [Nimshi Wanniarachchi](https://lk.linkedin.com/in/nimshi-wanniarachchi-9a4541241)
- [Jazoolee Ahamed](https://lk.linkedin.com/in/jazoolee-ahamed)
