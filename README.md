## 🌟 **CipherCanvas**  

CipherCanvas is a simple and powerful Python tool that lets you hide and retrieve secret messages within images. Whether you’re a beginner curious about steganography or someone looking for a secure way to communicate, CipherCanvas is the tool for you!  

---

## ✨ Features  
- **Hide Messages**: Embed secret messages inside images.  
- **Reveal Messages**: Extract hidden messages effortlessly.  
- **Cross-Platform**: Compatible with Windows, Linux, macOS, and Termux.  
- **User-Friendly**: Clean, interactive command-line interface.  

---

## 🛠️ Requirements  

1. **Python 3.6 or newer** installed on your system.  
2. Install the required libraries:  
   ```bash
   pip install pillow colorama
   ```  

### For Termux Users:  
If you encounter issues installing **Pillow**, follow these steps:  

## 🚀 Getting Started with Termux  

1. **Download Termux**:  
   Get the latest version of Termux from [F-Droid]([https://f-droid.org/](https://f-droid.org/en/packages/com.termux/)).  

2. **Install Termux**:  
   Once downloaded, install the app on your device.  

3. **Setup Termux**:  
   Open Termux and run the following commands to set up your environment:  
   ```bash
   apt update  
   apt upgrade  
   pkg install git  
   pkg install python  
   ```  



1. Install necessary packages:  
   ```bash
   pkg install python libjpeg-turbo libpng zlib freetype libwebp -y
   ```  

2. Upgrade essential tools:  
   ```bash
   pip install --upgrade pip setuptools wheel
   ```  

3. Install Pillow without cache:  
   ```bash
   pip install --no-cache-dir Pillow
   ```  

--- 


## 🚀 Getting Started  

1. **Clone this repository**:  
   ```bash
   git clone https://github.com/Moajjem404/CipherCanvas.git
   cd CipherCanvas
   ```  

2. **Run the script**:  
   ```bash
   python main.py
   ```  

---

## 📖 How to Use  

### 1️⃣ Embed a Secret Message  
- Select option `1` in the menu.  
- Enter:  
  - Path to the image file.  
  - The message you want to hide.  
  - Path to save the output image.  
- Your message will be hidden in the image and saved securely!  

### 2️⃣ Extract a Secret Message  
- Select option `2` in the menu.  
- Enter the path to the image containing the hidden message.  
- CipherCanvas will reveal the secret message for you.  

### 3️⃣ Exit  
- Select option `0` to close the program.  

---

## 📄 Example  

Here’s a quick example to get started:  

**Embed Message**  
```bash  
Enter the image file path: input_image.png  
Enter the secret message to embed: Hello, CipherCanvas!  
Enter the output image file path: output_image.png  
Message embedded successfully!  
```  

**Extract Message**  
```bash  
Enter the image file path: output_image.png  
Extracted Message: Hello, CipherCanvas!  
```  

---

## 👨‍💻 Author  

Created :- by **ShadowGlint**.  
- Explore more on **GitHub**: [Moajjem404](https://github.com/Moajjem404)  

---

## 🌟 Contributions  

Your contributions are welcome! Fork the repository, create a new branch, and submit a pull request with your ideas and improvements.  



