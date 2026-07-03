# ⚙️ SnapClass | Biometric Core Engine & Multi-Modal AI Backend

[![Live App Engine](https://img.shields.io/badge/Live-Biometric%20Engine-FF4B4B?style=for-the-badge)](https://snapclass-main-v2.streamlit.app/)
[![Live Landing Portal](https://img.shields.io/badge/Live-Landing%20Core-5865F2?style=for-the-badge)](https://snapclass-frontend-ten.vercel.app/)

Welcome to the computational heart of SnapClass. This repository houses the multi-modal AI biometric backend engineered to handle high-performance facial feature extraction, acoustic signal processing, stateful real-time data streaming, and secure cloud synchronization layers. 

Built natively in Python using a decoupled microservices philosophy, this engine interacts seamlessly with our edge-cached [Frontend Landing Core](https://snapclass-frontend-ten.vercel.app/) to deliver safe, rapid, and automated classroom attendance auditing.

---

## 🧠 Core AI & Engineering Architecture

### 1. Computer Vision Pipeline (Face Recognition Engine)
* **Facial Landmark Mapping:** Employs a pre-trained Deep Residual Network (ResNet-34) via the `dlib` backend to map structural facial contours and isolate individual coordinates.
* **128-D Vector Embeddings:** Transports crop face matrices into low-dimensional vector spaces, calculating localized spatial clusters to represent unique identities.
* **Vector Distance Optimization:** Computes Euclidean vector distance metrics against pre-registered student templates, utilizing tight boundary thresholds to maximize recognition accuracy while eliminating proxy sign-ins.

### 2. Acoustic Feature Extraction (Sequential Voice Biometrics)
* **Waveform Signal Processing:** Leverages `librosa` and digital signal processing architectures to slice raw audio inputs and eliminate background environmental classroom decibel noise.
* **Voice-Print Vector Generation:** Uses an open-source d-vector embedding framework (`Resemblyzer`) to capture high-level speaker voice characteristics independent of the spoken text.
* **Real-Time Sequential Parsing:** Features a thread-safe validation algorithm to evaluate speakers one after another, matching voice signatures against active database templates securely.

### 3. Real-Time Cloud Synchronization Layer
* **Connection Pooling & RLS:** Built directly on top of the **Supabase (PostgreSQL)** cloud backend to handle parallel student check-in transactions.
* **Row-Level Security (RLS):** Enforces strict data isolation rules to guarantee that student biometric signatures are strictly secure and accessible only by authorized operational procedures.

---

## 🛠️ Computational Tech Stack

| Component Layer | Technology Stack | Architectural Purpose |
| :--- | :--- | :--- |
| **Reactive Compute Dashboard** | Streamlit Architecture (v1.58+) | Manages highly reactive, stateful user viewports, data tables, and high-frequency UI reruns. |
| **Vision Analytics Matrix** | FaceRecognition / Dlib / OpenCV | Executes face localization, affine image normalization, and concurrent vector distance scoring. |
| **Acoustic Wave Processor** | Resemblyzer / Librosa / SoundFile | Extracts frame-based spectral frequencies and translates high-frequency audio into distinct voice-prints. |
| **Database & Real-Time Sync** | Supabase Python SDK (Postgres Layer) | Handles persistent storage pipelines, user authentication states, and instant attendance logs. |
| **Runtime Environment** | Streamlit Community Cloud | Provides isolated, Python-optimized cloud hosting containers for high-performance ML workloads. |

---

## 📁 Repository Structural Blueprint

```text
├── app.py                  # Primary Application Orchestrator & Multi-Portal Gateway
├── requirements.txt        # Managed ML/AI Framework Dependency Matrix
├── README.md               # Technical Backend Engineering Documentation
├── .env                    # Local Environment Cryptographic Secrets (Git Ignored)
└── src/
    ├── components/
    │   └── subject_card.py # Dynamic HTML/CSS Component Custom Rendering Logic
    ├── database/
    │   └── supabase_db.py  # Supabase Client Wrapper & Transaction Query Layer
    └── screens/
        ├── home_screen.py     # Portal Router Selection Viewport
        ├── student_screen.py  # Face/Voice Capture Hub & Onboarding Flow
        └── teacher_screen.py  # Control Panel, Attendance Logs, & Roster Management
