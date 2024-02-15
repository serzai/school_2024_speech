# Импорт необходимых библиотек
import streamlit as st
import speech_recognition as speech_rec


# Распознавание голоса
def recognizing(audio, lang):
    user_audio = speech_rec.AudioFile(audio)

    rec = speech_rec.Recognizer()
    with user_audio as audio_file:
        audio_content = rec.record(audio_file)
        del user_audio
        del audio_file

    if lang == 'Английский':
        final_text = rec.recognize_google(audio_content)
    if lang == 'Русский':
        final_text = rec.recognize_google(audio_content, language='ru-RU')

    return final_text


st.title('Преобразование аудио в текст')
st.write('Загрузите файл, далее выберите язык и нажмите "Преобразовать". Чтобы сбросить прогресс, перезагрузите страницу.')

audio = st.file_uploader('Загрузите файл (принимаются только файлы с расширением .wav)')
st.audio(audio)

lang = st.selectbox("Выберите язык:", ['Английский', 'Русский'])

send = st.button('Преобразовать')

if send:
    with st.spinner(text='Преобразовываем...'):
        text = recognizing(audio, lang)
        file = open("Результат.txt", "w", encoding='utf-8')
        file.write(text)
        file.close()
        file = open('Результат.txt', 'r', encoding='utf-8')
        st.success('Успешно выполнено! Скачайте файл ниже:')
    st.download_button(data=file, label='Скачать', file_name='Результат')
