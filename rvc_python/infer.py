from rvc_python.modules.vc.modules import VC
from rvc_python.configs.config import Config
from scipy.io import wavfile
import os

from glob import glob
import soundfile as sf

from rvc_python.modules.vc.modules import VC
from rvc_python.download_model import download_rvc_models


vc_global = None


def preloadModel(pthFile, device):
    global vc_global
    lib_dir = os.path.dirname(os.path.abspath(__file__))
    download_rvc_models(lib_dir)
    config = Config(lib_dir,device)
    vc_global = VC(lib_dir,config)
    vc_global.get_vc(pthFile,"v2")




def infer_file(
    input_path,
    index_path = "",
    f0method = "harvest",
    opt_path = "out.wav",
    index_rate = 0.5,
    filter_radius = 3,
    resample_sr = 0,
    rms_mix_rate = 1,
    protect = 0.33,
    f0up_key = 0,
):

    wav_opt = vc_global.vc_single(
        sid=1,
        input_audio_path=input_path,
        f0_up_key=f0up_key,
        f0_method=f0method,
        file_index=index_path,
        index_rate=index_rate,
        filter_radius=filter_radius,
        resample_sr=resample_sr,
        rms_mix_rate=rms_mix_rate,
        protect=protect,
        f0_file="",
        file_index2=""
    )
    wavfile.write(opt_path, vc_global.tgt_sr, wav_opt)
    return opt_path
