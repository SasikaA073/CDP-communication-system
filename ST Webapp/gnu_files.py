audio_dir = "../Audio Transfer/"
image_dir = "../Image Transfer/"
bit_stream_dir = "../Bit Stream Transfer/"
file_dir = "../File Transfer/"

gnu_py_files = {
    "audio":{
        "simulation": audio_dir +  "virtual_audio_transmitter.py",
        "real": audio_dir + "transmitter.py",
        "realtime" : audio_dir + "transmitter_realtime.py"
        }    , 
    "image":{
        "simulation": image_dir + "pkt_fsk_xmt.py",
        "real": image_dir + "pkt_fsk_xmt.py",
        "realtime" : image_dir + "pkt_fsk_xmt.py",
        "calculate_loss": image_dir + "Image_loss/image_loss.py"
    }
    ,
    "bit_stream":{
        "simulation": bit_stream_dir + "",
        "real": bit_stream_dir + "",
        "realtime": bit_stream_dir + ""
    },
    "file":{
        "simulation": file_dir + "file_transmitter.py",
        "real": file_dir + "file_transmitter.py",
        "realtime": file_dir + "file_transmitter.py", 
        "calculate_loss": file_dir + "file_transmitter_loss.py"
    },
    "test":{
        "simulation":audio_dir + "drawing.py"
    }
}

gnu_grc_files = {
    "audio":{
        "simulation": audio_dir +  "realtime_transmitter.grc",
        "real": audio_dir + "realtime_transmitter.grc"
        }    , 
    "image":{
        "simulation":image_dir + "pkt_fsk_xmt.grc",
        "real": image_dir + "pkt_fsk_xmt.grc",
        }
    ,
    "bit_stream":{
        "simulation": bit_stream_dir + "",
        "real": bit_stream_dir + "",
        "realtime": bit_stream_dir + ""
    },
    "file":{
        "simulation": file_dir + "file_transmitter.grc",
        "real": file_dir + "file_transmitter.grc",
        "realtime": file_dir + "file_transmitter.grc", 
    }
    ,
    "test":{
        "simulation":audio_dir + "drawing.py"
    }

}

