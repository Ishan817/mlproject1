# import nltk

# # downloads (run once)
# nltk.download('punkt')
# nltk.download('brown')
# nltk.download('stopwords')
# nltk.download('wordnet')

# # Brown corpus
# from nltk.corpus import brown
# for category in brown.categories():
#     print(f"{category}: {len(brown.words(categories=category))}")

# # Tokenizers
# from nltk.tokenize import RegexpTokenizer, TreebankWordTokenizer, TweetTokenizer

# text ="NLTK is powerful . It is widely used in NLP"
# print(RegexpTokenizer(r'\w+').tokenize(text))

# text ="I don't like me"
# print(TreebankWordTokenizer().tokenize(text))

# text = "w000wI dont like this!!! #isthisworking http://test.com"
# print(TweetTokenizer().tokenize(text))

# # Lemmatization
# lemmatizer = nltk.WordNetLemmatizer()
# print(lemmatizer.lemmatize("running"))

# # Stemming
# from nltk.stem import PorterStemmer
# ps = PorterStemmer()
# print(ps.stem("walking"))

# # Stopwords
# from nltk.corpus import stopwords
# s = [
#     "this is a my nlp course",
#     "this course is about nlp",
#     "we are learning nlp"
# ]

# corpus = " ".join(s)
# words = nltk.word_tokenize(corpus)

# stop_words = set(stopwords.words('english'))
# filtered_words = [w for w in words if w.lower() not in stop_words]

# print("Filtered words:", filtered_words)

# # Final tokenize
# s = "I Love Machine Learning."
# print(nltk.word_tokenize(s.lower()))

# import numpy, pandas, sklearn, nltk
# print("System stable")
# import numpy as np
# x=np.array([-1,2,3,-2])
# R = np.maximum(0,x)
# print(R)
# T=np.tanh(x)
# print(T)
# S=1/(1+np.exp(-x))
# print(S)
# soft_max=np.exp(x)/np.sum(np.exp(x))
# print(soft_max)
# step_func = np.where(x>0, 1, 0)
# print(step_func)
# import numpy as np
# X=np.array([2,3])
# W=np.array([0.5, 0.8])
# b=0.2
# z= np.dot(X,W) + b
# print(z)
# R=max(0,z)
# print(R)

