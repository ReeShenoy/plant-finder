import streamlit as st
from transformers import pipeline
from PIL import Image, UnidentifiedImageError

st.set_page_config(page_title="Plant Finder", page_icon="🌿", layout="wide")


@st.cache_resource
def load_classifier():
    return pipeline(
        "image-classification",
        model="microsoft/resnet-50",
    )


PLANT_FACTS = {
    "rose": "Roses have been cultivated for thousands of years and are among the world's most popular flowers.",
    "tulip": "Tulips became so valuable in 17th-century Netherlands that they were involved in a famous market bubble.",
    "daisy": "Many daisies close their petals at night and reopen them in daylight.",
    "sunflower": "Young sunflowers can track the sun across the sky, a behavior called heliotropism.",
    "orchid": "The orchid family contains tens of thousands of accepted species.",
    "lavender": "Lavender is an aromatic plant widely used in fragrances and essential oils.",
    "dandelion": "Dandelions provide nectar and pollen for pollinators.",
    "hibiscus": "Some hibiscus species are used to prepare colorful herbal teas.",
    "lily": "Lilies are flowering plants grown in gardens around the world.",
    "fern": "Ferns reproduce using spores rather than flowers and seeds.",
}


st.title("🌿 Plant Finder")
st.write(
    "Step outside, photograph a flower or plant, "
    "and explore what an AI image classifier recognizes."
)

st.sidebar.markdown("### 🌱 How it works")
st.sidebar.write(
    "1. Take a clear photo.\n"
    "2. Upload your image.\n"
    "3. Explore the model's predictions."
)
st.sidebar.caption(
    "This app uses a general-purpose image classifier. "
    "Predictions may not identify the exact plant species."
)

uploaded_file = st.file_uploader(
    "Upload a flower or plant photo",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        image.verify()

        # Reopen after verification and normalize the color mode.
        uploaded_file.seek(0)
        image = Image.open(uploaded_file).convert("RGB")

        col1, col2 = st.columns(2)

        with col1:
            st.image(
                image,
                caption="Your uploaded photo",
                use_container_width=True,
            )

        with col2:
            st.subheader("🔍 Image analysis")

            with st.spinner("Loading model and analyzing image..."):
                classifier = load_classifier()
                results = classifier(image, top_k=3)

            st.success("Predictions ready!")

            for i, item in enumerate(results, start=1):
                label = item["label"]
                score = item["score"] * 100

                st.metric(
                    label=f"Result {i}: {label}",
                    value=f"{score:.1f}%",
                )

            top_label = results[0]["label"].lower()

            st.markdown("---")
            st.subheader("🌼 Quick fact")

            matched_fact = next(
                (
                    fact
                    for keyword, fact in PLANT_FACTS.items()
                    if keyword in top_label
                ),
                None,
            )

            if matched_fact:
                st.info(matched_fact)
            else:
                st.info(
                    "No specific fact is available for this prediction yet. "
                    "Research the predicted label to learn more."
                )

            st.caption(
                "Scores indicate the model's confidence in each predicted "
                "ImageNet class; they do not guarantee correct identification."
            )

    except (UnidentifiedImageError, OSError, ValueError):
        st.error("The uploaded file could not be read as a valid image.")

    except Exception:
        st.error(
            "Image analysis failed. Check your internet connection, "
            "model availability, and installed dependencies, then try again."
        )

st.markdown("---")
st.subheader("💡 Explore nature")
st.write(
    "Use this project as a starting point for discovering plants outdoors. "
    "For reliable species identification, compare predictions with a "
    "trusted botanical reference."
)