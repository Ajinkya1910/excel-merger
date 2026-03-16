# Deployment Guide for Excel Merger

## 🚀 Quick Deployment Summary

Choose one deployment method based on your needs:

| Method | Setup Time | Cost | Ease | Best For |
|--------|-----------|------|------|----------|
| **Streamlit Cloud** | 2 min | Free | ⭐⭐⭐⭐⭐ | Teams & Sharing |
| **Local Machine** | 5 min | Free | ⭐⭐⭐⭐ | Personal Use |
| **Docker** | 10 min | Free* | ⭐⭐⭐ | Production |
| **Render** | 5 min | Free* | ⭐⭐⭐⭐ | Always-On |
| **PythonAnywhere** | 10 min | Free* | ⭐⭐⭐ | Simple Hosting |

*Free tier available with limitations

---

## 🌐 Streamlit Cloud (Recommended - Fastest)

### 1. Prerequisites
- GitHub account (free)
- Streamlit Cloud account (free)

### 2. Deploy in 2 Minutes

```bash
# Push code to GitHub
git push origin main

# Go to https://share.streamlit.io
# Click "New app" → Select your repo → Done! ✅
```

**Public URL:** `https://share.streamlit.io/YOUR_USERNAME/excel-merger/main/app.py`

### 3. Update After Changes

```bash
git commit -am "Your change description"
git push origin main
# Auto-deployed in 1-2 minutes
```

---

## 💻 Deploy Locally (Desktop/Laptop)

### For Personal Use or Team on Same Network

```bash
# From project directory
streamlit run app.py

# Access at: http://localhost:8501
```

### Access from Other Machines on Network

```bash
# Get your machine's IP
ipconfig getifaddr en0  # macOS
# or
hostname -I  # Linux/Windows in WSL

# Access from another computer
http://YOUR_MACHINE_IP:8501
```

### Keep Running in Background (macOS/Linux)

```bash
# Using nohup
nohup streamlit run app.py > app.log 2>&1 &

# Using screen
screen -S excel-merger
streamlit run app.py
# Press Ctrl+A then D to detach
```

---

## 🐳 Docker Deployment

### Use Docker for Consistent Environment

```bash
# Create Dockerfile (already done)
# Build image
docker build -t excel-merger .

# Run container
docker run -p 8501:8501 excel-merger

# Access at: http://localhost:8501
```

### Deploy on Server with Docker

```bash
# On your server
docker run -d -p 8501:8501 excel-merger

# Access at: http://YOUR_SERVER_IP:8501
```

---

## 🎯 Render Free Tier

