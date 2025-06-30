import streamlit as st
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(
    page_title="Olympus Compression",
    page_icon="🗻",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f0f4f8;
    }
    .main {
        background-color: white;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    img {
        border-radius: 10px;
        border: 2px solid #ccc;
        margin-top: 10px;
    }
    .css-1aumxhk {
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>🗻 Olympus Compression</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #34495E;'>Kompresi Gambar Cepat, Mudah & Visual</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- Upload File ---
uploaded_file = st.file_uploader(
    "📤 Upload gambar (JPG / PNG)", 
    type=["jpg", "jpeg", "png"],
    key="main_uploader"  # ✅ Tambah key agar aman
)

if uploaded_file:
    # Load dan tampilkan gambar asli
    image = Image.open(uploaded_file)
    st.markdown("**🖼️ Sebelum Kompresi:**")
    st.image(image, use_column_width=True)

    # Slider kompresi
    quality = st.slider("🎚️ Pilih Tingkat Kompresi (Kualitas):", 10, 100, 70)
    st.markdown(f"🔧 Kualitas dipilih: **{quality}%**")

    # Tombol untuk mulai kompresi
    if st.button("⚙️ Kompres Sekarang"):
        with st.spinner("⏳ Mengompresi gambar, mohon tunggu..."):
            progress = st.progress(0)

            # Simulasikan proses loading
            import time
            for i in range(1, 6):
                time.sleep(0.1)
                progress.progress(i * 20)

            # Proses kompresi
            img_bytes = io.BytesIO()
            if image.mode != "RGB":
                image = image.convert("RGB")
            image.save(img_bytes, format="JPEG", quality=quality, optimize=True)
            img_bytes.seek(0)

        progress.empty()  # Hapus progress bar

        # Hitung ukuran
        original_size_kb = round(len(uploaded_file.getvalue()) / 1024, 2)
        compressed_size_kb = round(len(img_bytes.getvalue()) / 1024, 2)
        saved_percent = round((1 - (compressed_size_kb / original_size_kb)) * 100, 2)

        # Tampilkan hasil
        st.markdown("**📊 Hasil Kompresi:**")
        st.markdown(f"- Ukuran Sebelum: `{original_size_kb} KB`")
        st.markdown(f"- Ukuran Sesudah: `{compressed_size_kb} KB`")
        st.markdown(f"- Hemat: `{saved_percent}%`")

        st.markdown("**🖼️ Setelah Kompresi:**")
        st.image(img_bytes, use_column_width=True)

        # Tombol download
        st.download_button(
            label="💾 Download Gambar Hasil",
            data=img_bytes,
            file_name="olympus_compressed.jpg",
            mime="image/jpeg"
        )


else:
    st.info("Silakan upload gambar terlebih dahulu untuk memulai kompresi.")
