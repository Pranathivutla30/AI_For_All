
# <h1 align="center"> <span style="color:#005A8B"> Distilling Convolutional Neural Network Performance from Multiple Data Sources

If you're curious about how knowledge distillation can boost model performance using real and generated data, you're in the right place — this project is made for you.


We are a research team at UMass Boston from UMass Boston. We are Can Do Crew Team. We are exploring how **knowledge distillation** helps student models perform better when trained on a mix of real images and AI-generated images data. Our study focuses on 10 object classes and evaluates how training size, data sources, and augmentation impact model performance.


## <h2 align="center"><span style="color:#005A8B"> What’s This Project About?

Our goal is to investigate how *model distillation* can improve learning efficiency for image classification. In simple words, we train a **student model** to mimic the behavior of a powerful **teacher model**, hoping that the student can learn faster and perform better—even with less data.

This main idea is important when we want to:

* Reduce model size for deployment
* Train on limited or mixed-quality datasets
* Save computation but still keep high accuracy


## <h2 align="center"> <span style="color:#005A8B"> Before We Started

We built a **teacher model** trained to classify 10 visual classes using CIFAR datasets. Below are example images (1 per class), and this model serves as the ground truth for guiding all student models. _**Please note:** While we use the CIFAR dataset to train the teacher model, we intentionally avoid using CIFAR for the student models to prevent bias and ensure a more realistic evaluation._


We asked ourselves:

<blockquote style="background-color:#E6F4F9; padding: 15px; border-left: 5px solid #3498db; border-radius: 5px; font-style: italic;">

👉 <em>How well can student models learn from the teacher under different dataset conditions?</em>
</blockquote>

## <h2 align="center"> <span style="color:#005A8B"> Google + Bing Search Example Queries </span>

These are few examples of our search queries:

<p>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">frog nature</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">wild horse</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">off-road truck</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">cat close-up</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">bird in tree</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">dog close-up</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">airplane flying</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">wild deer</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">cargo ship</code>
  <code style="background-color:#C5E4F3; padding:4px 8px; border-radius:4px;">classic car</code>
  
</p>

## <h2 align="center"> <span style="color:#005A8B"> Trainning Examples </span>

### <h3 align="center"><span style="color:#F05A28">Google</span>

<p float="left">
  <img src="trainningimages/google_dataset_1000/frog_raw/frog_raw_0001.jpg" width="100" height="100"/>
  <img src="trainningimages/google_dataset_1000/bird_raw/bird_raw_0002.jpg" width="100" height="100"/>
  <img src="trainningimages/google_dataset_1000/cat_raw/cat_raw_0100.jpg" width="100" height="100"/>

  <img src="trainningimages/google_dataset_1000/dog_raw/dog_raw_0097.jpg" width="100" height="100"/>

  <img src="trainningimages/google_dataset_1000/deer_raw/deer_raw_0009.jpg" width="100" height="100"/>

  <img src="trainningimages/google_dataset_1000/horse_raw/horse_raw_0018.jpg" width="100" height="100"/>

  <img src="trainningimages/google_dataset_1000/truck_raw/truck_raw_0016.jpg" width="100" height="100"/>

  <img src="trainningimages/google_dataset_1000/ship_raw/ship_raw_0022.jpg" width="100" height="100"/>

  <img src="trainningimages/google_dataset_1000/automobile_raw/automobile_raw_0045.jpg" width="100" height="100"/>

  <img src="trainningimages/google_dataset_1000/airplane_raw/airplane_raw_0004.jpg" width="100" height="100"/>

</p>


### <h3 align="center"> <span style="color:#F05A28">Bing</span>

<p float="left">

  <img src="trainningimages/bing_dataset_1000/airplane/airplane_0093.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/automobile/automobile_0003.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/bird/bird_0060.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/cat/cat_0050.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/deer/deer_0003.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/dog/dog_0001.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/frog/frog_0002.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/horse/horse_0009.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/ship/ship_0007.jpg" width="100" height="100"/>

  <img src="trainningimages/bing_dataset_1000/truck/truck_0025.jpg" width="100" height="100"/>

</p>

<h2 align="center"><span style="color:#005A8B">Stable Diffusion Generate Example Queries</span></h2>


<div align="center">

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a passenger airplane flying above the clouds during sunset</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a sleek sports car speeding down a coastal highway</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a grand cruise ship sailing across the ocean at sunset</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a golden retriever playing fetch in a sunny park</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a majestic deer standing in a misty forest at dawn</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a colorful tree frog on a leaf</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a wild horse running across a desert</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a monster truck jumping over a ramp</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a fluffy kitten playing with a ball of yarn</code><br>

  <code style="background-color:#C5E4F3; padding:6px 12px; border-radius:6px;">a colorful parrot perched on a branch</code>

