#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import audio
from gnuradio import blocks
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import vocoder
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import sip
import transmitter_epy_block_4 as epy_block_4  # embedded python block
import transmitter_epy_block_5 as epy_block_5  # embedded python block



class transmitter(gr.top_block, Qt.QWidget):

    def __init__(self, InFile='default'):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "transmitter")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Parameters
        ##################################################
        self.InFile = InFile

        ##################################################
        # Variables
        ##################################################
        self.access_key = access_key = '11100001010110101110100010010011'
        self.trans_freq = trans_freq = 2.46e9
        self.time_offset = time_offset = 1.000
        self.thresh = thresh = 1
        self.taps = taps = [1.0 + 0.0j, ]
        self.samp_rate = samp_rate = 520834
        self.noise_volt = noise_volt = 0.0
        self.hdr_format = hdr_format = digital.header_format_default(access_key, 0)
        self.freq_offset = freq_offset = 0
        self.access_key_0 = access_key_0 = '11100001010110101110100010010011'

        ##################################################
        # Blocks
        ##################################################

        self._time_offset_range = Range(0.999, 1.001, 0.0001, 1.000, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, "Timing Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._time_offset_win)
        self._noise_volt_range = Range(0, 1, 0.01, 0.0, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, "Noise Voltage", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_volt_win)
        self._freq_offset_range = Range(-0.1, 0.1, 0.001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, "Frequency Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_offset_win)
        self.vocoder_cvsd_encode_fb_0 = vocoder.cvsd_encode_fb(1,0.5)
        self.vocoder_cvsd_decode_bf_0 = vocoder.cvsd_decode_bf(1,0.5)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=2,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=2,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Receive", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_1.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Transmit", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                200e3,
                50e3,
                window.WIN_HAMMING,
                6.76))
        self.epy_block_5 = epy_block_5.dec_blk(key=1)
        self.epy_block_4 = epy_block_4.enc_blk(key=1)
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_gfsk_mod_0 = digital.gfsk_mod(
            samples_per_symbol=2,
            sensitivity=1.0,
            bt=0.35,
            verbose=False,
            log=False,
            do_unpack=True)
        self.digital_gfsk_demod_0 = digital.gfsk_demod(
            samples_per_symbol=2,
            sensitivity=1,
            gain_mu=0.175,
            mu=0.5,
            omega_relative_limit=0.005,
            freq_error=0.0,
            verbose=False,
            log=False)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts(access_key_0,
          thresh, 'packet_len')
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=noise_volt,
            frequency_offset=freq_offset,
            epsilon=time_offset,
            taps=taps,
            noise_seed=0,
            block_tags=True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/thisara/Documents/old-cdp-docs/Audio/audio.wav', True)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'packet_len', 0)
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 12, "packet_len")
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(1)
        self.audio_sink_0 = audio.sink(48000, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.epy_block_5, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_gfsk_mod_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.blocks_repack_bits_bb_1, 0))
        self.connect((self.digital_gfsk_demod_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_gfsk_mod_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.epy_block_4, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.epy_block_5, 0), (self.vocoder_cvsd_decode_bf_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_gfsk_demod_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.vocoder_cvsd_encode_fb_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.vocoder_cvsd_decode_bf_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.vocoder_cvsd_encode_fb_0, 0), (self.epy_block_4, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "transmitter")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_InFile(self):
        return self.InFile

    def set_InFile(self, InFile):
        self.InFile = InFile

    def get_access_key(self):
        return self.access_key

    def set_access_key(self, access_key):
        self.access_key = access_key
        self.set_hdr_format(digital.header_format_default(self.access_key, 0))

    def get_trans_freq(self):
        return self.trans_freq

    def set_trans_freq(self, trans_freq):
        self.trans_freq = trans_freq

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps(self.taps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 200e3, 50e3, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt
        self.channels_channel_model_0.set_noise_voltage(self.noise_volt)

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_access_key_0(self):
        return self.access_key_0

    def set_access_key_0(self, access_key_0):
        self.access_key_0 = access_key_0



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--InFile", dest="InFile", type=str, default='default',
        help="Set File Name [default=%(default)r]")
    return parser


def main(top_block_cls=transmitter, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(InFile=options.InFile)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
