A simple Python based password generator in order to spray passwords at a target

### Installation

```bash
git clone https://github.com/ray-truong/Password-list-generator.git
cd Password-list-generator
chmod +x password_sprayer.py
```

### Usage (recommended)

Move the script into your PATH:

```bash
sudo mv password_sprayer.py /usr/local/bin/sprayer
```

Then run from anywhere:

```bash
sprayer
```

### Alternative: Bash Alias

```bash
echo "alias sprayer='python3 /path/to/password_sprayer.py'" >> ~/.zshrc
source ~/.zshrc
```