</div>


### <h3 align="center"> <span style="color:#F05A28">Stable Diffusion v2</span>

<p align="center">

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/airplane/airplane_00001.jpg" width="100" height="100"/><br>
    <span>airplane</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/automobile/automobile_00001.jpg" width="100" height="100"/><br>
    <span>automobile</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/bird/bird_00005.jpg" width="100" height="100"/><br>
    <span>bird</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/cat/cat_00001.jpg" width="100" height="100"/><br>
    <span>cat</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/deer/deer_00006.jpg" width="100" height="100"/><br>
    <span>deer</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/dog/dog_00095.jpg" width="100" height="100"/><br>
    <span>dog</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/frog/frog_00035.jpg" width="100" height="100"/><br>
    <span>frog</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/horse/horse_00080.jpg" width="100" height="100"/><br>
    <span>horse</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/ship/ship_00001.jpg" width="100" height="100"/><br>
    <span>ship</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_v2/truck/truck_00003.jpg" width="100" height="100"/><br>
    <span>truck</span>
  </div>

</p>


### <h3 align="center"> <span style="color:#F05A28">Stable Diffusion (Diffusers)</span>

<p align="center">

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/frog/frog_003.jpg" width="90"/><br>
    <span>frog</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/bird/bird_005.jpg" width="90"/><br>
    <span>bird</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/cat/cat_007.jpg" width="90"/><br>
    <span>cat</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/dog/dog_009.jpg" width="90"/><br>
    <span>dog</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/deer/deer_008.jpg" width="90"/><br>
    <span>deer</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/horse/horse_004.jpg" width="90"/><br>
    <span>horse</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/truck/truck_001.jpg" width="90"/><br>
    <span>truck</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/ship/ship_006.jpg" width="90"/><br>
    <span>ship</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/automobile/automobile_003.jpg" width="90"/><br>
    <span>automobile</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:8px;">
    <img src="trainningimages/gen_ai_1000_diffuser/airplane/airplane_007.jpg" width="90"/><br>
    <span>airplane</span>
  </div>

</p>


## <h2 align="center"> <span style="color:#005A8B"> Dataset Overview

We prepared three major sources of training data:

* **Google Images**

* **Bing Images**

* **Stable Diffusion** (using both SD v2 and Hugging Face Diffusers)

