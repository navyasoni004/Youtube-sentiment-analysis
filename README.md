# YouTube Sentiment Analysis

A Python-based project that analyzes the sentiment of YouTube video comments using multiple NLP models and libraries. This project compares different sentiment analysis approaches to provide comprehensive insights into audience sentiment.

## 📋 Project Overview

This application extracts comments from YouTube videos and performs sentiment analysis using three different approaches:
- **VADER** (Valence Aware Dictionary and sEntiment Reasoner)
- **TextBlob** - A simpler, lexicon-based approach
- **Transformer Models** - State-of-the-art deep learning models via Hugging Face

The results are visualized in a pie chart showing the distribution of positive, negative, and neutral sentiments.

## 🚀 Features

- **YouTube Integration**: Automatically fetches comments from any YouTube video
- **Text Preprocessing**: Cleans comments by removing URLs, special characters, and normalizing text
- **Multi-Model Analysis**: Compare sentiment scores across three different sentiment analysis models
- **Sentiment Classification**: Categorizes sentiments as Positive, Negative, or Neutral
- **Data Visualization**: Generates pie charts to visualize sentiment distribution
- **Model Comparison**: Side-by-side comparison of different sentiment analysis approaches

## 📁 Project Structure

```
Youtube-sentiment-analysis/
├── main.py                      # Main application entry point
├── youtube_api.py               # YouTube API integration
├── preprocessing.py             # Text cleaning and preprocessing
├── sentiment.py                 # VADER sentiment analysis
├── sentiment_textblob.py        # TextBlob sentiment analysis
├── sentiment_transformers.py    # Transformer-based sentiment analysis
├── README.md                    # Project documentation
└── LICENSE                      # MIT License
```

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- YouTube API Key
- pip package manager

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/navyasoni004/Youtube-sentiment-analysis.git
   cd Youtube-sentiment-analysis
   ```

2. **Install required packages**:
   ```bash
   pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
   pip install nltk textblob transformers torch matplotlib
   ```

3. **Download NLTK data** (required for VADER):
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

4. **Set up YouTube API Key**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project and enable YouTube Data API v3
   - Generate an API key
   - Replace the `API_KEY` in `youtube_api.py` with your own key

## 📖 Usage

Run the main script:
```bash
python main.py
```

When prompted, enter a YouTube video URL:
```
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

The program will:
1. Extract the video ID from the URL
2. Fetch up to 100 comments from the video
3. Clean and preprocess the comments
4. Analyze sentiment using all three models
5. Display cleaned comments, sentiment scores, and classification
6. Show a comparison of different sentiment analysis models
7. Display a pie chart with sentiment distribution

## 📊 Output Example

```
Cleaned comments:
this video is amazing
loved every second of it
not my cup of tea
...

Sentiment Scores:
0.7564
0.8439
-0.5423
...

Final Sentiment Count:
Counter({'Positive': 67, 'Neutral': 22, 'Negative': 11})

MODEL COMPARISON:
Text: this video is amazing
VADER: 0.7564
TextBlob: 0.85
Transformer: POSITIVE 0.9987
```

## 🧠 Models Used

### 1. VADER (Sentiment Intensity Analyzer)
- Rule-based lexicon approach
- Great for social media content
- Returns compound score: -1 (negative) to +1 (positive)

### 2. TextBlob
- Simple lexicon-based sentiment analyzer
- Returns polarity score: 0.0 (negative) to 1.0 (positive)
- Lightweight and fast

### 3. Transformer (Hugging Face)
- Pre-trained deep learning models
- State-of-the-art accuracy
- Returns: sentiment label (POSITIVE/NEGATIVE/NEUTRAL) and confidence score

## 📋 Requirements

- `google-auth-oauthlib` - Google authentication
- `google-auth-httplib2` - HTTP library for Google API
- `google-api-python-client` - YouTube Data API
- `nltk` - Natural Language Toolkit (VADER)
- `textblob` - TextBlob sentiment analysis
- `transformers` - Hugging Face transformers
- `torch` - PyTorch (required by transformers)
- `matplotlib` - Data visualization

## ⚠️ Important Notes

- **API Key Security**: Never commit your API key to version control. Consider using environment variables
- **Rate Limits**: YouTube API has rate limits (default: 10,000 units per day)
- **Comment Limitations**: The current implementation fetches top 100 comments only
- **Text Length**: Transformer models have a 512 token limit (handled in code)

## 🔄 Workflow

1. **Extract Video ID** → Extract from YouTube URL
2. **Fetch Comments** → Use YouTube API to get video comments
3. **Preprocess** → Clean text (remove URLs, symbols, lowercase)
4. **Analyze** → Run sentiment analysis with three models
5. **Classify** → Convert scores to labels (Positive/Negative/Neutral)
6. **Visualize** → Display pie chart with sentiment distribution

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new sentiment analysis models
- Enhance preprocessing methods

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Navya Soni**
- GitHub: [@navyasoni004](https://github.com/navyasoni004)

## 🙏 Acknowledgments

- NLTK VADER for rule-based sentiment analysis
- TextBlob for lexicon-based analysis
- Hugging Face Transformers for deep learning models
- Google YouTube API for video data access

## 📞 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.