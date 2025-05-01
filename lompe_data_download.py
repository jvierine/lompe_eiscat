# # downlaod the data for the event (specifically iridium, supermag and superdarn data)

# need forked lompe version on https://github.com/FasilGibdaw/lompe/
from lompe.data_tools import dataloader, datadownloader
import pandas as pd
event = '2025-03-04'

# # reading files if they exist or downloading and preparing in lompe data formats

# sdarn_file = datadownloader.download_sdarn(event, tempfile_path='./') # no sdarn data
# smag_file = datadownloader.download_supermag(
#     event, tempfile_path='./')  # no supermag data
# iridium_file = datadownloader.download_iridium(
#     event, tempfile_path='./')  # no iridium data
# file_iridium = dataloader.read_iridium(
#     event, file_name=iridium_file, tempfile_path='./')  # no iridium data
# file_ssusi = datadownloader.download_ssusi_cdaweb(
#     event, hemi='north', basepath='./ssusi_tempfiles', tempfile_path='./', source='cdaweb')  # no ssusi data
file_swarm = datadownloader.download_swarm(event, tempfile_path='./')

# file names and location, reading the data
# supermag = pd.read_hdf(smag_file)
# superdarn = pd.read_hdf(sdarn_file)
# iridium = pd.read_hdf(file_iridium)
# this data is just used as if swarm is not detecting divergence free current
# swarm_data = pd.read_hdf(file_swarm)
