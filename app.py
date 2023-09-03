"""Awesome UI for the Music Genre Classifier"""
import gradio as gr

from transformers import pipeline

classifier = pipeline(
    "audio-classification",
    model="mahimairaja/distilhubert-music-classifier-finetuned-gtzan",
)


def classifiy_music(audio):
    """
    Outputs the label for the given audio
    """
    label = classifier(audio)
    outputs = {}
    for pred_value in label:
        outputs[pred_value["label"]] = pred_value["score"]
    return outputs


TITLE = "Music Genre Classifier"

demo = gr.Blocks()

mic_translate = gr.Interface(
    fn=classifiy_music,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs=gr.outputs.Label(),
    title=TITLE,
)

file_translate = gr.Interface(
    fn=classifiy_music,
    inputs=gr.Audio(source="upload", type="filepath"),
    outputs=gr.outputs.Label(),
    examples=[
        "assets/song_01.wav",
        "assets/song_02.wav",
        "assets/song_03.wav",
        "assets/song_04.wav",
    ],
    title=TITLE,
)

with demo:
    gr.TabbedInterface(
        [mic_translate, file_translate],
        ["Microphone", "Audio File"]
        )

demo.launch()
