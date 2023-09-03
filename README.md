# music-genre-gtzan-classification
An transformer based audio classification system fine-tuned on distilBERT with Tesla T4 GPU


<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][Twitter-shield]][Twitter-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mahimairaja/music-genre-gtzan-classification">
    <img src="assets/logo.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Music Genre Classifier</h3>

  <p align="center">
    An Transformer based audio classification system fine-tuned on distilBERT with Tesla T4 GPU
    <br />
    <a href="https://github.com/mahimairaja/music-genre-gtzan-classification"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://huggingface.co/spaces/mahimairaja/music-genre-classifier">View Demo</a>
    ·
    <a href="https://github.com/mahimairaja/music-genre-gtzan-classification/issues">Report Bug</a>
    ·
    <a href="https://github.com/mahimairaja/music-genre-gtzan-classification/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


The Music Genre Classifier is an advanced audio classification system, utilizing a Transformer-based model fine-tuned with distilBERT, powered by a Tesla T4 GPU. This cutting-edge technology automatically assigns music tracks to specific genres, making it invaluable for music streaming platforms, recommendation systems, and music enthusiasts.

Key Features:

**Transformer-Based Model:** Leveraging the Transformer architecture, renowned for its success in natural language processing, this system adapts it to audio data, effectively capturing music characteristics.
<br>
**Fine-Tuned distilBERT:** The distilBERT model's efficiency and performance are harnessed to understand the intricate features unique to different music genres, enhancing genre prediction accuracy.
<br>
**Tesla T4 GPU:** The Tesla T4 GPU accelerates both training and inference, ensuring rapid processing even with extensive audio datasets.
<br><br>
With seamless data preprocessing, model training, and efficient inference, the system predicts music genres, enhancing music recommendations, playlist creation, and genre-based searches. Enjoy more personalized music experiences with this Music Genre Classifier, offering precision and speed in audio genre classification.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Transformers
* DistilBERT
* Numpy
* gradio
* librosa
* HuggingFace


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

To run this project, you need to have python installed on your system. If you don't have python installed, you can install it from [here](https://www.python.org/downloads/)

### Installation

1. Clone the repo and cd into the directory
   ```sh
   git clone https://github.com/mahimairaja/music-genre-gtzan-classification.git
   ```
   ```sh
   cd music-genre-gtzan-classification
   ```
2.  Create a virtual environment
    ```sh
    python -m venv venv
    ```
3. Activate the virtual environment
    ```sh
    source venv/bin/activate
    ```
4. Install the required packages
    ```sh
    pip install -r requirements.txt
    ```
5. Run the app
    ```sh
    python app.py
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Mahimai Raja J - [@mahimairaja3](https://twitter.com/your_username) - info@mahimairaja.in

Project Link: [mahimairaja/music-genre-gtzan-classification](https://github.com/mahimairaja/music-genre-gtzan-classification)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/mahimairaja/music-genre-gtzan-classification.svg?style=for-the-badge
[contributors-url]: https://github.com/mahimairaja/music-genre-gtzan-classification/graphs/contributors


[stars-shield]: https://img.shields.io/github/stars/mahimairaja/music-genre-gtzan-classification.svg?style=for-the-badge
[stars-url]: https://github.com/mahimairaja/music-genre-gtzan-classification/stargazers

[forks-shield]: https://img.shields.io/github/forks/mahimairaja/music-genre-gtzan-classification.svg?style=for-the-badge
[forks-url]: https://github.com/mahimairaja/music-genre-gtzan-classification/network/members

[issues-shield]: https://img.shields.io/github/issues/mahimairaja/music-genre-gtzan-classification.svg?style=for-the-badge
[issues-url]: https://github.com/mahimairaja/music-genre-gtzan-classification/issues

[license-shield]: https://img.shields.io/github/license/mahimairaja/music-genre-gtzan-classification.svg?style=for-the-badge
[license-url]: https://github.com/mahimairaja/music-genre-gtzan-classification/blob/main/LICENSE


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mahimairaja

[twitter-shield]: https://img.shields.io/badge/Twitter-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[Twitter-url]: https://twitter.com/mahimairaja3

[product-screenshot]: assets/demo.png

