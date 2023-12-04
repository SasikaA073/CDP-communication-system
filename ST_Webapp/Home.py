# Libraries
import streamlit as st
from PIL import Image

# Config
st.set_page_config(page_title='Communication Design Project', page_icon=':bar_chart:', layout='wide')


# Title
st.title('Communication System Design Project')

# Content
# c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = st.columns(14)
# c1.image(Image.open('images/ethereum-logo.png'))
# c2.image(Image.open('images/bsc-logo.png'))
# c3.image(Image.open('images/polygon-logo.png'))
# c4.image(Image.open('images/solana-logo.png'))
# c5.image(Image.open('images/avalanche-logo.png'))
# c6.image(Image.open('images/cosmos-logo.png'))
# c7.image(Image.open('images/near-logo.png'))
# c8.image(Image.open('images/flow-logo.png'))
# c9.image(Image.open('images/thorchain-logo.png'))
# c10.image(Image.open('images/osmosis-logo.png'))
# c11.image(Image.open('images/gnosis-logo.png'))
# c12.image(Image.open('images/optimism-logo.png'))
# c13.image(Image.open('images/arbitrum-logo.png'))
# c14.image(Image.open('images/axelar-logo.png'))


st.subheader('GNU Radio')
st.write(
    """
    GNU Radio is an open-source software development toolkit that provides signal processing blocks to implement software-defined radios and signal processing systems. It allows users to design and build radio systems to process a wide range of signals - from audio to radio frequencies - using a graphical interface.

Developed in Python, GNU Radio offers a comprehensive environment where users can create complex signal processing flowgraphs. These flowgraphs consist of interconnected blocks representing various signal processing functionalities, such as filters, modulators, demodulators, sources, sinks, and more. Users can design custom signal processing chains by arranging these blocks to create tailored radio systems or signal processing applications.

Its versatility makes it widely used across various domains, including telecommunications, aerospace, defense, research, and hobbyist projects. The software's open-source nature fosters a collaborative environment where developers contribute to the library of available blocks and functionalities.

GNU Radio's flexibility, coupled with its extensive library of signal processing blocks, empowers users to experiment, innovate, and develop diverse applications in the realm of software-defined radio and signal processing.   """
)


st.write("Developed by: ")

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Sasika Amarasinghe: [@SasikaA073](https://twitter.com/SasikaA073)**', icon="💡")
with c2:
    st.info('**GitHub: [@sasikaa073](https://github.com/SasikaA073)**', icon="💻")
with c3:
    st.info('**SW: [GNU Radio](https://www.gnuradio.org/)**', icon="🛰️")