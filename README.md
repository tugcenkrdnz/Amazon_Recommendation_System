# 🛒 Amazon Product Recommendation System

A Collaborative Filtering-based recommendation engine built with Python and Streamlit. It analyzes 8 million rows of Amazon electronics data to find product associations.

## 🛠️ How It Works
1. **User Overlap:** It identifies users who purchased a specific item.
2. **Behavioral Analysis:** It looks at what else those specific users bought.
3. **Quality Filter:** It sorts the co-purchased items by their average rating and recommends the top 3.

## 🚀 Deployment
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`

## 📊 Dataset
The model uses the Amazon Electronics Ratings dataset, pre-processed to ensure high-quality recommendations.