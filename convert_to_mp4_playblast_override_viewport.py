import maya.cmds as cmds
import os
import subprocess
import datetime

def playblast_to_mp4():
    ffmpeg_path = "C:/ffmpeg.exe"
    if not os.path.isfile(ffmpeg_path):
        cmds.error(f"FFmpeg not found at: {ffmpeg_path}")
        return

    videos_folder = os.path.join(os.path.expanduser("~"), "Videos")
    if not os.path.exists(videos_folder):
        os.makedirs(videos_folder)

    scene_name = os.path.splitext(os.path.basename(cmds.file(q=True, sn=True)))[0] or "untitled"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    selection = cmds.ls(selection=True, long=True) or []
    selected_cameras = []
    for obj in selection:
        shapes = cmds.listRelatives(obj, shapes=True, type="camera", fullPath=True) or []
        selected_cameras.extend(shapes)

    # Use the current focused model panel
    active_panel = cmds.getPanel(withFocus=True)
    if not cmds.getPanel(typeOf=active_panel) == "modelPanel":
        cmds.warning("⚠️ No active model panel. Please click inside a viewport before running the script.")
        return

    fallback_camera = cmds.modelEditor(active_panel, q=True, camera=True)
    if not selected_cameras:
        if not fallback_camera:
            cmds.warning("⚠️ No fallback camera available.")
            return
        selected_cameras = [fallback_camera]

    for cam in selected_cameras:
        cam_transform = cmds.listRelatives(cam, parent=True, fullPath=True)
        cam_name = cam_transform[0] if cam_transform else cam
        cam_short = cam_name.split("|")[-1].replace(":", "_")

        filename_base = f"{scene_name}_{cam_short}_{timestamp}"
        avi_path = os.path.join(videos_folder, f"{filename_base}.avi")
        mp4_path = os.path.join(videos_folder, f"{filename_base}.mp4")

        print(f"🎥 Switching {active_panel} to camera: {cam_name}")
        cmds.setFocus(active_panel)
        cmds.modelEditor(active_panel, edit=True, camera=cam_name)
        cmds.refresh(force=True)

        print(f"🎬 Playblasting {avi_path} using override viewport...")
        cmds.playblast(format="avi", filename=avi_path, forceOverwrite=True, clearCache=True,
                       viewer=False, showOrnaments=False, percent=100, compression="none",
                       quality=100, widthHeight=[1920, 1080])

        print(f"🎞️ Converting to MP4: {mp4_path}")
        subprocess.run([ffmpeg_path, "-y", "-i", avi_path,
                        "-c:v", "libx264", "-crf", "23", "-preset", "slow", mp4_path])

        try:
            os.remove(avi_path)
        except Exception as e:
            print(f"⚠️ Could not delete temporary file: {avi_path} — {e}")

        print(f"📂 Opening {mp4_path}")
        subprocess.Popen(['start', '', mp4_path], shell=True)

    print("✅ All playblasts completed.")
