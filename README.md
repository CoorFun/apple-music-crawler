# apple-music-crawler

This simple script is used to extract track, artist, and album name from a given apple music playlist url.

### Setup

##### 1. In your Terminal, direct to the project folder

A simple way to do so, input `cd` and a white space in the terminal window, then drag and drop this project folder into the Terminal window

Finally, a completed command should be like this:

```bash
cd ~/Download/apple-music-crawler
```

(Don't forget to press Enter to execute)

##### 2. Once you are in the project directory, install project dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### Usage

##### 1. Find out the target **playlist** urls from [Apple Music](https://music.apple.com/fr/browse)

> Beware that this script only supports playlist extraction at the moment

##### 2. Use any text editor to open up the `extract.py` file

##### 3. Fill urls as a tuple in `(name, url)` format, where the `name` parameter is not necessarily bounded to the playlist name on the web page

Here is an example with three pre-filled playlist urls and their names:
 
```python
urls = [
    ("jazz", "https://music.apple.com/us/playlist/smooth-jazz-essentials/pl.cbefd5b0db0e4d9698da967311cb811c"),
    ("top100", "https://music.apple.com/us/playlist/top-100-france/pl.6e8cfd81d51042648fa36c9df5236b8d"),
    ("puer_french", "https://music.apple.com/us/playlist/pure-french/pl.cf50d6eaeb6c4badbe72d93466694995")
]
```

##### 4. Save the modification and exit

##### 5. Run `python extract.py` command, this will take a while if you have multiple urls need to be extracted

##### 6. The extracted results are saved under your current directory with the name we've specified in Step 3

##### 7. Use any excel software open up the exported `csv` file