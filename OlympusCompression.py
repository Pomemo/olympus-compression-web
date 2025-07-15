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
    image = Image.open(uploaded_file)
    st.markdown("**🖼️ Sebelum Kompresi:**")
    st.image(image, use_container_width=True)

    # Slider dengan batas maksimum 95%
    quality = st.slider(
        label="🎚️ Pilih Tingkat Kompresi (Kualitas):",
        min_value=10,
        max_value=85,
        value=70,
        step=1
    )
    st.caption("⚠️ Kualitas maksimal dibatasi hingga 85% untuk mencegah ukuran file membengkak.")
    st.markdown(f"🔧 Kualitas dipilih: **{quality}%**")

    # Tombol kompres
    if st.button("⚙️ Kompres Sekarang"):
        with st.spinner("⏳ Mengompresi gambar, mohon tunggu..."):
            progress = st.progress(0)

            import time
            for i in range(101):
                time.sleep(0.1)
                progress.progress(i)

            img_bytes = io.BytesIO()
            if image.mode != "RGB":
                image = image.convert("RGB")
            image.save(img_bytes, format="JPEG", quality=quality, optimize=True)
            img_bytes.seek(0)

        progress.empty()

        # Hasil
        original_size_kb = round(len(uploaded_file.getvalue()) / 1024, 2)
        compressed_size_kb = round(len(img_bytes.getvalue()) / 1024, 2)
        saved_percent = round((1 - (compressed_size_kb / original_size_kb)) * 100, 2)

        st.markdown("**📊 Hasil Kompresi:**")
        st.markdown(f"- Ukuran Sebelum: `{original_size_kb} KB`")
        st.markdown(f"- Ukuran Sesudah: `{compressed_size_kb} KB`")
        st.markdown(f"- Hemat: `{saved_percent}%`")

        st.markdown("**🖼️ Setelah Kompresi:**")
        st.image(img_bytes, use_container_width=True)

        st.download_button(
            label="💾 Download Gambar Hasil",
            data=img_bytes,
            file_name="olympus_compressed.jpg",
            mime="image/jpeg"
        )
else:
    st.info("Silakan upload gambar terlebih dahulu untuk memulai kompresi.")

# --- Sidebar Help Menu ---
with st.sidebar.expander("❓ Bantuan / Panduan Penggunaan"):
    st.markdown("""
### 🧭 Cara Menggunakan Olympus Compression
1. **Upload gambar** dalam format `.jpg`, `.jpeg`, atau `.png`.
2. **Atur tingkat kualitas** gambar menggunakan slider (10–100%).
   - Semakin rendah nilainya, ukuran file akan lebih kecil.
   - Semakin tinggi, kualitas lebih tinggi tapi ukuran besar.
3. Klik tombol **⚙️ Kompres Sekarang** untuk memulai proses.
4. Tunggu sebentar... ⏳ Progress bar akan muncul selama proses kompresi.
5. Setelah selesai:
   - Lihat perbandingan gambar **Sebelum & Sesudah**
   - Dapatkan info ukuran & efisiensi
   - Klik **💾 Download** untuk menyimpan hasilnya

---

### ℹ️ Tips Teknis
- Format gambar yang didukung: **JPG, JPEG, PNG**
- Kompresi dilakukan dengan format JPEG
- Gunakan kualitas 60–80% untuk hasil optimal
- Olympus berbasis web, **tidak perlu install apa pun**
- Direkomendasikan menggunakan browser seperti **Chrome atau Edge**

---

### 🤝 Hubungi Kami
Jika Anda mengalami kendala, silakan hubungi tim kami melalui:
📧 olympus.support@example.com
    """)
