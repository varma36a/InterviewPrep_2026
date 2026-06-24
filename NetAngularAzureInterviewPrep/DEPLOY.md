# Deploy — Streamlit Community Cloud (recommended, free)

## Live deploy settings

| Setting | Value |
|---|---|
| **Repository** | `varma36a/InterviewPrep_2026` |
| **Branch** | `main` |
| **Main file** | `NetAngularAzureInterviewPrep/app.py` |
| **App URL (suggested)** | `net-interview-prep` |

## One-click deploy

1. Open [share.streamlit.io](https://share.streamlit.io/)
2. Sign in with GitHub (`varma36a`)
3. Click **Create app** → **Yup, I have an app**
4. Paste GitHub URL to entrypoint:
   `https://github.com/varma36a/InterviewPrep_2026/blob/main/NetAngularAzureInterviewPrep/app.py`
5. Set custom subdomain: `net-interview-prep` (or any available name)
6. Click **Deploy**

Streamlit reads `NetAngularAzureInterviewPrep/requirements.txt` automatically.

Sibling folders (`DesignPatternsLearnignFolder/`, `Linq/`) are at repo root so live C# pattern and LINQ code loads correctly.

## Docker / Fly.io (optional)

```bash
cd InterviewPrep_2026
fly deploy --remote-only --auto-confirm --now
```

Requires Fly.io billing on the account.

## Local run

```bash
cd NetAngularAzureInterviewPrep
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