### 1. Create Render Account
- Go to [render.com](https://render.com)
- Sign up with GitHub

### 2. Create Web Service
- Click "New +" → "Web Service"
- Select your GitHub repo
- Configure:
  - **Build Command:** `pip install -r requirements.txt`
  - **Start Command:** `streamlit run app.py --server.port 10000`
  - **Instance Type:** Free

### 3. Deploy
- Click "Create Web Service"
- Render builds and deploys automatically
- Get public URL in dashboard

### 4. Limitations
- Free tier: 15-minute auto-spin down when unused
- Starts up in ~1-2 minutes on first request
- No custom domain on free tier

---

## 🐍 PythonAnywhere Hosting

### 1. Create Account
- Go to [pythonanywhere.com](https://www.pythonanywhere.com)
- Sign up (free account available)

### 2. Upload Files
- Go to Files tab
- Create new directory: `/home/USERNAME/excel-merger`
- Upload all project files via web interface

### 3. Create Web App
- Web tab → Add new web app
- Choose Python version (3.9+)
- Select "Manual configuration"

### 4. Configure
Edit `/var/www/USERNAME_pythonanywhere_com_wsgi.py`:

```python
import sys
import os
from streamlit.cli import main

sys.path.insert(0, '/home/USERNAME/excel-merger')
os.chdir('/home/USERNAME/excel-merger')

# Run Streamlit app
if __name__ == '__main__':
    main(['run', 'app.py', '--server.port', '5000'])
```

### 5. Restart & Access
- Reload web app
- Access at: `http://USERNAME.pythonanywhere.com`

---

## ☁️ AWS EC2 Deployment

### 1. Launch EC2 Instance
- Instance type: `t3.micro` (free tier eligible)
- Security group: Allow port 8501 (TCP)
- Key pair for SSH access

### 2. SSH into Instance

```bash
ssh -i your-key.pem ec2-user@YOUR_INSTANCE_IP
```

### 3. Install Dependencies

```bash
# Update system
sudo yum update -y

# Install Python
sudo yum install python3 -y

# Install git
sudo yum install git -y
```

### 4. Clone and Run

```bash
git clone https://github.com/YOUR_USERNAME/excel-merger.git
cd excel-merger
pip3 install -r requirements.txt
streamlit run app.py
```

### 5. Keep Running (Using Tmux)

```bash
tmux new-session -d -s excel
tmux send-keys -t excel "cd ~/excel-merger && streamlit run app.py" Enter
```

### 6. Access
- Open: `http://YOUR_EC2_IP:8501`

### ⚠️ Note
- EC2 free tier: 750 hours/month for 12 months
- Stop instance when not in use to avoid charges

---

## 🏢 Self-Hosted Linux Server

### 1. SSH into Server

```bash
ssh user@your-server.com
```

### 2. Clone Project

```bash
git clone https://github.com/YOUR_USERNAME/excel-merger.git
cd excel-merger
```

### 3. Install Python & Dependencies

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip -y
pip3 install -r requirements.txt
```

### 4. Run with Systemd (Auto-restart)

Create `/etc/systemd/system/excel-merger.service`:

```ini
[Unit]
Description=Excel Merger Streamlit App
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/excel-merger
ExecStart=/usr/bin/python3 -m streamlit run app.py --server.port 8501 --server.address 0.0.0.0
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable excel-merger
sudo systemctl start excel-merger
sudo systemctl status excel-merger
```

### 5. Setup Reverse Proxy (Nginx)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 6. Access
- Go to: `http://your-domain.com`

---

## 🔒 Production Security Checklist

### Before Going Live

- [ ] Add authentication/password protection
- [ ] Use HTTPS (SSL certificate)
- [ ] Set environment variables (no hardcoded secrets)
- [ ] Limit upload file size
- [ ] Add rate limiting
- [ ] Monitor logs
- [ ] Regular backups
- [ ] Test error handling
- [ ] Document API endpoints

### Add Authentication

Edit `app.py` (add to top):

```python
import os

# Get password from environment variable
APP_PASSWORD = os.getenv("EXCEL_MERGER_PASSWORD", "change_me_in_production")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔐 Excel Merger - Login")
    password = st.text_input("Enter password:", type="password")
    
    if st.button("Login"):
        if password == APP_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Incorrect password")
            st.stop()
    else:
        st.stop()

# Rest of your app code...
```

### Enable HTTPS

#### On Streamlit Cloud
- Automatic ✓

#### On Server with Nginx
```bash
sudo apt-get install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

---

## 📊 Performance Optimization for Production

### 1. Enable Caching

```python
@st.cache_data
def load_file(uploaded_file):
    return pd.read_excel(uploaded_file)
```

### 2. Set Resource Limits

```bash
# In systemd service or Docker
# Limit memory to 1GB
MemoryLimit=1G

# Limit CPU to 1 core
CPUQuota=100%
```

### 3. Monitor Usage

```bash
# Check Streamlit logs
tail -f streamlit_logs.txt

# Monitor system resources
top
# or
htop
```

---

## 🆘 Deployment Troubleshooting

| Issue | Solution |
|-------|----------|
| **Port 8501 in use** | `streamlit run app.py --server.port 8502` |
| **Connection refused** | Check firewall, ensure server is running |
| **Slow uploads** | Increase `maxUploadSize` in config.toml |
| **Memory errors** | Reduce file size limit or add swap |
| **Module not found** | Reinstall: `pip install -r requirements.txt` |
| **Permission denied** | Check file permissions: `chmod +x app.py` |

---

## 📈 Scaling Strategies

### For High Traffic

1. **Streamlit Cloud** - Automatically scales
2. **Load Balancer** - Multiple instances behind Nginx
3. **Database** - Store results instead of processing on-demand
4. **Queue System** - Async processing with Celery

### For Large Files

1. Split processing across workers
2. Use streaming/chunking for uploads
3. Move to batch processing

---

## 🎯 Recommended Deployment Path

**For Individuals:**
```
Local Testing → Streamlit Cloud → Done ✅
(5 min) → (2 min)
```

**For Teams:**
```
GitHub Repo → Streamlit Cloud → Teams share link ✅
(2 min) → (2 min)
```

**For Production:**
```
GitHub → Docker → Self-hosted/AWS EC2 → Nginx/SSL ✅
(5 min) → (10 min) → (15 min)
```

---

## 📞 Support Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Cloud FAQ](https://docs.streamlit.io/streamlit-cloud/get-started)
- [Docker Docs](https://docs.docker.com)
- [Render Docs](https://render.com/docs)

---

**Ready to deploy? Start with Streamlit Cloud - it takes 2 minutes! 🚀**
