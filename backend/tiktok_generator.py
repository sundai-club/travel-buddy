import json
import tiktokgen

def generate_tiktok(itinerary, save_path="data/sample_video.mp4"):
    model = tiktokgen.prompt_to_video.find_model("Internet Videos")
    
    scripts = []
    for day, data in itinerary.items():
        day_parsed = day.replace("_", " ").replace("day", "Day")
        for d in data:
            scripts.append({
                "text": f"{day_parsed}: {d['location']}",
                "foreground_img": None,
                "prompt": d["location"]
            })
    
    print(json.dumps(scripts, indent=4))
    prompt = tiktokgen.prompt_to_stock_video.prompt_to_stock_video(parsed_script=script)
    
    


if __name__ == "__main__":
    with open("data/dymmy_itirenary.json", "r") as file:
        script = json.loads(file.read())
    generate_tiktok(script, save_path="data/sample_video.mp4")