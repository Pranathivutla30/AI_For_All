import os
import random
import shutil
from icrawler.builtin import BingImageCrawler
import requests
from PIL import Image
from io import BytesIO

# 10 classes with extended search terms
global_search_terms = {
    "frog": [
        "frog", "frog nature", "frog close-up", "frog in water", "frog on leaf",
        "frog sitting", "green frog", "frog in pond", "small frog", "tree frog",
        "frog macro", "poison dart frog", "rainforest frog", "frog on rock", "frog jumping",
        "frog red eyes", "amphibian frog", "tropical frog", "tiny frog", "frog resting",
        "frog camouflage", "frog night photo", "frog face", "frog under leaf", "frog legs",
        "blue poison frog", "yellow frog", "frog in jungle", "frog relaxing", "baby frog"
    ],
    "horse": [
        "horse", "wild horse", "horse galloping", "horse close-up", "horse running",
        "horse herd", "horse in field", "brown horse", "white horse", "race horse",
        "horse portrait", "mustang horse", "horse with rider", "horse rearing", "black horse",
        "farm horse", "horse in snow", "horse with foal", "horse in stable", "horse grazing",
        "horse on hill", "horse in fog", "horse on trail", "horse saddle", "horse looking back",
        "horse resting", "horse drinking water", "horse hair blowing", "painted horse", "horse training"
    ],
    "truck": [
        "truck", "off-road truck", "truck close-up", "red truck", "vintage truck",
        "big rig truck", "semi truck", "truck on road", "pickup truck", "monster truck",
        "diesel truck", "delivery truck", "truck side view", "cargo truck", "white truck",
        "military truck", "blue truck", "truck at construction site", "tow truck", "city truck",
        "fire truck", "truck in desert", "truck headlight", "truck crossing bridge", "snow plow truck",
        "truck hauling", "dump truck", "logging truck", "truck parked", "rusty truck"
    ],
    "cat": [
        "cat", "kitten", "cat close-up", "cat sleeping", "cat drinking water",
        "cat in garden", "cute cat", "cat playing", "cat on chair", "tabby cat",
        "cat licking", "cat stretching", "long-haired cat", "calico cat", "black cat",
        "cat near window", "cat with toy", "cat staring", "cat hiding", "fluffy cat",
        "cat on couch", "cat looking up", "cat walking", "cat in bed", "white cat",
        "cat with big eyes", "grumpy cat", "cat yawning", "siamese cat", "ginger cat"
    ],
    "bird": [
        "bird", "bird in tree", "bird close-up", "flying bird", "exotic bird",
        "colorful bird", "bird wings spread", "bird perched", "small bird", "bird eating",
        "hummingbird", "eagle flying", "parrot bird", "blue jay", "bird nest",
        "songbird", "owl", "flock of birds", "bird in sky", "water bird",
        "bird silhouette", "cardinal bird", "bird on fence", "bird with berries", "bird mid flight",
        "woodpecker", "falcon", "swallow bird", "bird in rain", "bird reflection"
    ],
    "dog": [
        "dog", "puppy", "dog close-up", "dog playing", "dog running",
        "cute dog", "dog in park", "brown dog", "small dog", "dog with ball",
        "labrador retriever", "golden retriever", "dog tongue out", "dog on grass", "white dog",
        "dog sitting", "dog jumping", "dog with owner", "poodle dog", "dog with collar",
        "dog barking", "fluffy dog", "dog sleeping", "beagle dog", "puppy eyes",
        "dog shaking water", "happy dog", "rescue dog", "dog on leash", "dog in car"
    ],
    "airplane": [
        "airplane", "airplane flying", "jet airplane", "commercial airplane",
        "airplane close-up", "airplane in sky", "airplane taking off", "airplane landing", "airplane wing", "airplane cockpit",
        "private jet", "airplane on runway", "airplane clouds", "airplane inside", "military jet",
        "airbus plane", "boeing airplane", "old airplane", "glider", "airplane above city",
        "airplane contrails", "night airplane", "airplane over ocean", "airport terminal airplane", "airplane parked",
        "plane taxiing", "airplane window view", "small airplane", "airplane night lights", "pilot in airplane"
    ],
    "deer": [
        "deer", "wild deer", "deer close-up", "baby deer", "deer in forest",
        "deer in grass", "deer family", "male deer", "female deer", "deer standing",
        "deer walking", "deer running", "deer in snow", "white-tailed deer", "spotted deer",
        "antlered deer", "deer drinking water", "deer trail camera", "young deer", "deer ears",
        "deer looking back", "deer on hill", "deer herd", "deer resting", "forest deer",
        "deer beside tree", "deer on path", "deer grazing", "deer under sunlight", "deer eyes"
    ],
    "ship": [
        "ship", "cargo ship", "cruise ship", "ship at sea", "old ship",
        "big ship", "sailing ship", "container ship", "warship", "boat ship",
        "ship deck", "ship on ocean", "luxury ship", "naval ship", "tanker ship",
        "ship sunset", "ship side view", "harbor ship", "ship loading", "fishing ship",
        "ship in storm", "ship silhouette", "ship bridge", "ship chimney", "ship docking",
        "ship with flags", "ship fog", "ship bow", "ship rope", "ship radar"
    ],
    "automobile": [
        "automobile", "classic car", "sports car", "luxury car", "vintage automobile",
        "red automobile", "blue car", "car front view", "car driving", "automobile racing",
        "convertible car", "electric car", "black car", "automobile showroom", "car engine view",
        "car headlights", "urban car", "car parked", "highway car", "car rear view",
        "shiny car", "rusty car", "car interior", "old convertible", "family car",
        "yellow car", "SUV automobile", "compact car", "offroad car", "white sports car"
    ]
}


MAX_NUMBER = 200                  # max images per search term
TARGET_IMAGES = 2000              # images per class
base_output_path = "./bing2000downloads"  # output folder for all images

# ------------------- DOWNLOAD FUNCTION -------------------
def download_images_bing(category, terms):
    save_path = os.path.join(base_output_path, category)
    os.makedirs(save_path, exist_ok=True)

    total_downloaded = len([
        f for f in os.listdir(save_path)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])

    for term in terms:
        if total_downloaded >= TARGET_IMAGES:
            break

        crawler = BingImageCrawler(storage={'root_dir': save_path})
        crawler.crawl(
            keyword=term,
            max_num=min(MAX_NUMBER, TARGET_IMAGES - total_downloaded),
            filters={
                'type': 'photo',
                'license': 'commercial'
            }
        )

        # Update count after each crawl
        total_downloaded = len([
            f for f in os.listdir(save_path)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ])

        print(f"🟢 {category}: {total_downloaded}/{TARGET_IMAGES} downloaded so far...")

    print(f"✅ Done downloading {category}: {total_downloaded} images.")

# ------------------- FULL PROCESS -------------------
for category, terms in global_search_terms.items():
    download_images_bing(category, terms)

print("🎯 All categories completed with approximately 200 images each.")
