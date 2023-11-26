# Communication System Design 

## 1. Requirements 
- Implement a point-to-point digital wireless communication system
using software defined radios
- Communications must be secure and reliable

- Transmitter Design 
 - [x] Send key strokes
 - [ ] Read Numlock/Capslock/Scrolllock state
 - [ ] Encoding
 - [ ] Security Implementation
 - [ ] Reliability Enhancement 
 - [ ] Jamming Protection
 - [ ] Modulation 

- Receiver Design 
 - [x] Reliability Enhancement
 - [x] Demodulation
 - [x] Decoding

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

### - [x] 1. Image Transmission 
 - Mean Squared Error (_MSE_) between the transmitted Image(_T_) and Received Image(_R_) 
 - MSE for Monochrome image of size _MxN_ is defined as

_MSE_ $= \sum_{i=1}^{M}$ $ \sum_{j=1}^{N} [T(i,j) - R(i,j)]^{2} $

### - [x] 2. Binary Data Stream Transmission 
 - Bit Error Rate (_BER_)

### - [x] 3. Voice Transmission (Real Time voice captured from MIC / Recorded voice clip)
 - Based on the Quality of the Received Voice (Evaluated by Hearing it)