> ✅ You can explore our full training samples [here](#)

> ✅ We also show a few of our **text prompts and search queries** used to build the dataset.

Each data source brings its own quality, variation, and bias. We tested how they affect student model learning.


## <h2 align="center"> <span style="color:#005A8B"> Our Experiments

We ran **13 experiments** across 3 dataset sizes:

| Dataset Size | Training Samples | Test Samples | Notes                           |
| ------------ | ---------------- | ------------ | ------------------------------- |
| Small        | 800              | 200          | Augmented with color + rotation |
| 5x           | 4000             | 1000         | Combined real + synthetic       |
| 10x          | 8000             | 2000         | Large scale, diverse samples    |

All models was evaluated on **real test images** from Google and Bing only.


## <h2 align="center"> <span style="color:#005A8B"> Key Results (Summary)

Our most exciting insights:

* **Small dataset**: Models improved slightly with KD, but **color augmentation** made the biggest boost.
* **5x dataset**: Minimal difference between scratch and KD—distillation was less impactful here.
* **10x dataset**: Huge gain! Google 10x + KD reached the highest accuracy with \~30% gain over baseline.

> 🔁 *Knowledge distillation works best at scale, especially with consistent, high-quality data.*


## <h2 align="center"> <span style="color:#005A8B"> Limitations

* We only used 10 object classes; real-world applications like cybersecurity involve far more complexity.
* Most test data was collected from Google/Bing; synthetic images varied in realism.
* Stable Diffusion v2 images and Bing's images sometimes lacked of generating right images based on queries.


### <h3 align="center"> <span style="color:#F05A28"> Failure Examples - Stable Fushion V2

<p float="left" align="middle">
  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/airplane/airplane_00002.jpg" width="100" height="100"/><br>
    <span>airplane</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/automobile/automobile_00013.jpg" width="100" height="100"/><br>
    <span>automobile</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/bird/bird_00040.jpg" width="100" height="100"/><br>
    <span>bird</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/cat/cat_00062.jpg" width="100" height="100"/><br>
    <span>cat</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/deer/deer_00010.jpg" width="100" height="100"/><br>
    <span>deer</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/dog/dog_00068.jpg" width="100" height="100"/><br>
    <span>dog</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/frog/frog_00050.jpg" width="100" height="100"/><br>
    <span>frog</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/horse/horse_00006.jpg" width="100" height="100"/><br>
    <span>horse</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/ship/ship_00006.jpg" width="100" height="100"/><br>
    <span>ship</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/gen_ai_1000_v2/truck/truck_00007.jpg" width="100" height="100"/><br>
    <span>truck</span>
  </div>
</p>

### <h3 align="center"> <span style="color:#F05A28"> Failure Examples - Bing

<p float="left" align="middle">
  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/airplane/airplane_0005.jpg" width="100" height="100"/><br>
    <span>airplane</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/automobile/automobile_0002.jpg" width="100" height="100"/><br>
    <span>automobile</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/bird/bird_0004.jpg" width="100" height="100"/><br>
    <span>bird</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/cat/cat_0007.jpg" width="100" height="100"/><br>
    <span>cat</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/deer/deer_0007.jpg" width="100" height="100"/><br>
    <span>deer</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/dog/dog_0049.jpg" width="100" height="100"/><br>
    <span>dog</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/frog/frog_0061.jpg" width="100" height="100"/><br>
    <span>frog</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/horse/horse_0009.jpg" width="100" height="100"/><br>
    <span>horse</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/ship/ship_0005.jpg" width="100" height="100"/><br>
    <span>ship</span>
  </div>

  <div style="display:inline-block; text-align:center; margin:5px;">
    <img src="trainningimages/bing_dataset_1000/truck/truck_0005.jpg" width="100" height="100"/><br>
    <span>truck</span>
  </div>
</p>


## <h2 align="center"> <span style="color:#005A8B"> Future Work

* Expand to **more challenging categories** and **larger label sets**

* Add dataset sources like **Firefox telemetry** and **Kaggle open image sets**

* Experiment with **fine-tuned diffusion models** for higher-quality synthetic generation.


## <h2 align="center"> <span style="color:#005A8B"> How We Used AI in This Project

Everyone in the team used AI tools to support different parts:

* **Rami** – Asked ChatGPT to explain results and improve insight clarity
* **Pranathi** – Generated UI mockups and experiment instructions
* **Avanith** – Used ChatGPT to generate base training scripts
* **Shauna** – Prompted ChatGPT to help plan poster layout and chart styling


## <h2 align="center"> <span style="color:#005A8B">Team & Acknowledgements</span>

We’d like to thank **Professor Yinxin Wan** and **Professor Wei Ding** at UMass Boston for their continuous support, guidance, and encouragement throughout this project. Your mentorship helped shape our journey in the #**AIforAll** class at UMass Boston. All of our contributions were made in support of this class.

## <h2 align="center"> <span style="color:#005A8B"> Follow Us </span>


<div align="center">

  <div style="display: inline-block; margin: 15px; text-align: center;">
    <a href="https://www.linkedin.com/in/raminguyen/">
      <img src="teamimages/ramihuunguyen.png" width="100" height="100" style="border-radius: 50%;"/><br>
      <span>Rami Huu Nguyen</span>
    </a>
  </div>

  <div style="display: inline-block; margin: 15px; text-align: center;">
    <a href="https://www.linkedin.com/in/lakshmi-pranathi-vutla30/">
      <img src="teamimages/LakshmiPranathiVutla.png" width="100" height="100" style="border-radius: 50%;"/><br>
      <span>Lakshmi Pranathi Vutla</span>
    </a>
  </div>

  <div style="display: inline-block; margin: 15px; text-align: center;">
    <a href="https://www.linkedin.com/in/avanith-kanamarlapudi-8aa081204/">
      <img src="teamimages/Avanith_Kanamarlapudi.png" width="100" height="100" style="border-radius: 50%;"/><br>
      <span>Avanith Kanamarlapudi</span>
    </a>
  </div>

  <div style="display: inline-block; margin: 15px; text-align: center;">
    <a href="https://www.linkedin.com/in/shauna-murray-6b3096201/">
      <img src="teamimages/Shauna_Murray.png" width="100" height="100" style="border-radius: 50%;"/><br>
      <span>Shauna Murray</span>
    </a>
  </div>

</div>


<p align="center">
  #AIforAll #UMassBoston #Innovation #2025 #Rami #Avanith #Pranathi #Shauna
</p>
