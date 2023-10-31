""" top level run script """
from facemap import process
import glob
import os
import numpy as np

savepath="/results"

# set parameters for face & behavior video angles
face_params={
  'rois':[{
    'rind': 1,
    'rtype': 'motion SVD',
    'iROI': 0,
    'ivid': 0,
    'yrange':np.arange(138,272),
    'xrange':np.arange(236,372),
  }],
  'fullSVD':False,
  'save_mat':False,
  'sbin':1,
  'sy': np.array([0]),
  'sx': np.array([0]),
  'savepath':savepath,
}

behav_params={
  'rois':[{
    'rind': 1,
    'rtype': 'motion SVD',
    'iROI': 0,
    'ivid': 0,
    'yrange':np.arange(115,190),
    'xrange':np.arange(107,227),
  }],
  'fullSVD':False,
  'save_mat':False,
  'sbin':1,
  'sy': np.array([0]),
  'sx': np.array([0]),
  'savepath':savepath,
}

def run():
  # find all attached .mp4 videos in data folder 
  video_base_path="/data"
  video_file_paths=glob.glob(os.path.join(video_base_path,'**','*.mp4'),recursive=True)
    
  if len(video_file_paths)==0:
    raise FileNotFoundError('no .mp4 videos found in data folder')

  # loop over all video files and process with facemap
  for vid_path in video_file_paths:
        
    if 'Face' in vid_path:
      params=face_params
    elif 'Behavior' in vid_path:
      params=behav_params
    else:
      print(vid_path+' does not contain Face or Behavior in its name, skipping')
      continue
      
    process.run(
      [[vid_path]],
      sbin=1,
      motSVD=True,
      movSVD=True,
      GUIobject=None,
      parent=None,
      proc=params,
      savepath=savepath,
    )


if __name__ == "__main__": 
  run()
