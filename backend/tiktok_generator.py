import json
import os
import tiktokgen


def generate_tiktok(itinerary, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    script = []
    for day, data in itinerary.items():
        day_parsed = day.replace("_", " ").replace("day", "Day")
        for d in data:
            script.append(
                {
                    "text": f"{day_parsed}: {d['location']}",
                    "foreground_img": None,
                    "prompt": d["location"],
                }
            )

    prompt = tiktokgen.prompt_to_stock_video.prompt_to_stock_video(
        parsed_script=script, filedir=save_dir, augment_prompt=False
    )

    output_video_paths = []
    for i, item in enumerate(prompt):
        # create audio from script
        audio_filename = f"{os.path.basename(save_dir)}_speech_{i}"
        audio_path, transcription_data = (
            tiktokgen.script_snippet_to_audio.generate_speech_and_transcription(
                item["text"], filename=audio_filename
            )
        )
        print(f"Audio File Saved: {audio_path}")
        print(f"transcription_data: {transcription_data}")

        # combine video and audio
        output_video_path = f"{save_dir}/output_" + str(i) + ".mp4"
        tiktokgen.audio_video.combine_video_audio(
            item["video_path"],
            audio_path,
            transcription_data.words,
            output_video_path,
            item["foreground_img"],
        )
        output_video_paths.append(output_video_path)

    print(output_video_paths)
    combined_script = " ".join([x["text"] for x in script])
    tiktokgen.audio_video.combine_videos(
        output_video_paths,
        f"{save_dir}/final_video.mp4",
        combined_script,
        logo_path="data/sundai_logo.png",
    )
    return output_video_paths


if __name__ == "__main__":
    with open("data/dymmy_itirenary_small.json", "r") as file:
        inp_script = json.loads(file.read())
    generate_tiktok(inp_script, save_dir=f"data/test_dir")
