# 🌿 Plant Finder

An AI-powered web application that analyzes photos of flowers and plants using a pre-trained image classification model from Hugging Face.

## 🎯 About

Plant Finder is a simple, beginner-friendly web application designed to encourage people to explore nature and learn about plants around them.

Simply take a photo of a flower or plant, upload it to the app, and explore AI-generated image classification predictions along with interesting plant facts.

Built for the **Hacktoberfest 2026 "Touch Grass" Challenge** — promoting outdoor exploration through technology.

## ✨ Features

* 📸 **Image Upload** — Upload JPG, JPEG, or PNG images.
* 🤖 **AI-Powered Classification** — Uses the pre-trained ResNet-50 model through Hugging Face Transformers.
* 📊 **Top 3 Predictions** — Displays the three highest-scoring predicted ImageNet classes.
* 🌼 **Plant Facts** — Shows interesting facts when a prediction matches a supported plant keyword.
* ⚡ **Model Caching** — Caches the loaded model with Streamlit to reduce repeated loading.
* 🖼️ **Image Preview** — Displays the uploaded image alongside the results.
* 🛡️ **Error Handling** — Handles unreadable images and reports image-analysis failures.
* 🌍 **Open Source** — Built with Python and freely available open-source libraries.

## 🛠️ Tech Stack

* **Python** — Core programming language
* **Streamlit** — Web application framework
* **Hugging Face Transformers** — Image classification pipeline
* **PyTorch** — Deep learning framework used by the model
* **Pillow (PIL)** — Image loading, validation, and processing

## 📋 Requirements

* Python 3.8 or higher, subject to the Python versions supported by your installed dependencies
* Internet connection for the initial model download
* Sufficient disk space and memory for the model and its dependencies

Resource requirements depend on the selected package versions and execution environment.

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/plant-finder.git
cd plant-finder
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows — Command Prompt**

```bat
venv\Scripts\activate.bat
```

**Windows — PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

Make sure your `requirements.txt` contains the required libraries:

```text
streamlit
transformers
torch
Pillow
```

Install them using:

```bash
pip install -r requirements.txt
```

For reproducible installations, test and pin compatible dependency versions for your environment.

### 5. Run the Application

```bash
streamlit run app.py
```

The app will usually be available at:

`http://localhost:8501`

The first run may take longer because the pre-trained model needs to be downloaded.

## 💡 How to Use

1. Launch the application.
2. Take a clear photo of a flower or plant.
3. Click **Upload a flower or plant photo**.
4. Select a JPG, JPEG, or PNG image.
5. View the uploaded photo and the top three model predictions.
6. Read a quick fact if the highest-ranked prediction matches a supported plant keyword.
7. Use the predicted label as a starting point for further research.

## 📸 Example

Suppose you upload a photo of a red rose. The app might return results similar to these:

```text
Image classification results:

1. rose                 — example score
2. vase                 — example score
3. daisy                — example score

Quick fact:
Roses have been cultivated for thousands of years
and are among the world's most popular flowers.
```

**Note:** These labels are illustrative only, not measured output from the application. Actual predictions depend on the uploaded image.

## 🤖 How It Works

Plant Finder uses the `microsoft/resnet-50` image classification model through the Hugging Face Transformers pipeline.

The model is a pre-trained ResNet-50 classifier trained on the ImageNet dataset.

The application follows this process:

1. **Upload:** Streamlit receives the user's image.
2. **Validate:** Pillow checks whether the uploaded file can be read as an image.
3. **Preprocess:** The image is converted to RGB format.
4. **Load the model:** The classification pipeline is initialized and cached using `@st.cache_resource`.
5. **Predict:** The model returns the three highest-scoring ImageNet classes.
6. **Display results:** Streamlit displays the predicted labels and their scores.
7. **Show a fact:** The app searches its plant-fact dictionary for a keyword matching the top prediction.

## ⚠️ Model Limitations

Plant Finder is an educational image-classification demo, not a specialist botanical identification system.

* **General-purpose model:** ResNet-50 is trained on ImageNet classes rather than a dedicated plant-species dataset.
* **Identification may be inaccurate:** A plant image may receive an unrelated label or a label that is too general to identify the species.
* **Scores are not guarantees:** The displayed scores represent the model's scores for predicted classes, not verified probabilities that an identification is correct.
* **Limited facts:** Facts are available only for keywords included in the application's dictionary.
* **Image quality matters:** Lighting, focus, viewing angle, background clutter, and image resolution may affect predictions.
* **Internet requirement:** An internet connection is normally required to download the model on the first run. Subsequent use depends on whether the model remains cached locally and available to the application.

Always verify important plant identifications using a reliable botanical reference. Do not rely on this application to determine whether an unfamiliar plant is safe to eat or touch.

## 📁 Project Structure

```text
plant-finder/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
```

`LICENSE` and `assets/screenshot.png` are optional until you create them. Keep the project structure consistent with the files actually present in your repository.

## 🎓 Learning Outcomes

This project demonstrates:

* Building a web application with Streamlit
* Integrating a pre-trained model using Hugging Face Transformers
* Performing image classification with deep learning
* Validating and preprocessing images with Pillow
* Caching expensive resources for better performance
* Displaying predictions and confidence scores
* Handling common image-processing and inference errors
* Building an approachable open-source learning project

## 🌱 Future Improvements

* [ ] Integrate a plant-specific classification model for more relevant predictions
* [ ] Add plant care instructions and growing tips
* [ ] Expand the plant-fact database
* [ ] Display reference links for predicted plants
* [ ] Save previously identified plants
* [ ] Add multilingual support
* [ ] Improve automated tests and input validation
* [ ] Deploy the application using Streamlit Community Cloud or Hugging Face Spaces
* [ ] Add a screenshot and demonstration GIF

## 🐛 Troubleshooting

**The model fails to load**

* Check your internet connection.
* Verify that PyTorch and Transformers are installed correctly.
* Check that the selected model is available from Hugging Face.
* Review the terminal output for the underlying error.

**The uploaded image cannot be read**

* Try a valid JPG, JPEG, or PNG image.
* Make sure the file is not corrupted.
* Try saving the image again and uploading it.

**The prediction seems incorrect**

* Use a clear, well-lit photograph.
* Keep the plant as the main subject.
* Remember that this application uses a general-purpose ImageNet classifier.

## 🤝 Contributing

Contributions are welcome!

You can help by:

* Reporting bugs through GitHub Issues
* Suggesting new features
* Improving documentation
* Adding plant facts and tests
* Improving image classification
* Submitting pull requests

For contributions, fork the repository, create a feature branch, make your changes, and submit a pull request describing what you changed.


## ⭐ Support

If you find this project useful, consider giving the repository a star on GitHub!

---

**Made for the "Touch Grass" Challenge** 🌿

Get off your screen and explore the amazing plants around you!


---

## 👨‍💻 Author

**Reethu**  

GitHub: https://github.com/ReeShenoy

---

Built with ❤️ for the Hacktoberfest 2026 "Touch Grass" Challenge.
