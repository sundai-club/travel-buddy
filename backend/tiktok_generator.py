import json
import tiktokgen

def generate_tiktok(itinerary, save_path="data/sample_video.mp4"):
    model = tiktokgen.prompt_to_video.find_model("Internet Videos")
    
    script = []
    for day, data in itinerary.items():
        day_parsed = day.replace("_", " ").replace("day", "Day")
        for d in data:
            script.append({
                "text": f"{day_parsed}: {d['location']}",
                "foreground_img": None,
                "prompt": d["location"]
            })

    prompt = tiktokgen.prompt_to_stock_video.prompt_to_stock_video(parsed_script=script)
    
    output_video_paths = []
    for i, item in enumerate(prompt):
        # create audio from script
        audio_path, transcription_data = tiktokgen.script_snippet_to_audio.generate_speech_and_transcription(item['text'], filename="Generate_speech_"+str(i))
        print(f"Audio File Saved: {audio_path}")
        print(f"transcription_data: {transcription_data}")

        # combine video and audio
        output_video_path = "data/output_"+str(i)+".mp4"
        tiktokgen.audio_video.combine_video_audio(item['video_path'], audio_path, transcription_data.words, output_video_path, item['foreground_img'])
        output_video_paths.append(output_video_path)
        
    print(output_video_paths)
    combined_script = ' '.join([x['text'] for x in script])
    tiktokgen.audio_video.combine_videos(output_video_paths, save_path, combined_script, logo_path="data/sundai_logo.png")
    return output_video_paths

if __name__ == "__main__":
    with open("data/dymmy_itirenary_small.json", "r") as file:
        inp_script = json.loads(file.read())
    generate_tiktok(inp_script, save_path="data/sample_video.mp4")